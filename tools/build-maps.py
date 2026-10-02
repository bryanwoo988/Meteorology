#!/usr/bin/env python3
"""Build the app's offline base maps from Natural Earth (public domain).

Run:  venv/bin/python tools/build-maps.py

Writes data/maps/world.json (110m land + country borders) and
data/maps/seasia.json (50m, clipped to 85–135°E, 15°S–28°N). Rings are
[[lon, lat], ...] rounded to 0.01°, simplified with Douglas–Peucker so the
files stay small enough to precache. Natural Earth: https://www.naturalearthdata.com/
"""
import io, json, urllib.request, zipfile
from pathlib import Path
import shapefile  # pyshp

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "maps"
CACHE = ROOT / "venv" / "naturalearth"
BASE = "https://naciscdn.org/naturalearth"


def fetch(scale, kind, name):
    CACHE.mkdir(parents=True, exist_ok=True)
    z = CACHE / f"{name}.zip"
    if not z.exists():
        url = f"{BASE}/{scale}/{kind}/{name}.zip"
        print("  downloading", url)
        z.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    zf = zipfile.ZipFile(z)
    stem = name
    return shapefile.Reader(shp=io.BytesIO(zf.read(f"{stem}.shp")), dbf=io.BytesIO(zf.read(f"{stem}.dbf")),
                            shx=io.BytesIO(zf.read(f"{stem}.shx")))


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = (dx * dx + dy * dy) ** 0.5 or 1e-12
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]
        d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / norm
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return rdp(pts[: idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def rdp_ring(pts, eps):
    """A closed ring starts and ends at the same point, which gives
    Douglas-Peucker no baseline; split it at the point farthest from the start."""
    if len(pts) < 4 or pts[0] != pts[-1]:
        return rdp(pts, eps)
    x0, y0 = pts[0]
    k = max(range(len(pts)), key=lambda i: (pts[i][0] - x0) ** 2 + (pts[i][1] - y0) ** 2)
    return rdp(pts[: k + 1], eps)[:-1] + rdp(pts[k:], eps)


def rings(reader, eps, bbox=None, min_pts=4):
    out = []
    for shape in reader.shapes():
        parts = list(shape.parts) + [len(shape.points)]
        for a, b in zip(parts, parts[1:]):
            ring = shape.points[a:b]
            if bbox:
                x0, y0, x1, y1 = bbox
                if all(not (x0 <= x <= x1 and y0 <= y <= y1) for x, y in ring):
                    continue
            simple = rdp_ring([tuple(p) for p in ring], eps)
            if len(simple) >= min_pts:
                out.append([[round(x, 2), round(y, 2)] for x, y in simple])
    return out


def clip_ring(ring, bbox):
    """Clamp a ring to a box (Sutherland–Hodgman on each edge)."""
    x0, y0, x1, y1 = bbox
    def clip(pts, inside, cross):
        res = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            if inside(cur):
                if not inside(prev):
                    res.append(cross(prev, cur))
                res.append(cur)
            elif inside(prev):
                res.append(cross(prev, cur))
        return res
    def at_x(xv):
        return lambda p, q: [xv, p[1] + (q[1] - p[1]) * (xv - p[0]) / ((q[0] - p[0]) or 1e-12)]
    def at_y(yv):
        return lambda p, q: [p[0] + (q[0] - p[0]) * (yv - p[1]) / ((q[1] - p[1]) or 1e-12), yv]
    pts = ring
    for inside, cross in ((lambda p: p[0] >= x0, at_x(x0)), (lambda p: p[0] <= x1, at_x(x1)),
                          (lambda p: p[1] >= y0, at_y(y0)), (lambda p: p[1] <= y1, at_y(y1))):
        if not pts:
            break
        pts = clip(pts, inside, cross)
    return [[round(x, 2), round(y, 2)] for x, y in pts]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = {"source": "Natural Earth (public domain), naturalearthdata.com", "fetched": "2026-10-02"}

    land = rings(fetch("110m", "physical", "ne_110m_land"), 0.25)
    borders = rings(fetch("110m", "cultural", "ne_110m_admin_0_boundary_lines_land"), 0.25, min_pts=2)
    world = {**meta, "scale": "1:110m", "land": land, "borders": borders}
    (OUT / "world.json").write_text(json.dumps(world, separators=(",", ":")))

    box = (85, -15, 135, 28)
    land50 = [clip_ring(r, box) for r in rings(fetch("50m", "physical", "ne_50m_land"), 0.04, bbox=box)]
    land50 = [r for r in land50 if len(r) >= 4]
    borders50 = rings(fetch("50m", "cultural", "ne_50m_admin_0_boundary_lines_land"), 0.04, bbox=box, min_pts=2)
    seasia = {**meta, "scale": "1:50m", "bbox": box, "land": land50, "borders": borders50}
    (OUT / "seasia.json").write_text(json.dumps(seasia, separators=(",", ":")))

    for f in ("world.json", "seasia.json"):
        print(f"  data/maps/{f}  {(OUT / f).stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()

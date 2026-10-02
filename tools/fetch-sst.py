#!/usr/bin/env python3
"""Fetch sea-surface temperature grids for the ocean and ENSO maps.

Run:  python3 tools/fetch-sst.py

Source: NOAA OI SST V2 (1°, monthly), NOAA PSL, via OPeNDAP. Writes
  data/maps/sst-events.json  2° anomalies (vs the 1991–2020 December mean)
                             for December 2015 (El Niño), December 2013
                             (neutral) and December 2010 (La Niña)
  data/maps/sst-clim.json    4° 1991–2020 monthly-mean SST, 12 months
Both cover 60°N–60°S, longitudes rotated to −180…180, land = null.
"""
import json, re, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2"
EVENTS = {"elnino-2015-12": 408, "neutral-2013-12": 384, "lanina-2010-12": 348}   # months since Dec 1981
LAT_RANGE = (30, 149)      # lat index 30 = 59.5°N … 149 = 59.5°S


def fetch(url):
    return urllib.request.urlopen(url, timeout=120).read().decode()


def grid(text, var="sst"):
    """Parse an OPeNDAP .ascii Grid response into {time: rows}."""
    body = text.split("---------------------------------------------", 1)[1].split(f"{var}.time", 1)[0]
    out = {}
    for line in body.splitlines():
        m = re.match(r"^\[(\d+)\]\[(\d+)\],\s*(.*)$", line.strip())
        if m:
            out.setdefault(int(m.group(1)), []).append([float(v) for v in m.group(3).split(",")])
    return out


def axis(text, name, var="sst"):
    m = re.search(rf"\n{var}\.{name}\[\d+\]\n([^\n]+)", text)
    return [float(v) for v in m.group(1).split(",")]


def rotate(rows, lons):
    """Columns 0…360 → −180…180, rows north→south → south→north."""
    k = next(i for i, l in enumerate(lons) if l > 180)
    lons = [l - 360 for l in lons[k:]] + lons[:k]
    return [r[k:] + r[:k] for r in rows][::-1], lons


def clean(v, scale=1.0, missing=None):
    if missing is not None and v == missing:
        return None
    v *= scale
    return None if v < -5 or v > 40 else v


def main():
    out = ROOT / "data" / "maps"
    a, b = LAT_RANGE
    # December climatology at 2° and all months at 4°.
    clim_dec = fetch(f"{BASE}/sst.ltm.1991-2020.nc.ascii?sst%5B11:1:11%5D%5B{a}:2:{b}%5D%5B0:2:359%5D")
    dec = grid(clim_dec)[0]
    # The SST files are filled over land; the product's own land-sea mask (1 = ocean) blanks it.
    mask2 = grid(fetch(f"{BASE}/lsmask.nc.ascii?mask%5B0:1:0%5D%5B{a}:2:{b}%5D%5B0:2:359%5D"), "mask")[0]
    mask4 = grid(fetch(f"{BASE}/lsmask.nc.ascii?mask%5B0:1:0%5D%5B{a}:4:{b}%5D%5B0:4:359%5D"), "mask")[0]
    lats2, lons2 = axis(clim_dec, "lat"), axis(clim_dec, "lon")
    events = {}
    for name, t in EVENTS.items():
        txt = fetch(f"{BASE}/sst.mnmean.nc.ascii?sst%5B{t}:1:{t}%5D%5B{a}:2:{b}%5D%5B0:2:359%5D")
        rows = grid(txt)[0]
        anom = [[None if mk != 1 or (c := clean(x, 0.01, 32767)) is None or (d := clean(y)) is None else round(c - d, 1)
                 for x, y, mk in zip(r, dr, mr)] for r, dr, mr in zip(rows, dec, mask2)]
        events[name], lons = rotate(anom, lons2)
        print(name, sum(v is not None for r in events[name] for v in r), "ocean cells")
    lats = sorted(lats2)
    (out / "sst-events.json").write_text(json.dumps({
        "source": "NOAA OI SST V2 monthly means (NOAA PSL); anomalies relative to the 1991–2020 December mean",
        "url": "https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html", "fetched": "2026-10-02",
        "lon0": lons[0] - 1, "lat0": lats[0] - 1, "dlon": 2, "dlat": 2, "nx": len(lons), "ny": len(lats),
        "events": {k: [v for r in rows for v in r] for k, rows in events.items()},
    }, separators=(",", ":")))

    txt = fetch(f"{BASE}/sst.ltm.1991-2020.nc.ascii?sst%5B0:1:11%5D%5B{a}:4:{b}%5D%5B0:4:359%5D")
    g = grid(txt)
    lats4, lons4 = axis(txt, "lat"), axis(txt, "lon")
    months = []
    for t in range(12):
        rows, lons = rotate([[None if mk != 1 or (c := clean(x)) is None else round(c, 1) for x, mk in zip(r, mr)] for r, mr in zip(g[t], mask4)], lons4)
        months.append([v for r in rows for v in r])
    lats = sorted(lats4)
    (out / "sst-clim.json").write_text(json.dumps({
        "source": "NOAA OI SST V2, 1991–2020 long-term monthly means (NOAA PSL)",
        "url": "https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.html", "fetched": "2026-10-02",
        "lon0": lons[0] - 2, "lat0": lats[0] - 2, "dlon": 4, "dlat": 4, "nx": len(lons), "ny": len(lats), "months": months,
    }, separators=(",", ":")))
    for f in ("sst-events.json", "sst-clim.json"):
        print(f, (out / f).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()

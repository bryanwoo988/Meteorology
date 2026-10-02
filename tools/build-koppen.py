#!/usr/bin/env python3
"""Pack the Köppen–Geiger 1991–2020 map (Beck et al. 2023, CC0) for the app.

Run:  venv/bin/python tools/build-koppen.py <dir containing 1991_2020/*.tif>

Download koppen_geiger_tif.zip from https://doi.org/10.6084/m9.figshare.21789074
(figshare file 42602809) and unzip it first. Writes data/maps/koppen.json:
one character per cell, chr(48 + class) where class 0 = ocean and 1–30 follow
legend.txt; a 1° world grid and a 0.5° South-East Asia grid.
"""
import json, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CLASSES = ["", "Af", "Am", "Aw", "BWh", "BWk", "BSh", "BSk", "Csa", "Csb", "Csc", "Cwa", "Cwb", "Cwc", "Cfa", "Cfb", "Cfc",
           "Dsa", "Dsb", "Dsc", "Dsd", "Dwa", "Dwb", "Dwc", "Dwd", "Dfa", "Dfb", "Dfc", "Dfd", "ET", "EF"]


def pack(im, res, lon0, lon1, lat0, lat1):
    """Rows south→north, columns west→east, as one string."""
    cells = []
    for j in range(round((lat1 - lat0) / res)):
        lat = lat0 + (j + 0.5) * res
        y = int((90 - lat) / res)
        for i in range(round((lon1 - lon0) / res)):
            lon = lon0 + (i + 0.5) * res
            x = int((lon + 180) / res)
            cells.append(chr(48 + im.getpixel((x, y))))
    return "".join(cells)


def main():
    src = Path(sys.argv[1])
    world = Image.open(src / "1991_2020" / "koppen_geiger_1p0.tif")
    sea = Image.open(src / "1991_2020" / "koppen_geiger_0p5.tif")
    out = {
        "source": "Beck et al. (2023) Köppen–Geiger classification 1991–2020, Scientific Data 10, 724 (CC0)",
        "url": "https://doi.org/10.6084/m9.figshare.21789074", "fetched": "2026-10-02", "classes": CLASSES,
        "world": {"lon0": -180, "lat0": -60, "dlon": 1, "dlat": 1, "nx": 360, "ny": 140, "cells": pack(world, 1, -180, 180, -60, 80)},
        "seasia": {"lon0": 90, "lat0": -12, "dlon": 0.5, "dlat": 0.5, "nx": 80, "ny": 74, "cells": pack(sea, 0.5, 90, 130, -12, 25)},
    }
    p = ROOT / "data" / "maps" / "koppen.json"
    p.write_text(json.dumps(out, separators=(",", ":")))
    print(p.relative_to(ROOT), p.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()

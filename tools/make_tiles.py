"""Draw Khmer letter/word tiles as SVG with real glyph outlines.

Shapes text with uharfbuzz (correct Khmer subscript/vowel reordering), then
converts the resulting glyphs to SVG <path>s from Noto Sans Khmer, so a tile
renders identically everywhere — no font needed by the viewer.

Usage:  python tools/make_tiles.py tiles.json
tiles.json = [{"out": "l1/img/t-ka.svg", "text": "ក", "bg": "#F4E9D8", "fg": "#3A2B12"}, ...]
"""
import json
import os
import sys

import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(HERE, "fonts", "NotoSansKhmer-Regular.ttf")

_cache = {}


def _font():
    if "hb" not in _cache:
        blob = hb.Blob.from_file_path(FONT_PATH)
        face = hb.Face(blob)
        font = hb.Font(face)
        tt = TTFont(FONT_PATH)
        order = tt.getGlyphOrder()
        gset = tt.getGlyphSet()
        hhea = tt["hhea"]
        _cache["hb"] = (face, font)
        _cache["tt"] = (order, gset, hhea.ascender, hhea.descender)
    return _cache["hb"], _cache["tt"][0], _cache["tt"][1], _cache["tt"][2], _cache["tt"][3]


def tile_svg(text, bg="#F4E9D8", fg="#2B2118", pad_ratio=0.35):
    (face, font), order, gset, asc_m, desc_m = _font()
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    upem = face.upem

    paths = []
    x = y = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gid = info.codepoint
        if gid == 0:  # .notdef -> skip invisible boxes
            x += pos.x_advance
            continue
        pen = SVGPathPen(gset)
        gset[order[gid]].draw(pen)
        d = pen.getCommands()
        if d:
            tx = x + pos.x_offset
            ty = y + pos.y_offset
            paths.append(f'<path transform="translate({tx:.1f},{ty:.1f})" d="{d}"/>')
        x += pos.x_advance
        y += pos.y_advance

    asc = max(asc_m, upem * 0.9)   # Khmer upper signs ride high
    desc = min(desc_m, -upem * 0.5)  # subscripts ride low
    pad = (asc - desc) * pad_ratio * 0.5
    w = x + pad * 2
    h = asc - desc + pad * 2
    body = "".join(paths)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}">'
        f'<rect width="{w:.0f}" height="{h:.0f}" rx="{upem*0.12:.0f}" fill="{bg}"/>'
        f'<g transform="translate({pad:.1f},{asc + pad:.1f}) scale(1,-1)" fill="{fg}">{body}</g></svg>'
    )


def main(spec_path):
    with open(spec_path, encoding="utf-8") as f:
        tiles = json.load(f)
    made = 0
    for t in tiles:
        out = t["out"]
        if not os.path.isabs(out):
            out = os.path.join(HERE, "..", out)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        svg = tile_svg(t["text"], t.get("bg", "#F4E9D8"), t.get("fg", "#2B2118"))
        with open(out, "w", encoding="utf-8") as f:
            f.write(svg)
        made += 1
    print(f"wrote {made} tiles")


if __name__ == "__main__":
    main(sys.argv[1])

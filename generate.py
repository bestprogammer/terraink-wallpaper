"""
generate.py — Terraink Wallpaper Generator
Berechnet Abmessungen automatisch aus Bildschirmauflösung und PPI
"""
import argparse
from pathlib import Path
from terraink_py import PosterRequest, generate_poster

THEMES = [
    "midnight_blue",
    "noir",
    "blueprint",
    "neon_cyberpunk",
    "warm_beige",
    "pastel_dream",
    "japanese_ink",
    "emerald",
    "forest",
    "ocean",
    "terracotta",
    "sunset",
    "autumn",
    "copper_patina",
    "gradient_roads",
    "contrast_zones",
]

# PPI-Tabelle für gängige iPhone Modelle
# Schlüssel = logische Höhe in Punkten
IPHONE_PPI = {
    844: 460,   # iPhone 13, 13 Pro, 14, 15, 15 Pro
    932: 460,   # iPhone 13 Pro Max, 14 Plus, 15 Plus, 15 Pro Max
    812: 460,   # iPhone 12 mini, 13 mini
    926: 458,   # iPhone 12 Pro Max
    780: 476,   # iPhone 12, 12 Pro
    896: 326,   # iPhone 11, XR
    874: 460,   # iPhone 16 Pro
    956: 460,   # iPhone 16 Pro Max
    852: 460,   # iPhone 16, 16 Plus
}

def get_ppi(screen_height_pts: int) -> int:
    return IPHONE_PPI.get(screen_height_pts, 460)

def pts_to_cm(pts: int, scale: int, ppi: int) -> float:
    return round((pts * scale / ppi) * 2.54, 2)

def main():
    parser = argparse.ArgumentParser(description="Terraink Wallpaper Generator")
    parser.add_argument("--location",      type=str, required=True)
    parser.add_argument("--theme",         type=str, default="midnight_blue", choices=THEMES)
    parser.add_argument("--distance",      type=int, default=3000)
    parser.add_argument("--screen-width",  type=int, default=390)
    parser.add_argument("--screen-height", type=int, default=844)
    parser.add_argument("--scale",         type=int, default=3)
    parser.add_argument("--list-themes",   action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        print("Verfügbare Themes:")
        for t in THEMES:
            print(f"  {t}")
        return

    Path("output").mkdir(exist_ok=True)

    ppi = get_ppi(args.screen_height)
    width_cm  = pts_to_cm(args.screen_width,  args.scale, ppi)
    height_cm = pts_to_cm(args.screen_height, args.scale, ppi)

    print(f"Generiere: {args.location} | Theme: {args.theme} | Radius: {args.distance}m")
    print(f"Bildschirm: {args.screen_width}x{args.screen_height}pt @ {ppi}ppi → {width_cm}x{height_cm}cm")

    result = generate_poster(
        PosterRequest(
            output=Path("output/wallpaper"),
            formats=("png",),
            location=args.location,
            title=args.location.split(",")[1].strip() if "," in args.location else args.location,
            subtitle="",
            theme=args.theme,
            width_cm=width_cm,
            height_cm=height_cm,
            distance_m=args.distance,
            include_buildings=True,
        )
    )
    print(f"Gespeichert: {result.files}")

if __name__ == "__main__":
    main()

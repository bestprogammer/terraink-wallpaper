"""
generate.py — Terraink Wallpaper Generator
Optimiert für iPhone 13 (2532x1170px, 460ppi)
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

def main():
    parser = argparse.ArgumentParser(description="Terraink Wallpaper Generator")
    parser.add_argument("--lat",         type=float, required=True)
    parser.add_argument("--lon",         type=float, required=True)
    parser.add_argument("--city",        type=str,   default="My Location")
    parser.add_argument("--theme",       type=str,   default="midnight_blue", choices=THEMES)
    parser.add_argument("--distance",    type=int,   default=3000)
    parser.add_argument("--list-themes", action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        print("Verfügbare Themes:")
        for t in THEMES:
            print(f"  {t}")
        return

    Path("output").mkdir(exist_ok=True)

    print(f"Generiere: {args.city} ({args.lat}, {args.lon}) | Theme: {args.theme} | Radius: {args.distance}m")

    result = generate_poster(
        PosterRequest(
            output=Path("output/wallpaper"),
            formats=("png",),
            lat=args.lat,
            lon=args.lon,
            title=args.city,
            subtitle="",
            theme=args.theme,
            width_cm=9.91,   # iPhone 13: 2532x1170px @ 460ppi
            height_cm=21.44, # Seitenverhältnis 19.5:9
            distance_m=args.distance,
            include_buildings=True,
        )
    )
    print(f"Gespeichert: {result.files}")

if __name__ == "__main__":
    main()

"""
generate.py — Terraink Wallpaper Generator
Optimiert für iPhone 13 (2532x1170px, 460ppi)
Nutzt Adresstext statt Koordinaten — terraink_py löst via Nominatim auf
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
    parser.add_argument("--location",    type=str,   required=True,            help="Adresse oder Stadtname")
    parser.add_argument("--theme",       type=str,   default="midnight_blue",  choices=THEMES)
    parser.add_argument("--distance",    type=int,   default=3000)
    parser.add_argument("--list-themes", action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        print("Verfügbare Themes:")
        for t in THEMES:
            print(f"  {t}")
        return

    Path("output").mkdir(exist_ok=True)

    print(f"Generiere: {args.location} | Theme: {args.theme} | Radius: {args.distance}m")

    result = generate_poster(
        PosterRequest(
            output=Path("output/wallpaper"),
            formats=("png",),
            location=args.location,
            title=args.location.split(",")[1].strip() if "," in args.location else args.location,
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

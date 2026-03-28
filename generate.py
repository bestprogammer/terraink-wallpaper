"""
generate.py — Terraink Wallpaper Generator
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

PPI = 460

def px_to_cm(px: int) -> float:
    return round((px / PPI) * 2.54, 2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--location",    type=str, required=True)
    parser.add_argument("--theme",       type=str, default="midnight_blue", choices=THEMES)
    parser.add_argument("--distance",    type=int, default=3000)
    parser.add_argument("--width-px",    type=int, default=1170)
    parser.add_argument("--height-px",   type=int, default=2532)
    parser.add_argument("--list-themes", action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        for t in THEMES:
            print(t)
        return

    Path("output").mkdir(exist_ok=True)

    width_cm  = px_to_cm(args.width_px)
    height_cm = px_to_cm(args.height_px)

    print(f"Generiere: {args.location} | {args.theme} | {args.width_px}x{args.height_px}px → {width_cm}x{height_cm}cm")

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

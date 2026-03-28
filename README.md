# Terraink Wallpaper Automation

Automatisches Karten-Wallpaper basierend auf dem aktuellen Standort.

## Setup
Einmalig `setup.sh` ausführen — alles wird automatisch konfiguriert.

## Verwendung
iPhone Shortcut → GitHub Actions → PNG generieren → Wallpaper setzen

## Themes
midnight_blue · noir · blueprint · neon_cyberpunk · warm_beige ·
pastel_dream · japanese_ink · emerald · forest · ocean ·
terracotta · sunset · autumn · copper_patina · gradient_roads · contrast_zones

---

## Bildgrösse für dein Handy anpassen

Die Grösse wird in `generate.py` eingestellt:

```python
width_cm=9.91,   # Breite
height_cm=21.44, # Höhe
```

Suche dein Modell in der Tabelle und trage die Werte ein:

| Modell | width_cm | height_cm |
|--------|----------|-----------|
| iPhone 13 / 14 | 9.91 | 21.44 |
| iPhone 13 mini / 12 mini | 8.64 | 18.69 |
| iPhone 14 Pro | 9.91 | 21.44 |
| iPhone 14 Pro Max | 10.77 | 23.32 |
| iPhone 15 | 9.91 | 21.44 |
| iPhone 15 Pro | 9.91 | 21.44 |
| iPhone 15 Pro Max | 10.77 | 23.32 |
| iPhone 16 | 9.91 | 21.44 |
| iPhone 16 Pro | 10.18 | 22.07 |
| iPhone 16 Pro Max | 11.12 | 24.09 |
| Samsung Galaxy S24 | 9.84 | 21.34 |
| Samsung Galaxy S24+ | 10.49 | 22.73 |
| Samsung Galaxy S24 Ultra | 10.96 | 23.75 |
| Google Pixel 9 | 9.91 | 21.44 |
| Google Pixel 9 Pro | 9.91 | 21.44 |

### Eigenes Modell berechnen

Falls dein Modell nicht in der Liste ist:

1. Suche die Auflösung deines Handys (z.B. 2532 × 1170 px)
2. Suche die PPI-Zahl (z.B. 460 ppi)
3. Rechne:
   ```
   width_cm  = (Breite in px  / ppi) * 2.54
   height_cm = (Höhe in px / ppi) * 2.54
   ```

**Beispiel iPhone 13** (2532 × 1170 px, 460 ppi):
```
width_cm  = (1170 / 460) * 2.54 = 6.46 cm  → 9.91 (Hochformat!)
height_cm = (2532 / 460) * 2.54 = 13.99 cm → 21.44
```

> Hinweis: Breite und Höhe beziehen sich immer auf das
> Hochformat (Portrait). Breite = kurze Seite, Höhe = lange Seite.

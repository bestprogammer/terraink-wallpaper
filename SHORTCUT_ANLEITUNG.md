# Apple Shortcut: Terraink Wallpaper

## Aktionen in dieser Reihenfolge

### 1 — Standort
```
„Aktuellen Standort abrufen"
→ Variable: MeinStandort
```

### 2 — Koordinaten & Stadt
```
„Details des Standorts abrufen" → Breitengrad  → Variable: Lat
„Details des Standorts abrufen" → Längengrad   → Variable: Lon
„Details des Standorts abrufen" → Ort          → Variable: Stadt
```

### 3 — Theme wählen
```
„Aus Liste auswählen"
Elemente:
  midnight_blue
  noir
  blueprint
  neon_cyberpunk
  warm_beige
  pastel_dream
  japanese_ink
  emerald
  forest
  ocean
  terracotta
  sunset
  autumn
  copper_patina
  gradient_roads
  contrast_zones
Eingabeaufforderung: Karten-Theme
→ Variable: ThemeName
```

### 4 — Radius wählen
```
„Aus Liste auswählen"
Elemente:
  1000
  2000
  3000
  5000
  10000
Eingabeaufforderung: Kartenradius in Metern
→ Variable: Radius
```

### 5 — GitHub Actions auslösen
```
„Inhalt der URL abrufen"
URL:     https://api.github.com/repos/DEIN-USERNAME/terraink-wallpaper/actions/workflows/generate-wallpaper.yml/dispatches
Methode: POST
Header:
  Accept               → application/vnd.github+json
  Authorization        → Bearer DEIN_TOKEN
  X-GitHub-Api-Version → 2022-11-28
Body (JSON):
  ref      → main
  inputs   →
    latitude   → [Lat]
    longitude  → [Lon]
    city       → [Stadt]
    theme      → [ThemeName]
    distance   → [Radius]
```

### 6 — Warten
```
„Warten" → 70 Sekunden
```

### 7 — Cache-Buster Timestamp
```
„Aktuelles Datum" → Format: Unix-Zeitstempel
→ Variable: Timestamp
```

### 8 — Bild herunterladen
```
„Inhalt der URL abrufen"
URL: https://raw.githubusercontent.com/DEIN-USERNAME/terraink-wallpaper/main/wallpaper/current.png?t=[Timestamp]
Methode: GET
```

### 9 — Wallpaper setzen
```
„Hintergrundbild festlegen"
Bild:      Ergebnis von Schritt 8
Bildschirm: Sperrbildschirm und Home-Bildschirm
```

---

## Theme-Übersicht

| Theme | Stil |
|-------|------|
| midnight_blue | Dunkelblau, goldene Straßen |
| noir | Schwarz, weiße Straßen |
| blueprint | Blaupauspaper, technisch |
| neon_cyberpunk | Dunkel, pink/cyan Neon |
| warm_beige | Vintage Sepia |
| pastel_dream | Weiche Pastelle |
| japanese_ink | Minimalistisch, Tusche |
| emerald | Dunkles Grün |
| forest | Tiefdunkelgrün, Salbei |
| ocean | Blau/Türkis |
| terracotta | Mediterranes Warmrot |
| sunset | Orange/Pink |
| autumn | Herbstliches Orange/Rot |
| copper_patina | Oxidiertes Kupfer |
| gradient_roads | Farbverlauf-Straßen |
| contrast_zones | Hoher Kontrast |

---

## Stündliche Automation

Shortcuts App → Automation → + → Zeitplan → Täglich → Stündlich
→ Shortcut auswählen → „Vor dem Ausführen fragen" deaktivieren

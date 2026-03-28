# Apple Shortcut: Terraink Wallpaper

## Aktionen in dieser Reihenfolge

### 1 — Standort holen
```
Suchen: „Standort"
→ „Aktuellen Ort abrufen"
→ Variable: MeinStandort
```

### 2 — Adressdetails extrahieren
```
Suchen: „Details"
→ „Details von Ort abrufen"
  Attribut: Straße    → Variable: Strasse
  
(gleiche Aktion nochmal)
  Attribut: Ort       → Variable: Ort

(gleiche Aktion nochmal)
  Attribut: Region    → Variable: Region
```

### 3 — Adresse zusammensetzen
```
Suchen: „Text"
→ „Text"
  Inhalt: [Strasse], [Ort], [Region]
→ Variable: Adresse
```

### 4 — Theme wählen
```
Suchen: „Liste"
→ „Aus Liste auswählen"
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

### 5 — Radius wählen
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

### 6 — GitHub Actions auslösen
```
Suchen: „URL"
→ „Inhalt der URL abrufen"
  URL:     https://api.github.com/repos/bestprogammer/terraink-wallpaper/actions/workflows/generate-wallpaper.yml/dispatches
  Methode: POST
  Header:
    Accept               → application/vnd.github+json
    Authorization        → Bearer DEIN_TOKEN
    X-GitHub-Api-Version → 2022-11-28
  Body (JSON):
    ref      → main
    inputs   →
      location  → [Adresse]
      theme     → [ThemeName]
      distance  → [Radius]
```

### 7 — Warten
```
„Warten" → 70 Sekunden
```

### 8 — Cache-Buster Timestamp
```
Suchen: „Datum"
→ „Aktuelles Datum"
  Format: Unix-Zeitstempel
→ Variable: Timestamp
```

### 9 — Bild herunterladen
```
„Inhalt der URL abrufen"
  URL: https://raw.githubusercontent.com/bestprogammer/terraink-wallpaper/main/wallpaper/current.png?t=[Timestamp]
  Methode: GET
```

### 10 — Wallpaper setzen
```
Suchen: „Hintergrund"
→ „Hintergrundbild festlegen"
  Bild:       Ergebnis von Schritt 9
  Bildschirm: Sperrbildschirm und Home-Bildschirm
```

---

## Stündliche Automation

Shortcuts App → Automation → + → Zeitplan → Täglich → Stündlich
→ Shortcut auswählen → „Vor dem Ausführen fragen" deaktivieren ✅

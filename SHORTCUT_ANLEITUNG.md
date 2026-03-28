# Apple Shortcut: Terraink Wallpaper

## Einmalige Einrichtung — Token eintragen

1. Shortcut öffnen → Aktion „Inhalt der URL abrufen" (POST)
2. Bei Header Authorization: Bearer DEIN_TOKEN
3. Einmalig speichern — danach nie wieder nötig

## Token erneuern falls abgelaufen

1. github.com → Settings → Developer settings → Tokens (classic)
2. Alten löschen → Generate new token
3. Scopes: ✅ repo  ✅ workflow  ✅ read:org
4. Shortcut → Authorization → neuen Token eintragen

---

## Aktionen in dieser Reihenfolge

### 1 — Standort holen
Suchen: „Standort"
→ „Aktuellen Ort abrufen"
→ Variable: MeinStandort

### 2 — Adresse extrahieren
Suchen: „Details"
→ „Details von Ort abrufen"
  Attribut: Straße   → Variable: Strasse
(gleiche Aktion nochmal)
  Attribut: Ort      → Variable: Ort
(gleiche Aktion nochmal)
  Attribut: Region   → Variable: Region

### 3 — Adresse zusammensetzen
Suchen: „Text"
→ „Text"
  Inhalt: [Strasse], [Ort], [Region]
→ Variable: Adresse

### 4 — Theme wählen
Suchen: „Liste"
→ „Aus Liste auswählen"
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
→ Variable: ThemeName

### 5 — Radius wählen
„Aus Liste auswählen"
  1000
  2000
  3000
  5000
  10000
→ Variable: Radius

### 6 — GitHub Actions auslösen
Suchen: „URL"
→ „Inhalt der URL abrufen"
  URL: https://api.github.com/repos/bestprogammer/terraink-wallpaper/actions/workflows/generate-wallpaper.yml/dispatches
  Methode: POST
  Header:
    Accept               → application/vnd.github+json
    Authorization        → Bearer DEIN_TOKEN
    X-GitHub-Api-Version → 2022-11-28
  Body (JSON):
    ref      → main
    inputs   → (Wörterbuch)
      location  → [Adresse]
      theme     → [ThemeName]
      distance  → [Radius]
      width_px  → 1170
      height_px → 2532

### 7 — Warten
„Warten" → 70 Sekunden

### 8 — Timestamp
„Aktuelles Datum"
„Sekunden zwischen 1 Januar 1970 und Datum"
→ Variable: Timestamp

### 9 — Bild herunterladen
„Inhalt der URL abrufen"
  URL: https://raw.githubusercontent.com/bestprogammer/terraink-wallpaper/main/wallpaper/current.png?t=[Timestamp]
  Methode: GET

### 10 — Wallpaper setzen
„Hintergrundbild festlegen"
  Bild: Ergebnis von Schritt 9
  Bildschirm: Sperrbildschirm und Home-Bildschirm

---

## Stündliche Automation
Shortcuts App → Automation → + → Zeitplan → Stündlich
→ Shortcut auswählen → „Vor dem Ausführen fragen" deaktivieren ✅

---

## Auflösungen (von terraink.app)

| Modell | width_px | height_px |
|--------|----------|-----------|
| iPhone 13 / 14 | 1170 | 2532 |
| iPhone 14 Pro / 15 / 15 Pro | 1179 | 2556 |
| iPhone 14 Pro Max / 15 Plus / 15 Pro Max | 1290 | 2796 |
| iPhone 16 / 16 Plus | 1179 | 2556 |
| iPhone 16 Pro | 1206 | 2622 |
| iPhone 16 Pro Max | 1320 | 2868 |
| Samsung S24 Ultra | 1440 | 3120 |

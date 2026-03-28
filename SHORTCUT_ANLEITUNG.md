# Apple Shortcut: Terraink Wallpaper

## Einmalige Einrichtung

Beim ersten Mal musst du deinen GitHub Token eintragen:

1. Shortcut öffnen → Aktion **„Inhalt der URL abrufen"** (der POST zu GitHub)
2. Bei Header **Authorization** → Wert:
   ```
   Bearer DEIN_TOKEN_HIER
   ```
   Ersetze `DEIN_TOKEN_HIER` mit deinem echten Token z.B.:
   ```
   Bearer ghp_17B5W7ACEEbflrSwIEFzWji0kntV2I4eRM9j
   ```
3. Einmalig speichern — danach nie wieder nötig

---

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

### 4 — Bildschirmgrösse holen
```
Suchen: „Gerätedetails"
→ „Gerätedetails abrufen"
  Attribut: Bildschirmbreite
→ Variable: ScreenBreite

(gleiche Aktion nochmal)
  Attribut: Bildschirmhöhe
→ Variable: ScreenHoehe
```

### 5 — Theme wählen
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

### 6 — Radius wählen
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

### 7 — GitHub Actions auslösen
```
Suchen: „URL"
→ „Inhalt der URL abrufen"
  URL: https://api.github.com/repos/bestprogammer/terraink-wallpaper/actions/workflows/generate-wallpaper.yml/dispatches
  Methode: POST
  Header:
    Accept               → application/vnd.github+json
    Authorization        → Bearer DEIN_TOKEN_HIER
    X-GitHub-Api-Version → 2022-11-28
  Body (JSON):
    ref           → main
    inputs        → (Wörterbuch)
      location      → [Adresse]
      theme         → [ThemeName]
      distance      → [Radius]
      screen_width  → [ScreenBreite]
      screen_height → [ScreenHoehe]
      scale         → 3
```

### 8 — Warten
```
„Warten" → 70 Sekunden
```

### 9 — Timestamp
```
„Aktuelles Datum"
→ „Sekunden zwischen 1 Januar 1970 und Datum"
→ Variable: Timestamp
```

### 10 — Bild herunterladen
```
„Inhalt der URL abrufen"
  URL: https://raw.githubusercontent.com/bestprogammer/terraink-wallpaper/main/wallpaper/current.png?t=[Timestamp]
  Methode: GET
```

### 11 — Wallpaper setzen
```
Suchen: „Hintergrund"
→ „Hintergrundbild festlegen"
  Bild:       Ergebnis von Schritt 10
  Bildschirm: Sperrbildschirm und Home-Bildschirm
```

---

## Stündliche Automation
Shortcuts App → Automation → + → Zeitplan → Täglich → Stündlich
→ Shortcut auswählen → „Vor dem Ausführen fragen" deaktivieren ✅

---

## Token erneuern

Falls der Token abläuft oder ungültig wird:

1. github.com → Profilbild → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Alten Token löschen → Generate new token (classic)
4. Scopes: ✅ repo  ✅ workflow  ✅ read:org
5. Token kopieren
6. Shortcut öffnen → Aktion „Inhalt der URL abrufen"
7. Bei Authorization: `Bearer NEUER_TOKEN`

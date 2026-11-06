# Rezepte

Unsere Rezeptsammlung als lesbare Textdateien (Markdown). Eine Datei pro Rezept, sortiert nach Kategorien. Die Seite liegt auf GitHub Pages und lässt sich auf iPhone und Android als App zum Home-Bildschirm hinzufügen.

## Neues Rezept anlegen

1. `vorlage.md` kopieren und in den passenden Ordner legen, z. B. `rezepte/kochen/currys/thai-curry.md`.
2. Kopfdaten ausfüllen (Titel, Tags, Portionen, Zeit) und Zutaten und Schritte schreiben.
3. Index neu erzeugen: `python3 build_index.py`. Das schreibt `rezepte/index.json`, die die Seite liest.

## Kategorien

Backen: Brot · Semmeln & Brötchen · Kuchen & Torten · Kleingebäck & Kekse · Herzhaftes · Grundrezepte

Kochen: Currys · Eintöpfe · Suppen · Nudeln · Aufläufe · Pfannengerichte · Salate & Beilagen · Saucen & Dips

Namen und Reihenfolge stehen in `rezepte/kategorien.json`. Quer liegende Merkmale (vegan, schnell, kindertauglich …) stehen als `tags` im Kopf jedes Rezepts.

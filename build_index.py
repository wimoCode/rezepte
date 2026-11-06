#!/usr/bin/env python3
"""Erzeugt rezepte/index.json aus allen .md-Dateien unter rezepte/.

Aufruf (im Repo-Ordner):  python3 build_index.py
Die Kategorien und ihre Reihenfolge stehen in rezepte/kategorien.json.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
REZEPTE = ROOT / "rezepte"


def kopfdaten(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    daten = {}
    if not m:
        return daten
    for zeile in m.group(1).splitlines():
        if ":" not in zeile:
            continue
        key, _, wert = zeile.partition(":")
        wert = wert.strip()
        if wert.startswith("[") and wert.endswith("]"):
            daten[key.strip()] = [t.strip() for t in wert[1:-1].split(",") if t.strip()]
        else:
            daten[key.strip()] = wert
    return daten


def schoen(slug):
    return slug.replace("-", " ").capitalize()


def main():
    kat = json.loads((REZEPTE / "kategorien.json").read_text(encoding="utf-8"))
    rezepte = []
    for datei in sorted(REZEPTE.rglob("*.md")):
        teile = datei.relative_to(REZEPTE).parts
        if len(teile) < 3:
            continue
        haupt, unter = teile[0], teile[1]
        d = kopfdaten(datei.read_text(encoding="utf-8"))
        rezepte.append({
            "id": "/".join(teile)[:-3],
            "pfad": "rezepte/" + "/".join(teile),
            "titel": d.get("titel") or schoen(datei.stem),
            "untertitel": d.get("untertitel", ""),
            "kategorie": f"{haupt}/{unter}",
            "tags": d.get("tags", []),
            "portionen": d.get("portionen", ""),
            "zeit_gesamt": d.get("zeit_gesamt", ""),
        })
        kat.setdefault(haupt, {"label": schoen(haupt), "unter": {}})
        kat[haupt]["unter"].setdefault(unter, schoen(unter))

    kategorien = [
        {
            "id": hid,
            "label": h["label"],
            "unter": [{"id": uid, "label": ul} for uid, ul in h["unter"].items()],
        }
        for hid, h in kat.items()
    ]
    rezepte.sort(key=lambda r: r["titel"].lower())
    (REZEPTE / "index.json").write_text(
        json.dumps({"kategorien": kategorien, "rezepte": rezepte}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(f"{len(rezepte)} Rezepte in rezepte/index.json")


if __name__ == "__main__":
    main()

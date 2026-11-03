#!/usr/bin/env python3
"""Génère epg.xml : guide XMLTV des chaînes de démonstration de demo.m3u.

Couvre la veille (1 jour passé) et les 7 jours à venir, en UTC. Les programmes sont fictifs
et identiques d'un jour à l'autre pour une même heure (pas de hasard : le fichier ne change
que lorsque la date change). Bibliothèque standard de Python seulement.

Usage : python3 outils/generer_epg.py [fichier]   (par défaut : epg.xml)
"""
import sys
from datetime import datetime, timedelta, timezone
from xml.sax.saxutils import escape

PASSE_JOURS = 1
FUTUR_JOURS = 7

# (tvg-id, nom affiché, programmes en rotation : (durée en minutes, titre anglais, titre français, catégorie))
CHAINES = [
    ("demo1.ultime", "Démo 1", [
        (30, "BipBop Test Pattern", "Mire BipBop", "Documentary"),
        (60, "Demo Loop: Colours and Tones", "Boucle de démo : couleurs et sons", "Documentary"),
        (30, "Streaming Test Card", "Mire de diffusion", "Documentary"),
    ]),
    ("demo2.ultime", "Démo 2", [
        (60, "Advanced Stream Demo", "Démo du flux avancé", "Documentary"),
        (30, "Frame Rate Check", "Contrôle de la cadence", "Documentary"),
    ]),
    ("demo3.ultime", "Démo 3", [
        (45, "Demo Evening", "Soirée de démo", "Entertainment"),
        (45, "Test Pattern Magazine", "Le magazine de la mire", "Entertainment"),
        (30, "Late Demo", "Démo de fin de soirée", "Entertainment"),
    ]),
    ("demo4.ultime", "Démo 4", [
        (30, "Classic BipBop", "BipBop classique", "Documentary"),
        (30, "Quality Ladder", "L'échelle des qualités", "Documentary"),
    ]),
]

DESC_EN = "Fictional programme for the Ulti demo playlist. Video: Apple HLS test stream."
DESC_FR = "Programme fictif de la liste de démonstration d'Ulti. Vidéo : flux de test HLS d'Apple."


def fmt(d: datetime) -> str:
    return d.strftime("%Y%m%d%H%M%S +0000")


def generer(maintenant: datetime) -> str:
    debut = (maintenant - timedelta(days=PASSE_JOURS)).replace(hour=0, minute=0, second=0, microsecond=0)
    fin = debut + timedelta(days=PASSE_JOURS + FUTUR_JOURS + 1)
    lignes = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE tv SYSTEM "xmltv.dtd">',
        '<tv generator-info-name="ultime-iptv-demo" '
        'generator-info-url="https://github.com/Yoannf57/ultime-iptv-demo">',
    ]
    for cid, nom, _ in CHAINES:
        numero = cid[4]
        lignes += [
            f'  <channel id="{cid}">',
            f'    <display-name>{escape(nom)}</display-name>',
            f'    <icon src="https://yoannf57.github.io/ultime-iptv-demo/logos/demo{numero}.png"/>',
            "  </channel>",
        ]
    for cid, _, rotation in CHAINES:
        # Rotation recalée sur minuit UTC chaque jour : même grille d'un jour à l'autre.
        jour = debut
        while jour < fin:
            t = jour
            i = 0
            lendemain = jour + timedelta(days=1)
            while t < lendemain:
                duree, en, fr, categorie = rotation[i % len(rotation)]
                stop = min(t + timedelta(minutes=duree), lendemain)
                lignes += [
                    f'  <programme start="{fmt(t)}" stop="{fmt(stop)}" channel="{cid}">',
                    f'    <title lang="en">{escape(en)}</title>',
                    f'    <title lang="fr">{escape(fr)}</title>',
                    f'    <desc lang="en">{escape(DESC_EN)}</desc>',
                    f'    <desc lang="fr">{escape(DESC_FR)}</desc>',
                    f'    <category lang="en">{escape(categorie)}</category>',
                    "  </programme>",
                ]
                t = stop
                i += 1
            jour = lendemain
    lignes.append("</tv>")
    return "\n".join(lignes) + "\n"


if __name__ == "__main__":
    chemin = sys.argv[1] if len(sys.argv) > 1 else "epg.xml"
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(generer(datetime.now(timezone.utc)))
    print(f"{chemin} écrit ({PASSE_JOURS} jour passé, {FUTUR_JOURS} jours à venir)")

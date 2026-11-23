#!/usr/bin/env python3
"""Ajoute les balises de partage (Open Graph, Twitter) à la version publique de Tinan.

Usage : python3 ajouter_partage.py github/index.html

Le script insère le bloc juste après <title>. Il est idempotent : un bloc déjà
présent (entre les deux commentaires repères) est remplacé, jamais dupliqué.
L'image og-image.png doit se trouver à la racine du dépôt publié.
"""
import re
import sys

URL = "https://merry-goblin.github.io/tinan-lenavi/"
TITRE = "Tinan leNa'vi"
DESCRIPTION = (
    "Practise Na'vi, the language of the Avatar films, in 14 lessons: spaced "
    "review, an error log that tracks your mistakes, sourced grammar sheets. "
    "Free, no account, in English and French."
)
ALT = ("Tinan leNa'vi: a Na'vi exercise on a phone, with the expected answer "
       "and the rule explained after a mistake.")

DEBUT, FIN = "<!-- partage:debut -->", "<!-- partage:fin -->"


def attr(texte):
    return texte.replace("&", "&amp;").replace('"', "&quot;")


BLOC = f"""{DEBUT}
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{attr(TITRE)}">
<meta property="og:title" content="{attr(TITRE)} · Learn Na'vi">
<meta property="og:description" content="{attr(DESCRIPTION)}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}og-image.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{attr(ALT)}">
<meta property="og:locale" content="fr_FR">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{attr(TITRE)} · Learn Na'vi">
<meta name="twitter:description" content="{attr(DESCRIPTION)}">
<meta name="twitter:image" content="{URL}og-image.png">
<meta name="twitter:image:alt" content="{attr(ALT)}">
{FIN}"""


def ajouter(html):
    motif = re.compile(re.escape(DEBUT) + r".*?" + re.escape(FIN), re.S)
    if motif.search(html):
        return motif.sub(lambda _: BLOC, html, count=1)
    fin_titre = html.find("</title>")
    if fin_titre < 0:
        sys.exit("ajouter_partage : pas de <title> dans la page.")
    pos = fin_titre + len("</title>")
    return html[:pos] + "\n" + BLOC + html[pos:]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    chemin = sys.argv[1]
    with open(chemin, encoding="utf-8") as f:
        html = f.read()
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(ajouter(html))
    print(f"Balises de partage écrites dans {chemin}.")

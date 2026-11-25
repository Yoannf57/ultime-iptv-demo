# Liste d'essai (développement seulement)

Cette liste ne sert qu'aux essais d'Ulti sur les appareils de développement (« Ulti Essai »). Elle n'est pas la liste
de démonstration donnée aux magasins d'applications (`demo.m3u`, à la racine, inchangée).

Adresse : https://yoannf57.github.io/ultime-iptv-demo/essai/essai.m3u

| Chaîne | Flux | Cadence |
|---|---|---|
| Essai 50 | `essai/50/index.m3u8` (H.264 720p, AAC, MPEG-TS, boucle de 60 s sur 30 min) | 50 images par seconde |
| Essai 25 | `essai/25/index.m3u8` (même extrait) | 25 images par seconde |
| Essai 30 | BipBop 16:9 d'Apple (par lien) | 30 images par seconde |

Les deux premiers flux sont un extrait d'une minute de **Big Buck Bunny** (© 2008 Blender Foundation ·
www.bigbuckbunny.org, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)), réencodé à 50 et 25 images par
seconde pour essayer le réglage de la fréquence de l'écran. Fabrication : ffmpeg, à partir de la copie 720p de
video.blender.org (`-ss 60 -t 60 -vf fps=50`, H.264, segments de 6 s).

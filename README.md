# Ultime IPTV — liste de démonstration

Liste M3U **publique et 100 % légale** servant à tester l'app Ultime IPTV (par exemple pour la vérification
TestFlight d'Apple), sans abonnement IPTV.

- Liste : https://yoannf57.github.io/ultime-iptv-demo/demo.m3u
- Guide (XMLTV) : https://yoannf57.github.io/ultime-iptv-demo/epg.xml, régénéré chaque jour par une GitHub Action
  (`outils/generer_epg.py`, 1 jour passé et 7 jours à venir).
- Confidentialité : https://yoannf57.github.io/ultime-iptv-demo/confidentialite.html

Contenu : films ouverts de la Blender Foundation (Creative Commons), courts métrages *Caminandes* et flux de test HLS
publiés par Apple pour les développeurs. Aucune chaîne commerciale, aucun lien vers un fournisseur IPTV.
Sources, licences et attributions : [CREDITS.md](CREDITS.md).

Les chaînes « Démo 1 » à « Démo 4 » sont des flux de test d'Apple (vidéo à la demande) présentés comme des chaînes,
avec un guide fictif. Les épisodes de *Caminandes* se terminent par `#/series/…` : ce fragment n'est jamais envoyé
au serveur, il permet seulement à l'app de reconnaître un épisode de série.

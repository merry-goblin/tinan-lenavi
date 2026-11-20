# Tinan leNa'vi

Une app web pour s'entraîner au **Na'vi**, la langue créée par Paul Frommer pour les films *Avatar*. Elle est en français et pensée pour le téléphone.

Elle suit un parcours de 14 leçons, des sons de la langue jusqu'à la conversation :

- **Séance du jour** : cartes de vocabulaire, QCM, saisie et étiquettes à placer, avec révision espacée ;
- **Entraînement libre** par leçon, type d'exercice ou notion ;
- **Carnet d'erreurs** : chaque erreur est classée et revient jusqu'à être maîtrisée ;
- **Bilans de leçon**, **fiches** de grammaire et de vocabulaire, **lexique** ;
- **Export** des fiches et de la progression en Markdown.

Après une erreur, « Voir la règle » affiche la règle concernée, avec sa source.

## Ta progression

Rien n'est envoyé nulle part. La progression est enregistrée dans le navigateur, sur l'appareil utilisé. Elle n'est donc pas partagée entre deux appareils, et elle disparaît si tu effaces les données du site. On peut aussi l'effacer depuis les Réglages.

## Sources

Chaque règle de l'app indique sa source et sa date de vérification. Les références principales sont :

- [Horen Lì'fyayä leNa'vi](https://files.learnnavi.org/docs/horen-lenavi.pdf), la grammaire de référence de LearnNavi ;
- le [Concise Na'vi Dictionary](https://files.learnnavi.org/dicts/NaviPlainDictionary.pdf) de LearnNavi ;
- [Na'viteri](https://naviteri.org/), le blog de Paul Frommer.

En appui : [Kelutral](https://kelutral.org/), *[Na'vi in a Nutshell](https://files.learnnavi.org/docs/Navi_in_a_Nutshell.pdf)*, Wikipédia et Wikibooks. Les formes dérivées ont été contrôlées avec le conjugateur de [Reykunyu](https://reykunyu.lu/).

Le contenu a été préparé avec l'aide de Claude, qui n'a jamais servi de source.

Projet personnel d'apprentissage, sans lien avec les ayants droit d'*Avatar* ni avec LearnNavi.

## Pour la maintenance

`index.html` est généré, il ne se modifie pas à la main. Il réunit l'app Tinan, son contenu et une couche qui remplace les services de Claude dont se sert la version d'origine. La progression va dans le `localStorage` du navigateur, sous des clés `tinan/<chemin>`.

---
  title: 'Projet : CSS'
  author: qkzk
  weight: 23

---

pdf : [pour impression](./nsi_prem_projet_css.pdf)

# Mini projet CSS

![Margaret Hamilton](/docs/nsi/cours_premiere/ihm_web/projet_html_css/img/0.jpg)

## Objectif

L'objectif de ce mini projet est de réaliser **le style d'une page web.**

Vous disposez de **trois fichiers** :

- `margaret_hamilton.html` est la page web qu'il faut mettre en forme.

  _Il n'y a **rien à faire** dans ce document, **examinez en détail** les balises et classes._

- `style.css` est le style de la page web en question. Ce fichier contient
  des _selecteurs_ vides.

  _Votre travail est de les **remplir** avec les propriétés et attributs qui conviennent._

- `Margaret_Hamilton.pdf` est l'objectif final, converti en pdf.

  _Vous devez vous approcher le plus possible de ce résultat._

{{< hint danger >}}
- Le seul fichier à rendre est `style.css`. Rien d'autre.
- Si vous changez le contenu de `margaret_hamilton.html` alors je ne pourrais évaluer votre travail et vous perdrez des points.
{{< /hint >}}


### Liens vers ces fichiers :

1. [`margaret_hamilton.html`](https://raw.githubusercontent.com/qkzk/data_colab/master/margaret_hamilton.html)
2. [`style.css`](https://raw.githubusercontent.com/qkzk/data_colab/master/style.css)
3. [`Margaret_Hamilton.pdf`](https://github.com/qkzk/data_colab/raw/master/Margaret_Hamilton.pdf)

## Restitution du projet

- Vous rendrez un travail individuel
- Seul le fichier `style.css` est à rendre, les autres ne devant pas changer.
- Les autres modalités sont détaillées dans le travail donné.

## Quelques précisions

Démarche :

1. Enregistrer les trois fichiers dans un dossier `ihm_web/margaret_hamilton/` sur votre drive et localement.
1. Ouvrir les trois fichiers dans sublime text ou vs code. Vous pouvez utiliser autre chose mais je vous recommande un de ceux là.

   - sublime texte est moins efficace, il connaît les propriétés et complète les attributs mais ne les propose pas.
   - vs code fait le café.

1. Modifier le fichier `style.css` pour cela :

   - ouvrir le fichier HTML dans google _chrome_,
   - ouvrir les outils de développeur (F12) de chrome,
   - tester des modifications de style dans chrome,
   - copier ces modifications dans le fichier `style.css` une fois satisfait,
   - enregistrer le fichier et rafraîchir la page web (Maj + F5 pour forcer
     le rafraîchissement du style),
   - recommencer

Sauvegarder régulièrement, créez des versions, testez...

Essayez dans devTools _avant_ d'enregistrer, cela vous évitera des surprises.

Etant donné que j'ai _d'abord_ crée le style et ensuite converti, c'est
parfaitement faisable.

Mon fichier source fait 61 lignes. Pas 23456...

Attention, les attributs html sont loin d'être parfaits et manquent parfois de cohérence mais... lire le paragraphe suivant.

## Soin du détail

Vous êtes dans la peau d'un _intégrateur_ :

_"il met en page le document en accord avec la charte graphique et les règles_
_typographiques"_

- L'objectif est de _refaire_, pas d'apporter votre touche personnelle.
- Chaque détail compte : alignement, type de police, gras, souligné, italique,
  centrage, taille etc.

Tout n'est pas simple, certaines modifications demandent de l'astuce, n'y passez
pas la journée.

## Liste des propriétés CSS employées

Afin de vous éviter une galère trop conséquente, vous trouverez ici la liste
de toutes les propriétés CSS utilisées dans la correction, par ordre
alphabétique :

```css
border-bottom-color
border-bottom-style
color
display
font-family
font-size
font-style
line-height
margin-left
margin-right
padding-bottom
padding-top
text-align
text-decoration
width
```

Certaines sont employées plusieurs fois, selon l'élément ou la classe, avec
des attributs différents.

## Sources

- [MDN](https://developer.mozilla.org/fr/docs/Web/CSS/border-bottom-color)
  cherchez directement dans leur moteur après une propriété
- [W3 Schools](https://www.w3schools.com/cssref/pr_font_font-size.asp)
  même chose, cherchez directement, testez les exemples
- [google](https://google.com) : cherchez des méthodes précises
  "css centrer un élément"
- [premier résultat pour "css centrer un élément"](https://www.w3.org/Style/Examples/007/center.fr.html)

## Quelques mots sur le texte

Tiré d'un magasine publié en juillet 2019, il décrit le parcours
surprenant de Margaret Hamilton, une informaticienne de la NASA. Cela devrait
vous intéresser.

## Évaluation finale, objectifs

Je répète, l'objectif est de produire le même résultat, pas d'améliorer les documents fournis.
Vous ne touchez pas aux sources fournies, je n'utiliserai pas votre version modifiée de `margaret_hamilton.html`.

Afin d'évaluer votre travail je vais :

1. déplacer votre fichier `style.css` dans le dossier contenant `margaret_hamilton.html`.
2. ouvrir votre fichier dans un éditeur de texte et lire votre code. Lisibilité, organisation, soin du détail.
3. ouvrir `margaret_hamilton.html` dans chrome et comparer. Je n'évalue pas vraiment, c'est pour me faire une idée.
4. _"Imprimer"_... _"dans un pdf"_ ... et ouvrir ce pdf. C'est ce .pdf que je compare au document de référence `Margaret_Hamilton.pdf`. Et là je regarde tout tout tout.

**Et donc comment travailler ?**

Faîtes pareil.

1. déplacez les fichiers dans un même dossier.
2. **Faites une copie du fichier style.css d'origine**. Ça vous aidera. Conservez des versions intermédiaires aussi. Ça aide.
3. Ouvrez `style.css` avec un éditeur de texte comme sublime text, ouvrir aussi `margaret_hamilton.html`
4. Ouvrez le pdf avec chrome
5. modifiez `style.css`, enregistrer et rafraîchir `margaret_hamilton.html`
6. répétez jusqu'à obtenir un résultat satisfaisant
7. De temps en temps, exportez en pdf : "_Imprimer_, _dans un pdf_", comparer au pdf d'origine.
8. Quand vous êtes satisfait, nettoyez votre code. Vérifiez que ça fonctionne toujours.
9. Rendez le travail et attendez votre 20/20.

Dernière remarque : c'est parfaitement possible, c'est comme ça que j'ai crée le pdf.

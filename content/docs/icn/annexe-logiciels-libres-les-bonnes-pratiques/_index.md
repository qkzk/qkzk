---
author: qu3nt1n
date: 2016-07-08 14:09:56+00:00
draft: false
title: 'Annexe : Logiciels libres, les bonnes pratiques'
weight: 12

---

# Introduction


L'utilisation de logiciels et d'application est devenue un geste quotidien. Connaissez-vous leurs droits d'utilisation, de copie et d'édition ?

Savez-vous que vous pouvez contribuer à l'amélioration de nombreux logiciels ?

Qu'est ce qu'un logiciel libre ? Un logiciel propriétaire ?


# Logiciel libre, propriétaire, freeware (gratuiciel).


Citons la définition de [Wikipédia](https://fr.wikipedia.org/wiki/Logiciel_libre) d'un **logiciel libre** :



 	  0. _la liberté d'exécuter le programme, pour tous les usages ;_
 	  1. _la liberté d'étudier le fonctionnement du programme et de l'adapter à ses besoins ;_
 	  2. _la liberté de redistribuer des copies du programme (ce qui implique la possibilité aussi bien de donner que de vendre des copies) ;_
 	  3. _la liberté d'améliorer le programme et de distribuer ces améliorations au public, pour en faire profiter toute la communauté._

Un logiciel libre est donc un logiciel que vous pouvez utiliser comme bon vous semble une fois que vous l'avez acquis. Il est donc possible d'en étudier le code source et de l'adapter à vos besoins particuliers.

S'opposent à cette définition tous les logiciels dits **propriétaires** dont l'usage n'est pas libre et dont on ne peut généralement pas étudier le code source.

Une sous-catégorie apparaît : celles des logiciels propriétaires mais gratuits. Leur acquisition est gratuite mais vous ne pouvez en faire ce que vous voulez.


## Quelques exemples importants :




### Systèmes d'exploitation :


Le [système d'exploitation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation) est l'ensemble des programmes qui se situent entre le matériel et les programmes destinés à l'utilisateur. Ils en rendent l'usage de l'ordinateur possible et le contrôlent. Certains sont très épurés (mode texte, peu de fonctions) d'autres très chargés (environnement fenêtré, grande adaptabilité aux besoins courants). Le système d'exploitation permet aussi l'ajout de matériel sans devoir réécrire les programmes. Voici les plus courants :

**Windows** : propriétaire, développé par Microsoft. Son usage n'est que très rarement gratuit et repose généralement sur l'acquisition de licence. Nous reviendrons plus tard sur la pratique courante de certains utilisateurs qui contournent ces licences.

La conception de Windows remonte aux années 1970/1980 avec le rachat par Microsoft d'un système en pleine expansion à l'époque : DOS. Il est devenu MSDos. C'est l'invention par IBM du concept de PC (personnal computer) et de ses grands principes : rétrocompatibilité (votre .exe de 1980 fonctionne encore sur windows 10), interchangeabilité des composants (vous pouvez changer votre carte graphique ou votre ram sans trop de problème...) etc. qui a contribué à l'avènement de Microsoft. La grande erreur d'IBM fut de déléguer à Microsoft la conception d'un système d'exploitation grand public, préférant se concentrer sur les professionnels. Microsoft a rapidement équipé presque tous les PC grand public.

En 2016 Windows est toujours le premier système d'exploitation, équipant 90% des ordinateurs.

En théorie, Windows est rétrocompatible... dans la pratique c'est plus compliqué. Certains logiciels ne fonctionneront pas sur des versions trop récentes de windows. Inversement, certains logiciels demanderont une version plus récente de windows pour être mis à jour. Microsoft incite ainsi ses utilisateurs à acquérir de nouvelles licences.





Une grande catégorie de système d'exploitation respecte des règles assez strictes édictées dans les années 60 : «[ le type **Unix** ](https://fr.wikipedia.org/wiki/Type_Unix)».

_Le système **UNIX** est [multi-utilisateur](https://fr.wikipedia.org/wiki/Multi-utilisateur) et [multitâche](https://fr.wikipedia.org/wiki/Multit%C3%A2che), il a été construit pour être sûr, vis-à-vis des manipulations illicites des utilisateurs pour accéder à des données d'un autre utilisateur ou vis-à-vis des erreurs lors de l'exécution d'un programme. Il permet donc à un ordinateur mono ou multi-processeurs d'exécuter apparemment simultanément plusieurs programmes dans des zones protégées appartenant chacune à un utilisateur en minimisant tout risque de fraude ou d'incident. ([Wikipédia](https://fr.wikipedia.org/wiki/Type_Unix))_

De très nombreuses variantes d'Unix existent, on en distingue deux grandes catégories : **BSD** et **Linux**.

**BSD**, développé dans les années 1970 à Berkeley a visé la stabilité et la sécurité, **Linux** la facilité d'adaptation.** **Les variantes les plus connues sont :  NetBSD, OpenBSD, FreeBSD. Variantes du système BSD adaptées dédiés généralement aux serveurs et adaptés à certains besoins : NetBSD pour le réseau, OpenBSD pour la sécurité, FreeBSD pour la portabilité. Presque toutes les variantes de BSD sont des systèmes libres... sauf la plus connue : OS X.

**OS X** ( depuis peu **macOS**) : le système d'exploitation d'Apple présent sur tous les ordinateurs qu'ils vendent. C'est un système partiellement propriétaire fondé sur un noyau **BSD** et respectant toutes les propriétés d'UNIX. Les sources ne sont pas éditables, il n'est donc pas libre. Il est décliné en de nombreuses versions et rares sont les logiciels rétro compatibles. Ce qui signifie qu'il faut le mettre à jour (et c'est payant) pour continuer à mettre à jour ses logiciels !

**iOS** : le système d'exploitation propriétaire d'Apple présent sur les iPhones. Il n'est pas libre et est une déclinaison d'OS X

**GNU/Linux** (débian, ubuntu, mint, redhat, slackware, archlinux etc.) : Systèmes d'exploitation libre développés eux sur le noyau linux (son l'invention remonte aux années 90 par Linus Torvald). C'est l'archétype du système d'exploitation libre. On peut généralement tout faire avec les distributions proposées. Il est présent sur 90% des principaux serveurs web et autre et est totalement adaptable à tous les besoins : grand public, serveur devant économiser un maximum ses ressources, serveurs regroupant des centaines de machines etc. Linux ne propose à la base qu'un tout petit noyau de fonctionnalités très "low level" et peu utilisables. S'ajoutent alors d'autres logiciels pour former un systèmes d'exploitation complet : gestionnaire de périphérique, environnement graphique etc. C'est ce qu'on appelle une **distribution**.

Linux n'est pas difficile d'accès. Son inconvénient majeur à l'heure actuelle est le peu de jeux vidéos qu'il supporte et l'intégration native de certains matériels spécifiques. Rien n’empêche d'en faire la découverte - je vous le recommande - que ce soit sur une machine à part entière (un vieux pc oublié, un raspberry Pi) ou dans une **machine virtuelle** sous windows. On recommande souvent aux débutants d'attaquer par [Ubuntu](http://ubuntu-fr.org/). Je n'entrerai dans aucun débat avec d'éventuels "spécialistes" du sujet.

**Android : **_est un système d'exploitation mobile basé sur le noyau Linux et développé actuellement par Google. Le système a d'abord été conçu pour les smartphones et tablettes tactiles, puis s'est diversifié dans les objets connectés et ordinateurs comme les télévisions ([Android TV](https://fr.wikipedia.org/wiki/Android_TV)), les voitures ([Android Auto](https://fr.wikipedia.org/wiki/Android_Auto)), les ordinateurs (Android-x86) et les smartwatch ([Android Wear](https://fr.wikipedia.org/wiki/Android_Wear)). Le système a été lancé en juin 2007 à la suite du rachat par Google en 2005 de la startup du même nom. En 2015, **Android est le système d'exploitation le plus utilisé dans le monde avec plus de 80 % de parts de marché dans les smartphones.** [(Wikipédia)](https://fr.wikipedia.org/wiki/Android). _Android n'est donc pas un logiciel totalement libre.



On pourrait en citer d'autres, aux usages encore plus spécifiques ou qui ont marqué l'histoire (AmigaOS, Solaris SUN etc.). Certains systèmes devant respecter des conditions très sévères de stabilité et de sécurité tournent encore avec des systèmes développés dans les années 1960 ! C'est le cas, par exemple, de la gestion des [missiles nucléaires américains](http://www.slate.com/blogs/future_tense/2014/04/28/huge_floppy_disks_and_other_old_tech_is_common_at_air_force_nuclear_missile.html)... Pour les anglophobes la motivation est très simple : éviter les bugs et le piratage.




### Suites bureautiques


Les suites bureautiques cherchent à simplifier le travail "de bureau" : création de documents, calculs répétitifs, gestion de données en quantité modeste.


#### Suites bureautiques installées sur la machine :


La suite bureautique la plus connue est **Office**, développée par Microsoft. Son expansion coïncide avec le développement du PC dans les années 1980/1990 et l'arrivée dans les bureaux, les écoles puis les domiciles des ordinateurs. Office qui regroupe un traitement de texte (Word), un tableur (Excel), un diaporama (PowerPoint) mais aussi un système de base de données (Access) est donc couramment employé et fréquemment confondu avec le concept même de suite bureautique. C'est un système totalement propriétaire et payant, sans doute le logiciel le plus piraté au monde.

Microsoft propose toute une série de licences selon les usages (école cherchant à l'installer sur des centaines de machines, étudiants, enseignant, bureaux disposant d'un parc de milliers de machines, PME etc.). Les tarifs préférentiels ont pour objectif de fidéliser l'utilisateur et de l'inciter à réclamer Office à son entreprise une fois embauché... Ce qui lui coûtera très cher.

Depuis la fin des années 1990 deux grandes suites bureautiques sont apparues : **OpenOffice** et **LibreOffice**. Retenons simplement qu'elles ne formaient d'abord qu'une seule suite (OpenOffice). Les deux suites sont totalement libres et proposent sensiblement les mêmes fonctionnalités. Des différences existent mais l'utilisateur lambda ne les distinguera généralement pas.
Elles font aussi bien qu'Office (si, si) et sont gratuites... Aussi ?


#### Suites bureautique dans le cloud :


Depuis les années 2010, le développement du Cloud a bouleversé la donne et de nombreuses suites sont directement intégrées dans le Cloud. L'avantage est d’accéder partout sur internet à ses documents... l'inconvénient est de ne plus en être maître !

**Google Document** (celle que nous utilisons ici) est intégrée au cloud grand public de google : google drive. Il propose les mêmes outils sauf la gestion de base de donnée. C'est le précurseur et il est parfaitement intégré aux autres outils dans le cloud de Google : Calendar, Gmail, Keep (prises de notes), etc.

On citera aussi **Zoho**, **Office 365** (version d'office très allégée et intégrée au cloud de Microsoft), la gestion d'office par Dropbox etc.


### Les navigateurs web


**Chrome** : le navigateur web propriétaire de Google. Il est crée à partir du projet **Chromium** avec lequel il partage tout ou presque. Il tourne sur presque toutes les machines et est très régulièrement mis à jour. Il respecte tous les standards du web. C'est très important pour les web développeurs qui savent donc qu'à condition de respecter les standards, leur page s'affichera correctement sur Chrome.

Google a décidé en 2014 d'augmenter la sécurité de Chrome en bloquant certaines applications, en particulier java, qui ne peuvent plus s’exécuter dans le navigateur. C'est un problème mineur mais parfois gênant.

**Firefox : **déclinaison de Mozilla, il fut le premier adversaire historique d'internet explorer et le premier à renverser la domination de celui-ci. Il respecte lui aussi tous les standards du web et est très régulièrement mis à jour. C'est un logiciel libre et open source qui fonctionne sur toutes les plateformes.

**Internet Explorer** : installé avec windows il a longtemps dominé le marché et reste très employé, en particulier par les utilisateurs ne mettant pas à jour leur système. Les versions les plus anciennes telle IE6 posent énormément de problèmes aux développeurs web. Les versions actuelles sont moins pénibles et on peut considérer que Microsoft a refait son retard dans le domaine.

**Safari :** présent sur les machines apple (iphone et mac) il respecte tous les standards modernes.

**Chromium** et **Mozilla** : les deux projets à l'origine de Chrome et Firefox. Libres l'un comme l'autre ils développent toujours des navigateurs mais sont moins répandus.




### Les éditeurs de textes


A distinguer d'un traitement de texte, l'éditeur de texte vise principalement à noter quelques lignes sans se soucier d'un rendu particulier OU à créer et modifier du code. La liste est immense et presque chaque développeur a ses préférences ! La coloration syntaxique, les raccourcis claviers, la numérotation des lignes, les possibilités de recherche et d'éditions automatique font parties de fonctions de base de tout bon éditeur de texte. Il en existe des centaines.

Les systèmes sous **Unix **ayant les faveurs des développeurs c'est naturellement sur ces plateformes qu'on rencontre le plus d'éditeurs de texte. Par exemple :

**Vi** est l'archétype de l'éditeur Geek : ultra puissant, très difficile d'accès et dépourvu de gestion de la souris ! Tout se fait au clavier et on dispose de différents états permettant de manipuler le fichier en tant que tel (l’exécuter, le sauvegarder, le copier etc.) ou de l'éditer. Sa version moderne **Vim** propose 14000 extensions. Aussi surprenant que cela puisse paraître (souvenons-nous, pas de souris), Vim a un avantage immense : on peut programmer directement sur une machine distante sans télécharger/uploader les fichiers.

**nano** est un éditeur en mode texte très léger, beaucoup moins puissant que vi/vim mais très commode.

**Emacs** fait tout sauf le café. Les avantages sont immédiats : un seul logiciel, assez simple à première vue dont on est rarement contraint de sortir. Les inconvénients sont clairs : c'est vite une usine à gaz.

**Sublime Text** : Editeur graphique comportant de nombreux atouts (gestion des projets, grande souplesse des configurations, sélections/éditions multiple, esthétisme etc.). Sublime Text fonctionne sur toutes les plateformes ou presque. C'est un freeware.

Sous **Windows** on retiendra aussi **Notepad ++** pour sa simplicité et ses fonctionnalités qui est aussi un freeware.

Pour les passionnés j'en citerai trois qui fonctionnent sur le même principe que Sublime : **Atom **(développé directement par Github), **Brackets** (Adobe) et **VSCode **(Microsoft).

Et puisqu'on parle de goûts et couleurs, les miens :
**Atom** pour les gros projets, **Sublime** pour les fichiers énormes et le petit bordel (notes, todo list etc.), **Nano** pour éditer directement sur la machine distante.

Enfin, puisque c'est un sujet complexe.
Pour certains projets on est presque contraint d'employer certains éditeurs "augmentés". Ainsi pour développer une application android, on emploiera **Android Studio**. Il gère à la fois son développement, sa compilation et son fonctionnement sur la machine (virtuelle ou réelle). Il a aussi des fonctions étonnantes, comme celle de repérer qu'une variable n'a pas été déclarée ou qu'un paquet n'est pas installé. Par contre c'est l'archétype de l'usine à gaz.


### Le graphisme


L'informatique n'a pas simplifié que le travail du comptable et de la secrétaire. Il a aussi permis le développement des jeux vidéos et la prolifération de la publicité. Deux grands domaines qui usent et abusent du graphisme.

La suite graphique la plus utilisée dans le monde est celle d'adobe (**Adobe Creative Suite**) : Photoshop, Illustrator, InDesign, Acrobat, Dreamweaver etc.

Comme Microsoft, Adobe s'est développé dans les années 1980/1990 et s'est imposé comme l'éditeur le plus réputé et pendant très longtemps le seul ou presque.

Adobe (tout comme Microsoft) a longtemps eu une politique très laxiste vis à vis du piratage : licences chères et piratage facile. En laissant proliférer des versions craquées de ses logiciels, il s'est assuré que les apprentis pouvaient utiliser ses outils frauduleusement mais sans risque. En attaquant les entreprises qui n'achetaient pas de licence il s'est assuré de confortables revenus. Cette stratégie a parfaitement fonctionné : les apprentis maîtrisent Photoshop et demandent son installation une fois embauchés. Ils provoquent l'achat de nouvelles licences... La boucle est bouclée.

Avec l'arrivée du Cloud, adobe a changé son fusil d'épaule et a renforcé la sécurité de sa suite. Celle-ci est maintenant (plus) difficile à pirater mais disponible en abonnement à des prix plus accessibles.

Il n'existe pas encore d'autre suite aussi complète que celle proposée par Adobe mais des variantes pour chaque logiciels, citons-en quelques uns :

Citons toutefois **Affinity Designer** (~55€) qui rivalise - d'après mes amis graphistes - avec la suite Adobe... pour 10x moins cher.


#### Dessin


**Photoshop (Adobe)** : création et édition d'images bitmap (retouche photo). Le maître incontesté.

**Illustrator (Adobe) : **dessin vectoriel. A nouveau, il domine totalement.

**Gimp :** logiciel libre et open source remplissant sensiblement les mêmes fonctions que photoshop et illustrator.

**Inkscape :** logiciel libre dédié au dessin vectoriel.

**Photofiltre :** logiciel freeware permettant de faire de la retouche photo assez simple.


#### PDF


**Acrobat (Adobe) :** permet la création de PDF. Des documents lisibles sur toutes les machines et préformatés pour l'impression. A ne pas confondre avec **Acrobat Reader** qui ne permet que la LECTURE.

**PDFForge :** freeware permettant la création de PDF

**SumatraPDF :** logiciel libre permettant la LECTURE de PDF (beaucoup mieux qu'Acrobat Reader).

Un mot du professeur de mathématiques que je reste : de nombreux scientifiques créent leurs documents grâce à des éditeurs de texte dans le langage **Latex.** Ils les compilent directement en pdf. Le résultat est optimal, les formules sont parfaitement lisibles, les documents s'impriment partout et les sources sont éditables par tous. La difficulté d'accès est certaine mais le jeu en vaut la chandelle.




## Les enjeux du logiciels libre :


La question a longtemps été simple : grande maison d'édition vs logiciel libre.

Microsoft (et Adobe) ont longtemps affronté les développeurs souhaitant propager le logiciel libre. Leurs arguments étaient limpides : si le code source est connu, tout le monde peut le piller et le revendre (ce qu'ils ont fait à leur époque) et les maisons d'éditions vont mourir, n'ayant plus rien à vendre.

Le logiciel libre tire ses racines du développement d'Unix dans les années 60. D'abord propriétaire, Unix a permis l'apparition d'autres systèmes d'exploitation et donc d'autres logiciels, eux libres et gratuits. Depuis les années 2000 tout le monde peut installer linux ou bsd sur presque n'importe quelle machine et disposer d'un ordinateur totalement fonctionnel et libre. L'inconvénient est qu'il faut forcément se documenter.

Jusqu'aux années 2010 ces arguments n'ont pas évolué. L'arrivée du cloud et du développement dans celui-ci avec GIT a tout bouleversé. Tout le monde s'est mis à partager ses travaux, en totalité ou en partie. Microsoft a réussi le premier virage : celui du PC, dans les années 1980/1990 et raté le second, celui du smartphone et du retour en force de l'open source dans les années 2010.

**Mais pourquoi le libre ?** D'abord, il convient vraiment de distinguer un logiciel gratuit comme Notepad++ d'un logiciel libre comme Libreoffice. Si le premier est utilisable par chacun, le second est améliorable par chacun ! Je peux repérer un bug dans libreoffice et le corriger moi même (à condition d'en être capable). C'est impossible dans Notepad++, ses sources n'étant pas rendues publiques.

Est-ce un enjeu ? Oui totalement. En particulier pour rendre l'information accessible à tous et améliorer la sécurité.

L'accès à l'information est un critère déterminant pour le développement d'une société épanouie et libre. Si tous les logiciels sont payants et chers, certains marchés sont dans l'incapacité d'y accéder. Ce qui freine considérablement le développement de certaines nations. La politique chinoise visant à encourager la contrefaçon des logiciels s'est appuyée sur la difficulté d'accès et a, encore aujourd'hui, de sérieuses répercussions sur le marché du logiciel.

D'autre part le piratage informatique est simplifié par l'opacité des systèmes. De la géopolitique à la simple fraude à la carte bleue, les pirates informatiques ont devant eux un océan de possibilités. En rendant les sources libres on contribue à leur amélioration et donc, à la protection des systèmes en question.

Citons, par exemple Stuxnet, un virus informatique développé en 2010 par la NSA qui a détruit (physiquement) une grande partie des centrifugeuses d'enrichissement en Uranium installées en Iran. Voilà l'archétype de l'action d'un système totalement verrouillé (la NSA) contre un autre (le système gérant les centrales en Iran).


#### L'Open Source


L'open source va plus loin que le logiciel libre : le principe de l'open source est de systématiquement partager ses sources et **d'utiliser au maximum des outils pré existant** plutôt que de développer les siens. Ainsi on favorise l'échange et l'adaptation. Celui-ci étant amélioré par la simplicité avec laquelle on peut s'approprier un nouveau code, ne devant pas tout redécouvrir.


#### Le piratage, la sécurité informatique


Distinguons le simple pirate qui télécharge un logiciel ou un film du hacker qui tente de pénétrer un système (parfois pour le détruire, le piller ou le rançonner, parfois pour en améliorer la sécurité).

Le premier, le **simple pirate** que vous êtes peut-être, enfreint les lois concernant la propriété intellectuelle. Il spolie les auteurs en utilisant frauduleusement leurs créations. Ceux-ci sont alors privés d'un revenu. En n'acquittant pas ce qu'il doit, le pirate renforce les entreprises déjà établies (qui survivent déjà) contre celles qui cherchent à se développer. Le manque à gagner est difficile à quantifier (s'il était contrait de payer, le pirate le ferait-il ?) mais les conséquences sont bien réelles. Le "formatage" de la musique et du cinéma est la première conséquence. L'apparition des horribles Freemium (Candy crush et autres) est la suivante. Vous ne voulez pas payer ? Alors attendez 142 heures ou faîtes nous beaucoup de pub !

Le débat est vaste et les bonnes pratiques peu répandues. Il existe des moyens légaux d'accéder à l'information, aux loisirs et ils ne coûtent pas très cher. On peut télécharger légalement les jeux-videos, sans forcement les payer aussi cher que sur Steam ! On peut s'abonner à Spotify ou à Netflix et consommer légalement de la musique ou des films/séries.

Le **hacker **cherche à pénétrer un système, un réseau, une machine.

Le Script Kiddie emploie des outils préexistant sans forcement maîtriser les concepts. Ces programmes cherchent automatiquement des failles connues mais non corrigées.

Certains sont bien meilleurs et créent leurs propres logiciels et virus.

Enfin Les bons hackers cherchent à découvrir les failles des systèmes pour les corriger et améliorer leurs sécurités. La majorité des grandes entreprises rétribuent les hackers qui leur communiquent une faille.



Les enjeux de la sécurité informatique sont immenses et presque chaque nation dispose de ses propres pirates. Ils sont utilisés pour l'espionnage industriel, la sécurité des états mais aussi pour le sabotage à grande échelle des adversaires !

En ce qui concerne les utilisateurs que nous sommes, il convient d'adopter de saines pratiques : faire attention à ce qu'on fait et partage sur internet. Faire attention à ce qu'on télécharge. Nettoyer régulièrement ses machines (smartphones et ordinateurs) et sécuriser ses mots de passe.

Ces précautions élémentaires étant prises, on se penche ensuite sur les logiciels qu'on emploie.

Pourquoi renforcer un système globalement néfaste en piratant un logiciel cher et verrouillé plutôt que d'utiliser un logiciel libre et n'enfreindre aucune règle ? Si les jeux videos restent massivement développés pour les consoles et les PC windows, ce n'est plus le cas des autres outils qui existent tous en version libre.

**Comment trouver les logiciels gratuits mais moins connus** ? [AlternativeTo](http://alternativeto.net/software/adobe-photoshop/) vous propose des alternatives à tous les logiciels d'usage courant en vous précisant le type de licence.

A l'heure actuelle se prémunir du piratage revient aussi à se protéger contre l'emploi massif des données personnelles. Tout ce que vous faîtes sur internet est enregistré quelque part et nul ne sait si cela ne se retournera pas contre vous des années plus tard. L'exemple le plus connu est celui du directeur des ressources humaines qui fouille les réseaux sociaux à la recherche des candidats à l'embauche. Gare à ce que vous avez laissé traîné ! Mais la police utilise quotidiennement Facebook et les autres réseaux sociaux pour recouper les informations.

Enfin, en ce qui concerne les services en ligne (Gmail, Facebook, Twitter) l'adage bien connu est vrai : "_si c'est gratuit, c'est vous le produit."_


# Les services en ligne, le cloup et les apps


Là, c'est beaucoup plus clair. A moins que ce ne soit spécifié d'entrée, tout est propriétaire.

Ce qui signifie que que tout ce que vous y faites, tout ce que vous y enregistrez est sauvegardé quelque part sur un serveur. La moindre extension de chrome, la plus petite app de google play ou apple store est susceptible d'enregistrer vos donnée si vous la laissez faire. Elle vous demandera l'autorisation, c'est la loi, prenez le temps de le lire.

Facebook vous propose de récupérer l'intégralité de vos données, c'est aussi la loi. Il se garde par contre le droit de vendre vos données, anonymisées (mais votre nom n'a plus aucune importance, vous pouvez néanmoins être identifié) à des régies publicitaires et autres. C'est ainsi qu'il se paye sur votre dos.

Il existe des Clouds libres ([OwnCloud](https://owncloud.org/) par exemple) qui se soucient de la sécurité et de la vie privée de leurs utilisateurs. Leur usage est malheureusement peu répandu. Idem pour les réseaux sociaux, il en existe des libres... mais à nouveau, vous n'y retrouverez pas le beau Kerwann du club de foot ni la jolie Arantxa de l'abris bus. Libre à vous de leur faire découvrir (et bon courage).

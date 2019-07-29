
/*==  afficheMonument ==
Paramètres : 5
 nomMonument (chaine) : le nom du monument qui est écrit dans le titre
 longitude (flottant) : la longitude du centre de la carte affichée
 latitude  (flottant) : la latitude du centre de la carte affichée
 zoom (entier) : le facteur de zoom dela google map (entre 0 et 20 compris)
 taille (entier) : la taille d'affichage de l'image
Résultat : aucun
Effet de bord : affiche dans la page une section avec pour titre nomMonument et une image "gogle map" de la taille fournie, centrée sur la longitude et latitude indiquée, avec le zoom demandé.

*/
var afficheMonument = function(nomMonument, longitude, latitude, zoom, taille) {
    document.writeln(texteMonument(nomMonument, longitude, latitude, zoom, taille));
}


/* == texteMonument ==
Paramètres : 5
 nomMonument (chaine) : le nom du monument qui est écrit dans le titre
 laLongitude (flottant) : la longitude du centre de la carte affichée
 laLatitude (flottant) : la latitude du centre de la carte affichée
 zoom (entier) : le facteur de zoom dela google map (entre 0 et 20 compris)
 taille (entier) : la taille d'affichage de l'image
Résulat :
 type : chaîne de caractères
 description : un texte html représentant une section avec pour titre nomMonument et une image "gogle map" de la taille fournie, centrée sur la longitude et latitude indiquée, avec le zoom demandé.
*/

var texteMonument  = function(nomMonument, laLongitude, laLatitude, zoom, taille) {
    var titre = "<h2> "+ nomMonument+" </h2>";
    var texte = titre + imageGoogleMap(laLongitude, laLatitude, zoom, taille);

    return texte;
}

/* == texteMonument ==
Paramètres : 4
 nomMonument (chaine) : le nom du monument qui est écrit dans le titre
 longitude  (flottant) : la longitude du centre de la carte affichée
 latitude  (flottant) : la latitude du centre de la carte affichée
 zoom (entier) : le facteur de zoom dela google map (entre 0 et 20 compris)
 taille (entier) : la taille d'affichage de l'image
Résultat :
 type : chaîne de caractères
 description : un texte html d'un balise img correspondant à une image "gogle map" de la taille fournie, centrée sur la longitude et latitude indiquée, avec le zoom demandé.
*/
var imageGoogleMap = function(longitude, latitude, zoom, taille) {

    var texteCenter = 'center='+longitude+','+latitude;
    var texteZoom = 'zoom='+zoom;
    var texteTaille = 'size='+taille+'x'+taille;

    var image = '<img src="http://maps.googleapis.com/maps/api/staticmap?';
    image = image+texteCenter;
    image = image+'&'+texteZoom;
    image = image+'&'+texteTaille;
    image = image+'&maptype=satellite&sensor=false">';

    return image;
}

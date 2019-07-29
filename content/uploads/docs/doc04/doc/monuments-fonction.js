
/* -- afficheMonument --
 Paramètres : 3
   nomMonument (chaine) : le nom du monument qui est écrit dans le titre
   longitude (flottant) : la longitude du centre de la carte affichée
   latitude  (flottant) : la latitude du centre de la carte affichée
 Résultat : aucun
 Effet de bord : affiche dans la page une section avec pour titre nomMonument
    et une image "gogle map"  centrée sur la longitude et latitude indiquée.
 -------------------- */


var afficheMonument = function (nomMonument, longitude, latitude) {
    var texte = texteMonument(nomMonument, longitude, latitude);
    document.writeln(texte);
}



/* -- texteMonument --
 Paramètres : 3
   nomMonument (chaine) : le nom du monument qui est écrit dans le titre
   laLongitude (flottant) : la longitude du centre de la carte affichée
   laLatitude (flottant) : la latitude du centre de la carte affichée
 Résulat :
   type : chaîne de caractères
   description : un texte html représentant une section avec pour titre nomMonument
     et une image "gogle map"  centrée sur la longitude et latitude indiquée.
  -------------------- */

var texteMonument = function (nomMonument, laLongitude, laLatitude) {
    var titre = "<h2> Monument&nbsp;: "+ nomMonument+" </h2>";
    var texteImage = imageGoogleMap(laLongitude, laLatitude);
    var texte = titre + texteImage;

    return texte;
}



/* -- texteMonument --
 Paramètres : 2
   nomMonument (chaine) : le nom du monument qui est écrit dans le titre
   longitude  (flottant) : la longitude du centre de la carte affichée
   latitude  (flottant) : la latitude du centre de la carte affichée
 Résultat :
   type : chaîne de caractères
   description : un texte html d'un balise img correspondant à une image "gogle map" 
    centrée sur la longitude et latitude indiquée. La taille de l'image est un carré
    de taille 400 et le facteur de zoom et 17 .
 -------------------- */

var imageGoogleMap = function (longitude, latitude) {

    var texteCenter = "center="+longitude+","+latitude;

    var texte = "<img src=\"http://maps.googleapis.com/maps/api/staticmap?";
    texte = texte+texteCenter;
    texte = texte+"&zoom=17&size=400x400&maptype=satellite&sensor=false\">";

    return texte;
}


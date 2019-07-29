// **************************
// **** Données globales **** 
// **************************
 
// -- facteur de zoom sur les images
var facteurZoom = 17;
// -- taille des images (idem pour largeur et hauteur)
var tailleImage = 400; 



// ***********************
// ****** FONCTIONS ******
// ***********************

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
   longitude (flottant) : la longitude du centre de la carte affichée
   latitude (flottant) : la latitude du centre de la carte affichée
 Résulat :
   type : chaîne de caractères
   description : un texte html représentant une section avec pour titre nomMonument
     et une image "gogle map"  centrée sur la longitude et latitude indiquée.
  -------------------- */

var texteMonument = function (nomMonument, longitude, latitude) {
    var titre = "<h2> Monument&nbsp;: "+ nomMonument+" </h2>";
    var texteImage = imageGoogleMap(longitude, latitude);
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
    texte = texte+"&zoom="+facteurZoom;
    texte = texte+"&size="+tailleImage+"x"+tailleImage;
    texte = texte+"&maptype=satellite&sensor=false\">";

    return texte;
}


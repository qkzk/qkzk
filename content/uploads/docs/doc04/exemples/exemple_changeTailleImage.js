

var setupEvents = function() {
    var plusPetite = document.getElementById("plusPetite");
    plusPetite.addEventListener("click",reduit);
    var plusGrande = document.getElementById("plusGrande");
    plusGrande.addEventListener("click",agrandit);

}

window.addEventListener("load", setupEvents);

// ==================================================


// augmente la taille de l'image d'id "changeante" 
var agrandit = function() {
    var img =  document.getElementById("changeante");
    // récupère la taille actuelle
    var taille = parseInt(img.width);
    if (taille < 400) {
	// augmente la taille
	taille = taille + 20;
    }
    // fixe la nouvelle taille
    img.style.width = taille+"px";
    // change la valeur affichée dans l'élément "tailleInfo"
    var tailleInfo = document.getElementById("tailleInfo");
    tailleInfo.innerHTML = taille;
}
// diminue la taille de l'image d'id "changeante" 
var reduit = function() {
    var img =  document.getElementById("changeante");
    var taille = parseInt(img.width);
    if (taille > 100) {
	taille = taille - 20;
    }
    img.style.width = taille+"px";
    var tailleInfo = document.getElementById("tailleInfo");
    tailleInfo.innerHTML = taille;
}

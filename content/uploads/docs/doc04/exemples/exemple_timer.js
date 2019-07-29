
var setupEvents = function() {
    var buttonStart = document.getElementById("start");
    buttonStart.addEventListener("click", start);

    var stopButton = document.getElementById("stop");
    stopButton.addEventListener("click", stop);

}

var init = function() {
    var elt = document.getElementById("test");
    elt.style.backgroundColor = "white";
    afficheRGB();
}


window.addEventListener("load", setupEvents);
window.addEventListener("load", init);

//======================================================================
// variable pour mémoriser le timer ce qui d'une part permet de l'arrêter
//          et d'autre part évite d'en démarrer un second timer
var timer = null;

var start = function() {
    // changement de couleur toutes les 5ms
    if (timer==null) { // timer pas encore démarré ?
	timer = window.setInterval(changeColor,5);
    }
}

var stop = function () {
    // arrêt du timer (donc arrêt du changement de couleur)
    window.clearInterval(timer);
    timer = null; 
}

// calcule le prochain triplet r,g,b en modifiant l'une des composantes
// de "delta" (+/-1). On modifie d'abord le R puis le G pour le B.
var changeColor = function () {
    var elt = document.getElementById("test"); 
    // identifie la prochaine couleur à changer
    if (rColor < 255 && rColor > 0) {
	rColor = rColor + delta;
    } else if (gColor != rColor) {
	gColor = gColor + delta;
    } else if (bColor != gColor) {
	bColor = bColor + delta;
    } else {
	delta = -delta; 
	rColor = rColor + delta;
    }
    // met à jour l'affichage des R,G,B
    afficheRGB();
    // met à jour la couleur
    elt.style.backgroundColor = buildRGB(rColor, gColor, bColor);
}

// variation des couleurs : si +1 on incrémente si -1 on décrémente
var delta = +1;
// les valeurs rgb de la couleur courante
var rColor = 255;
var gColor = 255;
var bColor = 255;

// construit et retourne la chaîne de caractère rgb(...)
var buildRGB = function(color) {
    return "rgb("+rColor+","+gColor+","+bColor+")";
}

// affiche les infos RGB
var afficheRGB = function () {
    var R = document.getElementById("R"); 
    R.innerHTML = rColor;
    var G = document.getElementById("G"); 
    G.innerHTML = gColor;
    var B = document.getElementById("B"); 
    B.innerHTML = bColor;
}

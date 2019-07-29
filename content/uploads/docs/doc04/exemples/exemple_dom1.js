

var setupEvents = function() {

    var devoileButton = document.getElementById("devoile");
    devoileButton.addEventListener("click",devoile);
    var cacheButton = document.getElementById("cache");
    cacheButton.addEventListener("click",cache);

    
}

window.addEventListener("load", setupEvents);

// ==================================================


// rend visible un élément masqué 
// et donne l'impression de modifier un bouton en cachant/masquant un couple de "boutons"
var devoile = function() {
    // devoile le texte
    var cache = document.getElementById("txtcache");
    cache.style.display = "block";
    // devoile le bouton "cache"
    var cacheButton = document.getElementById("cache");
    cacheButton.style.display = "inline";
    // cache le bouton devoile
    this.style.display = "none";
}
// cache l'élément "txtcache"
var cache = function() {
    // cache le texte
    var cache = document.getElementById("txtcache");
    cache.style.display = "none";
    // devoile le bouton "devoile"
    var devoileButton = document.getElementById("devoile");
    devoileButton.style.display = "inline";
    // cache le bouton cache
    this.style.display = "none";
}



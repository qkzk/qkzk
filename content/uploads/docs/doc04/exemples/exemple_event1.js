var setupEvents = function() {
    // gestion événement pour piedDePage
    var pied =  document.getElementById("piedDePage");
    pied.addEventListener("click",action1);
}

window.addEventListener("load", setupEvents);

// ==================================================

// définition des fonctions
var action1 = function() {
    window.alert("on a cliqué sur le pied de page");
}

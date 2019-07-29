
function sesame() {
    var motDePasse = window.prompt("Indiquez le mot secret pour voir l'image");
    if (motDePasse == "secret") {
	var imagePrivee =  document.getElementById("privee");
	imagePrivee.src = "orionMessier.jpg";
    } 
    else {
	window.alert("Vous n'avez pas fourni le mot secret.");
    }
}

window.addEventListener("load", sesame);




function initGoogleMap() {
    var lElement  = document.getElementById("maCarte");
    var leCentre = new google.maps.LatLng(50.609731,3.137511);
    var lesOptions = {
	center: leCentre,
	zoom: 18,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var laCarte = new google.maps.Map(lElement, lesOptions);
	
}

window.addEventListener("load",initGoogleMap);

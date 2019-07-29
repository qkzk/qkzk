var setupEvents = function() {

    var tFahrenheit =  document.getElementById("tFahrenheit");
    tFahrenheit.addEventListener("change",fahrenheitVersCelsius);

    var tCelsius =  document.getElementById("tCelsius");
    tCelsius.addEventListener("change",celsiusVersFahrenheit);
}

window.addEventListener("load", setupEvents);

//==================================================

var fahrenheitVersCelsius = function() {
    var tFahrenheit =  document.getElementById("tFahrenheit");
    var tempF = parseInt(tFahrenheit.value);
    var tCelsius = document.getElementById("tCelsius");
    tCelsius.value = ((tempF - 32) *  5 / 9).toFixed(2);
}

var celsiusVersFahrenheit = function() {
    var tCelsius =  document.getElementById("tCelsius");
    var tempC = parseInt(tCelsius.value);
    var tFahrenheit = document.getElementById("tFahrenheit");
    tFahrenheit.value = (9/5*tempC + 32).toFixed(2);
}

var toggle = document.getElementById("dark-mode-toggle");

var darkTheme = document.getElementById("dark-mode-theme");

toggle.addEventListener("click", () => {
    if (toggle.className === "toggle_dark") {
        setTheme("dark");
    } else if (toggle.className === "toggle_light") {
        setTheme("light");
    }
});
// the default theme is light
var savedTheme = localStorage.getItem("dark-mode-storage") || "light";
setTheme(savedTheme);

function setTheme(mode) {
    localStorage.setItem("dark-mode-storage", mode);

    if (mode === "dark") {
        darkTheme.disabled = false;
        toggle.className = "toggle_light";
        toggle.innerHTML = '<i class="fas fa-sun"></i>';
    } else if (mode === "light") {
        darkTheme.disabled = true;
        toggle.className = "toggle_dark";
        toggle.innerHTML = '<i class="fas fa-moon"></i>';
    }
    console.log(`Shitched to theme ${mode}`);

}

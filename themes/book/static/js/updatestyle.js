/*
author : qkzk

FILE INCLUDED IN FOOTER
FOR STYLING PURPOSE
*/

/*
Inspired by w3Schools : https://www.w3schools.com/howto/howto_js_treeview.asp

Expand and hide (active and nested) after every clic on a "+" in the nav menu

Welcome to the worst algorithm ever !
It works... untill it breaks :)
*/



window.onload = updateStyle

function updateStyle() {
    setRandomBanner();
}


function setRandomBanner() {
    // banner img : change the banner
    let imgNumber = 5;
    let nbr = Math.floor(imgNumber * Math.random()) + 1;
    let imgName = '/banner/back' + nbr + '.jpg'
    document.getElementById("bannerImg").style.backgroundImage = 'url(' + imgName + ')';
}

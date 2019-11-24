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

// first we find the top UL element and remove it from active/inactive
var ul = document.querySelector('#main-container > aside.book-menu.fixed > nav > div > ul');
ul.setAttribute("id", "myUL");
ul.removeAttribute("class", "nested");

// then we find every element with class "caret"
var toggler = document.getElementsByClassName("caret");

// and we toggle their direct parent
for (let i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
    // every 2 clicks the parent lost the class "caret", so we add it back here
    this.classList.add("caret");
  });
}


window.onload = updateStyle

function updateStyle(){

  // first we close every onpened caret and nest every active element
  var topNav = document.getElementById("myUL");
  nestChildren(topNav);

  // then we show every direct parent of the active page
  styleMenuLinks()


  // then we set a random banner
  setRandomBanner();

  // set previous next links at the bottom
  // TODO enable this annoying feature again
  // previousNextLinks();
}

function styleMenuLinks(){

  // open all parent details of active page
  // color all parent links
  let activeLinkNode = document.getElementsByClassName("active");
  let parentNode = activeLinkNode[0]
  while (parentNode){
    var nested = parentNode.querySelector(".nested")
    if (nested != null) {
      if (nested.contains(activeLinkNode[0])) {
        // console.log("CONTAINS :");
        nested.classList.add("active");
      }
    }
    if (parentNode.nodeName == "LI"){
      // open the SPAN
      var children = parentNode.children;
      // console.log(children);
      parentNode.setAttribute("class", "coucher");
      for (var i = 0; i<children.length; i++){
        // console.log(children[i].tagName);
        if (children[i].tagName == "SPAN"){
          children[i].setAttribute("class", "caret-down");
          colorParentLinks(parentNode);
        }
      }
    }
    if (parentNode.parentNode.tagName == "DIV") {
      //console.log('reached the top');
      break;
    }
    parentNode = parentNode.parentNode;
  }
}


function nestChildren(element) {
  // close every opened caret, nest every active item
  var children = element.childNodes;
  children.forEach(function(item){
    if (item.tagName == "UL") {
      item.removeAttribute("class", "active");
      item.setAttribute("class", "nested");
    } else if (item.tagName == "SPAN") {
      item.removeAttribute("class", "caret-down");
      item.setAttribute("class", "caret");
    }
    nestChildren(item)
  });
}

function colorParentLinks(parentNode){
  // color the link of direct parents

  // color the links of parents
  let siblingsNodes = parentNode.childNodes;
  // console.log(siblingsNodes);
  if (siblingsNodes.length > 0){
    // console.log(siblingsNodes[1])
    if (siblingsNodes[1]){
      if (siblingsNodes[1].nodeName == "SPAN"){
        // console.log(siblingsNodes[1])
        let spanNode = siblingsNodes[1];
        spanNode.style.color = "#5555FF";
        let summaryChildren = spanNode.childNodes;
        // console.log(summaryChildren)
        let linkNode = summaryChildren[1];
        linkNode.style.color = "#5555FF";
        linkNode.style.fontWeight = "bold";
      }
    }
  }
}

function setRandomBanner(){
  // banner img : change the banner
  let imgNumber = 5;
  let nbr = Math.floor( imgNumber * Math.random() ) + 1;
  let imgName = '/banner/back' + nbr + '.jpg'
  document.getElementById("bannerImg").style.backgroundImage = 'url(' + imgName + ')';
  // console.log(imgName);
}

//
//
// function previousNextLinks(){
//   // set the links of the previous and next arrow accordingly
//
//   // first we need to know if there's siblings in the menu to that page
//
//   // how many siblings ?
//   let siblingsNumbers = document.getElementsByClassName("active")[0].parentNode.parentNode.parentNode.parentNode.childElementCount;
//   // console.log("siblingsNumbers");
//   // console.log(siblingsNumbers);
//   // next and previous ?
//   let parent = document.getElementsByClassName("active")[0].parentNode.parentNode.parentNode.parentNode;
//
//   // console.log("parent")
//   // console.log(parent)
//   let siblings = parent.children;
//   // console.log("siblings");
//   // console.log(siblings);
//
//   // we check the number of the current page in the menu.
//   let activeLinkNumber = getActiveLinkNumber(siblings);
//   // console.log(activeLinkNumber)
//
//   // if the number is -1, there was an error while we tried to retrieve it.
//   if (activeLinkNumber != - 1){
//     if (activeLinkNumber > 1){
//       let previousLinkNumber = activeLinkNumber - 1;
//       var previousLinkDest = siblings[previousLinkNumber].firstElementChild.firstElementChild.firstElementChild.href;
//       // console.log(previousLinkDest);
//     }
//     else {
//       let previousLinkDest = null;
//     }
//     if (activeLinkNumber < siblings.length - 1){
//       let nextLinkNumber = activeLinkNumber + 1;
//       var nextLinkDest = siblings[nextLinkNumber].firstElementChild.firstElementChild.firstElementChild.href;
//       // console.log(nextLinkDest);
//     }
//     else {
//       let nextLinkDest = null;
//     }
//     // we set the links to visible and set the hrefs.
//     populateNextAndPreviousLinks([previousLinkDest, nextLinkDest]);
//   }
// }
//
// function getActiveLinkNumber(siblings){
//   // tries to retrieve the number of the active page in the menu.
//
//   try{
//     for (var i = 0; i < siblings.length; i++){
//       sister = siblings[i];
//       // console.log("li sister")
//       // console.log(sister)
//       if (sister.firstElementChild.hasChildNodes() && sister.nodeName == "LI"){
//         // console.log("details")
//         // console.log(sister.firstElementChild);
//
//         let sister_details = sister.firstElementChild;
//         let sister_summary = sister_details.firstElementChild;
//         // console.log("sister_summary");
//         // console.log(sister_summary);
//
//         sister_a = sister_summary.firstElementChild;
//         // console.log("sister_a");
//         // console.log(sister_a);
//         // console.log("sister_a.classList")
//         // console.log(sister_a.classList)
//         // console.log("active" in sister_a.classList)
//         // console.log(i)
//         if (sister_a.classList[0] == "active"){
//           return i;
//         }
//       }
//     }
//   }
//   catch(err){
//     return -1;
//   }
// }
//
// function populateNextAndPreviousLinks(arraylinks){
//   // populate the element of links
//   let previousLinkDest = arraylinks[0];
//   let nextLinkDest = arraylinks[1];
//   // console.log(previousLinkDest);
//   // console.log(nextLinkDest);
//
//   if (previousLinkDest){
//     // console.log("previous !")
//     document.getElementById("link_previous").style.display ='block';
//     document.getElementById("link_previous").href = previousLinkDest;
//   }
//   else {
//     document.getElementById("link_previous").style.display ='none';
//   }
//   if (nextLinkDest){
//     // console.log("next !")
//     document.getElementById("link_next").style.display ='block';
//     document.getElementById("link_next").href = nextLinkDest;
//   }
//   else {
//     document.getElementById("link_next").style.display ='none';
//   }
// }

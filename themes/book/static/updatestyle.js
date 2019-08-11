/*
author : qkzk

FILE INCLUDED IN FOOTER
FOR STYLING PURPOSE
*/

window.onload = updateStyle

function updateStyle(){
  // set the style of menu links
  styleMenuLinks()
  // set the banner
  setBanner();
  // set previous next links at the bottom
  previousNextLinks();
}

function styleMenuLinks(){
  // open all parent details of active page
  // color all parent links
  let activeLinkNode = document.getElementsByClassName("active");
  let parentNode = activeLinkNode[0]
  while (parentNode){
    if (parentNode.nodeName = "DETAILS"){
      // open the DETAILS
      parentNode.open = true;
      // parentNode.style.color = "#5555FF";
      // color the links of direct parents
      colorParentLinks(parentNode);
    parentNode = parentNode.parentNode;
    }
  }
}


function colorParentLinks(parentNode){
  // color the link of direct parents

  // color the links of parents
  let siblingsNodes = parentNode.childNodes;
  // console.log(siblingsNodes);
  if (siblingsNodes.length > 0){
    // console.log(siblingsNodes[1])
    if (siblingsNodes[1]){
      if (siblingsNodes[1].nodeName == "SUMMARY"){
        // console.log(siblingsNodes[1])
        let summaryNode = siblingsNodes[1];
        summaryNode.style.color = "#5555FF";
        let summaryChildren = summaryNode.childNodes;
        // console.log(summaryChildren)
        let linkNode = summaryChildren[1];
        linkNode.style.color = "#5555FF";
        linkNode.style.fontWeight = "bold";
      }
    }
  }
}

function setBanner(){
  // banner img : change the banner
  let imgNumber = 5;
  let nbr = Math.floor( imgNumber * Math.random() ) + 1;
  let imgName = '/banner/back' + nbr + '.jpg'
  document.getElementById("bannerImg").style.backgroundImage = 'url(' + imgName + ')';
  // console.log(imgName);
}



function previousNextLinks(){
  // set the links of the previous and next arrow accordingly

  // first we need to know if there's siblings in the menu to that page

  // how many siblings ?
  let siblingsNumbers = document.getElementsByClassName("active")[0].parentNode.parentNode.parentNode.parentNode.childElementCount;
  // console.log("siblingsNumbers");
  // console.log(siblingsNumbers);
  // next and previous ?
  let parent = document.getElementsByClassName("active")[0].parentNode.parentNode.parentNode.parentNode;

  // console.log("parent")
  // console.log(parent)
  let siblings = parent.children;
  // console.log("siblings");
  // console.log(siblings);

  // we check the number of the current page in the menu.
  let activeLinkNumber = getActiveLinkNumber(siblings);
  // console.log(activeLinkNumber)

  // if the number is -1, there was an error while we tried to retrieve it.
  if (activeLinkNumber != - 1){
    if (activeLinkNumber > 1){
      let previousLinkNumber = activeLinkNumber - 1;
      var previousLinkDest = siblings[previousLinkNumber].firstElementChild.firstElementChild.firstElementChild.href;
      // console.log(previousLinkDest);
    }
    else {
      let previousLinkDest = null;
    }
    if (activeLinkNumber < siblings.length - 1){
      let nextLinkNumber = activeLinkNumber + 1;
      var nextLinkDest = siblings[nextLinkNumber].firstElementChild.firstElementChild.firstElementChild.href;
      // console.log(nextLinkDest);
    }
    else {
      let nextLinkDest = null;
    }
    // we set the links to visible and set the hrefs.
    populateNextAndPreviousLinks([previousLinkDest, nextLinkDest]);
  }
}

function getActiveLinkNumber(siblings){
  // tries to retrieve the number of the active page in the menu.

  try{
    for (var i = 0; i < siblings.length; i++){
      sister = siblings[i];
      // console.log("li sister")
      // console.log(sister)
      if (sister.firstElementChild.hasChildNodes() && sister.nodeName == "LI"){
        // console.log("details")
        // console.log(sister.firstElementChild);

        let sister_details = sister.firstElementChild;
        let sister_summary = sister_details.firstElementChild;
        // console.log("sister_summary");
        // console.log(sister_summary);

        sister_a = sister_summary.firstElementChild;
        // console.log("sister_a");
        // console.log(sister_a);
        // console.log("sister_a.classList")
        // console.log(sister_a.classList)
        // console.log("active" in sister_a.classList)
        // console.log(i)
        if (sister_a.classList[0] == "active"){
          return i;
        }
      }
    }
  }
  catch(err){
    return -1;
  }
}

function populateNextAndPreviousLinks(arraylinks){
  // populate the element of links
  let previousLinkDest = arraylinks[0];
  let nextLinkDest = arraylinks[1];
  // console.log(previousLinkDest);
  // console.log(nextLinkDest);

  if (previousLinkDest){
    // console.log("previous !")
    document.getElementById("link_previous").style.display ='block';
    document.getElementById("link_previous").href = previousLinkDest;
  }
  else {
    document.getElementById("link_previous").style.display ='none';
  }
  if (nextLinkDest){
    // console.log("next !")
    document.getElementById("link_next").style.display ='block';
    document.getElementById("link_next").href = nextLinkDest;
  }
  else {
    document.getElementById("link_next").style.display ='none';
  }
}

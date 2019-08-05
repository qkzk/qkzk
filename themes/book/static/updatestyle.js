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
        // summaryNode.style.content = "+z";
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

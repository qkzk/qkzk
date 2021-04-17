"use strict";

function makeGraphics() {
    let that = document.getElementById("graphics");

    /**
     * Initialize the graphics output.
     */
    that.init = async function () {
        Basthon.addEventListener("eval.display", function (data) {
            that.display(data);
        });
    };

    /**
     * Cleaning graphics.
     */
    that.clean = function() {
        // textContent seems faster than innerHTML...
        that.textContent = "";
    };

    /**
     * Display an element from Basthon data.
     */
    that.display = function (data) {
        that.clean();
        switch(data.display_type) {
        case "p5":
            var root = data.content;
            root.style.width = "100%";
            root.style.height = "100%";
            root.style.display = "flex";
            root.style.justifyContent = "center";
            root.style.alignItems = "center";
            
            function autoFit(node) {
                node.style.width = "auto";
                node.style.height = "auto";
                node.style.maxWidth = "100%";
                node.style.maxHeight = "100%";
            }

            // some canvas nodes can be added later so we observe...
            const observer = new MutationObserver(
                function(mutationsList, observer) {
                    for(const mutation of mutationsList)
                        for( const node of mutation.addedNodes )
                            if( ["canvas", "video"].includes(
                                node.tagName.toLowerCase()) )
                                autoFit(node);
                });
            observer.observe(root, { childList: true });
            
            root.querySelectorAll('canvas,video').forEach(autoFit);

            that.appendChild(root);
            break;
        case "matplotlib":
            var root = data.content;
            const canvas = root.querySelector('canvas');
            if( canvas ) root = canvas;
            root.style.width = "";
            root.style.height = "";
            root.style.maxWidth = "100%";
            root.style.maxHeight = "100%";
            that.appendChild(root);
            break;
        case "turtle":
            // Turtle result
            window.setTimeout(function () {
                that.innerHTML = data.content.outerHTML;
            }, 1);
            break;
        case "sympy":
            that.innerHTML = data.content;
            if( typeof(MathJax) === "undefined" ) {
                // dynamically loading MathJax
                console.log("Loading MathJax (Sympy expression needs it).");
                (function () {
                    let script = document.createElement("script");
                    script.type = "text/javascript";
                    script.src  = "https://cdn.jsdelivr.net/npm/mathjax@3.0.5/es5/tex-mml-chtml.js";
                    document.getElementsByTagName("head")[0].appendChild(script);
                })();
            } else {
                // otherwise, render it
                MathJax.typeset();
            }
            break;
        case "html":
            that.innerHTML = data.content;
            break;
        case "multiple":
            /* typically dispached by display() */
            for( let mime of ['image/svg+xml',
                              'image/png',
                              'text/html',
                              'text/plain'] ) {
                if( mime in data.content ) {
                    let content = data.content[mime];
                    if( mime === 'image/png' ) {
                        content = '<img src="data:image/png;base64,' + content + '" style="max-width: 100%; max-height: 100%;">';
                    }
                    that.innerHTML = content;
                    break;
                }
            }
            break;
        default:
            console.error("Not supported node type in eval.display result processing.");
        }
    };

    return that;
}

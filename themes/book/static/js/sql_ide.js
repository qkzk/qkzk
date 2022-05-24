function load(ide, worker_url, dbfile, init_file) {
    // Creates a new worker
    var worker = new Worker(worker_url);

    // Selects the DOM elements relative to the given element.
    var execBtn = ide.querySelector('button.execute');
    var outputElm = ide.querySelector('pre.output');
    var errorElm = ide.querySelector('div.error');
    var commandsElm = ide.querySelector('textarea.commands');

    // Start the worker in which sql.js will run
    worker.onerror = function(e) {
        console.log(e);
        errorElm.style.height = '2em';
        errorElm.textContent = e.message;
    };

    // Open a database
    worker.postMessage({ action: 'open' });

    function error(e) {
        console.log(e);
        errorElm.style.height = '2em';
        errorElm.textContent = e.message;
    }

    function print(text) {
        outputElm.innerHTML = text.replace(/\n/g, '<br>');
    }

    function noerror() {
        errorElm.style.height = '0';
    }

    // Execute the commands when the button is clicked
    function execEditorContent() {
        noerror()
        execute(editor.getValue() + ';');
    }

    // Performance measurement functions
    var tictime;
    if (!window.performance || !performance.now) { window.performance = { now: Date.now } }
    function tic() { tictime = performance.now() }
    function toc(msg) {
        var dt = performance.now() - tictime;
        console.log((msg || 'toc') + ": " + dt + "ms");
    }

    // Execute commands received
    function execute(commands) {
        tic();
        worker.onmessage = function(event) {
            var results = event.data.results;
            toc("Executing SQL");
            if (!results) {
                error({ message: event.data.error });
                return;
            }

            tic();
            outputElm.innerHTML = "";
            for (var i = 0; i < results.length; i++) {
                outputElm.appendChild(tableCreate(results[i].columns, results[i].values));
            }
            toc("Displaying results");
        }
        worker.postMessage({ action: 'exec', sql: commands });
        outputElm.textContent = "Fetching results...";
    }

    // Create an HTML table
    var tableCreate = function() {
        function valconcat(vals, tagName) {
            if (vals.length === 0) return '';
            var open = '<' + tagName + '>', close = '</' + tagName + '>';
            return open + vals.join(close + open) + close;
        }
        return function(columns, values) {
            var tbl = document.createElement('table');
            var html = '<thead>' + valconcat(columns, 'th') + '</thead>';
            var rows = values.map(function(v) { return valconcat(v, 'td'); });
            html += '<tbody>' + valconcat(rows, 'tr') + '</tbody>';
            tbl.innerHTML = html;
            return tbl;
        }
    }();

    execBtn.addEventListener(
        "click",
        execEditorContent,
        true
    );

    // Add syntax highlihjting to the textarea
    var editor = CodeMirror.fromTextArea(commandsElm, {
        mode: 'text/x-mysql',
        viewportMargin: Infinity,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: false,
        matchBrackets: true,
        autofocus: true,
        extraKeys: {
            "Ctrl-Enter": execEditorContent,
        }
    });


    // Closure which is executed if there's a given dbfile
    async function load_db_file(filepath) {
        console.log("dbfile :", filepath);
        worker.postMessage({ action: 'open' });

        const u = new URL(filepath);
        fetch(u).then(res => res.arrayBuffer()).then(buf => {
            try {
                worker.postMessage({ action: 'open', 'buffer': buf }, [buf]);
            } catch (exception) {
                worker.postMessage({ action: 'open', 'buffer': buf });
            }
        });
    }

    if (dbfile !== null) {
        load_db_file(dbfile);
    }


    // Closure which is executed if there's a give initfile
    async function load_init_file(filepath) {
        console.log("initfile :", filepath);

        const u = new URL(filepath);
        fetch(u).then(res => res.text()).then(text => {
            try {
                execute(text);
            } catch (exception) {
                console.log("commands failed");
            }
        });
    }

    if (init_file !== null) {
        load_init_file(init_file);
    }
}

/**
 *
 * Wait for an HTML element to be loaded like `div`, `span`, `img`, etc.
 * ex: `onElementLoaded("div.some_class").then(()=>{}).catch(()=>{})`
 * @param {*} elementToObserve wait for this element to load
 * @param {*} parentStaticElement (optional) if parent element is not passed then `document` is used
 * @return {*} Promise - return promise when `elementToObserve` is loaded
 */
function onElementLoaded(elementToObserve, parentStaticElement) {
    return new Promise((resolve, reject) => {
        try {
            if (document.querySelector(elementToObserve)) {
                resolve(true);
                return;
            }
            const parentElement = parentStaticElement
                ? document.querySelector(parentStaticElement)
                : document;

            const observer = new MutationObserver((_mutationList, obsrvr) => {
                const divToCheck = document.querySelector(elementToObserve);

                if (divToCheck) {
                    console.log(`element loaded: ${elementToObserve}`);
                    obsrvr.disconnect(); // stop observing
                    resolve(true);
                }
            });

            // start observing for dynamic div
            observer.observe(parentElement, {
                childList: true,
                subtree: true,
            });
        } catch (e) {
            console.log(e);
            reject(Error("some issue... promise rejected"));
        }
    });
}


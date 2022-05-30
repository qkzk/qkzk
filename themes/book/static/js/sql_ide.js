function load(ide, worker_url, dbfile, init_file) {
    // Creates a new worker
    const worker = new Worker(worker_url);

    // Selects the DOM elements relative to the given element.
    const textarea_elm = ide.querySelector('textarea.commands');
    const output_elm = ide.querySelector('pre.output');
    const error_elm = ide.querySelector('div.error');
    const btn_execute = ide.querySelector('a.execute');
    const btn_reset = ide.querySelector('a.reset');
    const btn_download = ide.querySelector('a.download');

    const initial_editor_value = textarea_elm.value;


    function error(e) {
        console.log(e);
        error_elm.style.height = '2em';
        error_elm.textContent = e.message;
    }

    function print(text) {
        output_elm.innerHTML = text.replace(/\n/g, '<br>');
    }

    function noerror() {
        error_elm.style.height = '0';
    }

    // Execute the commands when the button is clicked
    function execEditorContent() {
        noerror()
        execute(editor.getValue() + ';');
    }


    // Execute commands received
    function execute(commands) {
        worker.onmessage = function(event) {
            var results = event.data.results;
            if (!results) {
                error({ message: event.data.error });
                return;
            }

            output_elm.innerHTML = "";
            for (var i = 0; i < results.length; i++) {
                output_elm.appendChild(tableCreate(results[i].columns, results[i].values));
            }
        }
        worker.postMessage({ action: 'exec', sql: commands });
        output_elm.textContent = "Fetching results...";
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
            tbl.classList.add("sql");
            var html = '<thead>' + valconcat(columns, 'th') + '</thead>';
            var rows = values.map(function(v) { return valconcat(v, 'td'); });
            html += '<tbody>' + valconcat(rows, 'tr') + '</tbody>';
            tbl.innerHTML = html;
            return tbl;
        }
    }();

    // Start the worker in which sql.js will run
    worker.onerror = function(e) {
        console.log(e);
        error_elm.style.height = '2em';
        error_elm.textContent = e.message;
    };

    // Open a database
    worker.postMessage({ action: 'open' });

    // Download editor content
    function download_editor() {
        download("commands.sql", editor.getValue());
    }

    // Reset editor content
    function reset_editor() {
        editor.setValue(initial_editor_value);
    }

    function remove_focus() {
        editor.display.input.blur();
    }

    btn_execute.addEventListener( "click", execEditorContent, true);
    btn_reset.addEventListener("click", reset_editor, true);
    btn_download.addEventListener("click", download_editor, true);

    // Add syntax highlighting to the textarea
    var editor = CodeMirror.fromTextArea(textarea_elm, {
        mode: 'text/x-mysql',
        viewportMargin: Infinity,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: false,
        matchBrackets: true,
        autofocus: true,
        theme: "idea",
        extraKeys: {
            "Tab": (cm) => cm.execCommand("indentMore"),
            "Shift-Tab": (cm) => cm.execCommand("indentLess"),
            "Esc": remove_focus,
            "Ctrl-Enter": execEditorContent,
            "Ctrl-R": reset_editor,
            "Ctrl-S": download_editor,
            "Ctrl-K": (cm) => cm.execCommand("deleteLine"),
            "Ctrl-/": (cm) => cm.execCommand("toggleComment"),
        },
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


function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
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


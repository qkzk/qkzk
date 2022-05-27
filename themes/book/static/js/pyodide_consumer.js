async function init_worker(ide, url, initfile) {

    const textarea_elm = ide.querySelector('textarea.commands');
    const output_elm = ide.querySelector('pre.python_output');
    const python_error_elm = ide.querySelector('pre.python_error');
    const worker_error_elm = ide.querySelector('pre.worker_error');
    const btn_execute = ide.querySelector('button.execute');
    const btn_reset = ide.querySelector('button.reset');
    const btn_download = ide.querySelector('button.download');

    const initial_editor_value = textarea_elm.value;


    // Add syntax highlihjting to the textarea
    var editor = CodeMirror.fromTextArea(textarea_elm, {
        mode: {
            name: "python",
            version: 3,
            singleLineStringErrors: false
        },
        viewportMargin: Infinity,
        indentWithTabs: false,
        smartIndent: true,
        lineNumbers: true,
        matchBrackets: true,
        indentUnit: 4,
        autofocus: true,
        theme: "idea",
        extraKeys: {
            "Ctrl-Enter": read_run_code,
             "Tab": (cm) => cm.execCommand("indentMore"),
             "Shift-Tab": (cm) => cm.execCommand("indentLess"),
        }
    });

    const pyodideWorker = new Worker(url);
    const callbacks = {};

    /*
    * Called when the worker post a response.
    * Use the given callback from the response.
    */
    function onMessage(event) {
        const { id, ...data } = event.data;
        const onSuccess = callbacks[id];
        delete callbacks[id];
        onSuccess(data);
    }

    // Attach the onMessage function to Worker method
    pyodideWorker.onmessage = onMessage;

    // Allow async execution in the worker
    const asyncRun = (() => {
        let id = 0; // identify a Promise
        return (script, context) => {
            // the id could be generated more carefully
            id = (id + 1) % Number.MAX_SAFE_INTEGER;
            return new Promise((onSuccess) => {
                callbacks[id] = onSuccess;
                pyodideWorker.postMessage({
                    ...context,
                    python: script,
                    id,
                });
            });
        };
    })();


    /*
    *   Run a script, fill an object with the worker response.
    */
    async function run_code(script) {
        var output = null;
        var python_error = null;
        var worker_error = null;

        try {
            const { results, error } = await asyncRun(script, "");
            if (results) {
                output = results;
            } else if (error) {
                python_error = error;
            }
        } catch (e) {
            worker_error = `pyodide worker error at ${e.filename}, Line: ${e.lineno}, ${e.message}`
        }

        return {
            "output": output,
            "python_error": python_error,
            "worker_error": worker_error,
        }
    }

    /*
    * read code from the editor and the init file content.
    * run it through the worker
    * fill the output elements in the document
    * Hide empty elements from the document
    */
    async function read_run_code() {
        var init_content;
        if (initfile !== null) {
            init_content = await load_init_file(initfile);
        } else {
            init_content = "";
        }

        var editor_code = await editor.getValue();
        var script = init_content + editor_code;
        let resp = await run_code(script)

        fillOutput(resp);
        displayOrHideOutputs(resp);

    }

    // Replaces output elements innerText with worker response
    function fillOutput(resp) {
        output_elm.innerText = resp.output;
        python_error_elm.innerText = resp.python_error;
        worker_error_elm.innerText = resp.worker_error;
    }

    // Hide empty elements, display non empty ones.
    function displayOrHideOutputs(resp) {
        if (resp.output === null) { 
            output_elm.style.display="none"; }
        else {
            output_elm.style.display="block";
        }
        if (resp.python_error === null) { 
            python_error_elm.style.display="none"; }
        else {
            python_error_elm.style.display="block";
        }
        if (resp.worker_error === null) { 
            worker_error_elm.style.display="none"; }
        else {
            worker_error_elm.style.display="block";
        }
    }

    // Download editor content
    function download_editor() {
        const content = editor.getValue();
        download("script.py", content);
    }

    // Reset editor content
    function reset_editor() {
        editor.setValue(initial_editor_value);
    }

    btn_execute.addEventListener("click", read_run_code, true);
    btn_reset.addEventListener("click", reset_editor, true);
    btn_download.addEventListener("click", download_editor, true);
}

/*
* Download a text content to a file.
* Creates an <a> element with download action, clicks it and removes it.
*/
function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

/* 
* Load the init file content. Returns it as a string.
*/
async function load_init_file(filepath) {
    const u = new URL(filepath);
    return await fetch(u).then(res => res.text()).then(text => text);
}

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
export { init_worker, onElementLoaded };


// test interruption from server.
// doesn't work locally
try {
    var a = new SharedArrayBuffer(1);
    console.log("SharedArrayBuffer", a);
} catch(error) {
    console.log(error.message);
}

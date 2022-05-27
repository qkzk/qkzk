// webworker.js

// Setup your project to serve `py-worker.js`. You should also serve
// `pyodide.js`, and all its associated `.asm.js`, `.data`, `.json`,
// and `.wasm` files as well:
importScripts("https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js");

// var paragraph = document.getElementById("print");

async function loadPyodideAndPackages() {
    self.pyodide = await loadPyodide({
        // stdout: (text) => {paragraph.textContent += text;},
    });
    // await self.pyodide.loadPackage(["numpy", "pytz"]);
}
let pyodideReadyPromise = loadPyodideAndPackages();

self.onmessage = async (event) => {
    // make sure loading is done
    await pyodideReadyPromise;
    // Don't bother yet with this line, suppose our API is built in such a way:
    const { id, python, ...context } = event.data;
    console.log("onmessage, python:", python);
    // The worker copies the context in its own "memory" (an object mapping name to values)
    for (const key of Object.keys(context)) {
        self[key] = context[key];
    }
    // Now is the easy part, the one that is similar to working in the main thread:
    try {
        await self.pyodide.loadPackagesFromImports(python);
        let results = await self.pyodide.runPythonAsync(python);
        results = prepareResults(results);
        self.postMessage({ results, id });
    } catch (error) {
        self.postMessage({ error: error.message, id });
    }
};

/*
*   Prevents error :
*   pyodide Failed to execute 'postMessage' on 'DedicatedWorkerGlobalScope': [object Object] could not be cloned.
*   and converts true, false, undefined to
*   their Python's equivalent : True, False, None
*/
function prepareResults(results) {
    console.log("results", results, typeof results);
    if (pyodide.isPyProxy(results)) { 
        let temp = results.toString();
        console.log("catched proxy results", temp);
        results.destroy();
        results = temp;
    } else if (results === false) {
        console.log("catched false", results);
        results = "False";
    } else if (results === true) {
        console.log("catched false", results);
        results = "True";
    } else if (typeof results === 'undefined') {
        console.log("catched undefined", results);
        results = "None";
    }
    return results
}

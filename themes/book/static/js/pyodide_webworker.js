// webworker.js

// Setup your project to serve `py-worker.js`. You should also serve
// `pyodide.js`, and all its associated `.asm.js`, `.data`, `.json`,
// and `.wasm` files as well:
importScripts("https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js");

async function loadPyodideAndPackages() {
    self.pyodide = await loadPyodide({
    });
    // await self.pyodide.loadPackage(["numpy", "pytz"]);
}

let pyodideReadyPromise = loadPyodideAndPackages();

self.onmessage = async (event) => {
    // make sure loading is done
    await pyodideReadyPromise;

     if (event.data.cmd === "setInterruptBuffer") {
        pyodide.setInterruptBuffer(event.data.interruptBuffer);
        return;
      }
    if (event.data.cmd === "runCode") {
        // Don't bother yet with this line, suppose our API is built in such a way:
        const { id, python, ...context } = event.data.code;
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
    }
};

// self.addEventListener("message", (msg) => {
//   if (msg.data.cmd === "setInterruptBuffer") {
//     pyodide.setInterruptBuffer(msg.data.interruptBuffer);
//     return;
//   }
//   if (msg.data.cmd === "runCode") {
//     pyodide.runPython(msg.data.code);
//     return;
//   }
// });

/*
*   Prevents error and replace js format by python format.
*   Some JS objects are proxied before being sent back, we need to stringify them.
*   pyodide Failed to execute 'postMessage' on 'DedicatedWorkerGlobalScope': [object Object] could not be cloned.
*   converts true, false, undefined, Infinity, NaN to
*   their Python's equivalent : True, False, None, inf, nan
*   This is quite disapointing...
*/
function prepareResults(results) {
    if (pyodide.isPyProxy(results)) {
        let temp = results.toString();
        results.destroy();
        results = temp;
    } else if (results === false) {
        results = "False";
    } else if (results === true) {
        results = "True";
    } else if (typeof results === 'undefined') {
        results = "None";
    } else if (results === Infinity) {
        results = "inf";
    } else if (typeof results === 'number' && isNaN(results)) {
        results = "nan";
    }
    return results
}

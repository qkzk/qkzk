import { asyncRun } from "./py-worker.js";

// const script = `
//     import statistics
//     from js import A_rank
//     statistics.stdev(A_rank)
// `;
//
// const context = {
//     A_rank: [0.8, 0.4, 1.2, 3.7, 2.6, 5.8],
// };

async function run_code(script, context) {
    var output = null;
    var python_error = null;
    var worker_error = null;

    try {
        const { results, error } = await asyncRun(script, context);
        if (results) {
            console.log("pyodideWorker return results: ", results);
            output = results;
        } else if (error) {
            console.log("pyodideWorker error: ", error);
            python_error = error;
        }
    } catch (e) {
        worker_error = `Error in pyodideWorker at ${e.filename}, Line: ${e.lineno}, ${e.message}`
        console.log(worker_error);
    }

    return {
        "output": output,
        "python_error": python_error,
        "worker_error": worker_error,
    }
}

export { run_code };


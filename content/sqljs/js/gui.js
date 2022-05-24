var execBtn = document.getElementById("execute");
var outputElm = document.getElementById('output');
var errorElm = document.getElementById('error');
var commandsElm = document.getElementById('commands');
var dbFileElm = document.getElementById('dbfile');
var savedbElm = document.getElementById('savedb');

// Start the worker in which sql.js will run
var worker = new Worker("./js/worker.sql-wasm.js");
worker.onerror = error;

// Open a database
worker.postMessage({ action: 'open' });

// Connect to the HTML element we 'print' to
function print(text) {
    outputElm.innerHTML = text.replace(/\n/g, '<br>');
}
function error(e) {
    console.log(e);
    errorElm.style.height = '2em';
    errorElm.textContent = e.message;
}

function noerror() {
    errorElm.style.height = '0';
}

// Run a command in the database
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

// Execute the commands when the button is clicked
function execEditorContents() {
    noerror()
    execute(editor.getValue() + ';');
}
execBtn.addEventListener("click", execEditorContents, true);

// Performance measurement functions
var tictime;
if (!window.performance || !performance.now) { window.performance = { now: Date.now } }
function tic() { tictime = performance.now() }
function toc(msg) {
    var dt = performance.now() - tictime;
    console.log((msg || 'toc') + ": " + dt + "ms");
}

// Add syntax highlihjting to the textarea
var editor = CodeMirror.fromTextArea(commandsElm, {
    mode: 'text/x-mysql',
    viewportMargin: Infinity,
    indentWithTabs: true,
    smartIndent: true,
    lineNumbers: true,
    matchBrackets: true,
    autofocus: true,
    extraKeys: {
        "Ctrl-Enter": execEditorContents,
        "Ctrl-S": savedb,
    }
});

// Load a db from a file
dbFileElm.onchange = function() {
    var f = dbFileElm.files[0];
    var r = new FileReader();
    r.onload = function() {
        worker.onmessage = function() {
            toc("Loading database from file");
            // Show the schema of the loaded database
            editor.setValue("SELECT `name`, `sql`\n  FROM `sqlite_master`\n  WHERE type='table';");
            execEditorContents();
        };
        tic();
        try {
            worker.postMessage({ action: 'open', buffer: r.result }, [r.result]);
        }
        catch (exception) {
            worker.postMessage({ action: 'open', buffer: r.result });
        }
    }
    r.readAsArrayBuffer(f);
}

// Save the db to a file
function savedb() {
    worker.onmessage = function(event) {
        toc("Exporting the database");
        var arraybuff = event.data.buffer;
        var blob = new Blob([arraybuff]);
        var a = document.createElement("a");
        document.body.appendChild(a);
        a.href = window.URL.createObjectURL(blob);
        a.download = "sql.db";
        a.onclick = function() {
            setTimeout(function() {
                window.URL.revokeObjectURL(a.href);
            }, 1500);
        };
        a.click();
    };
    tic();
    worker.postMessage({ action: 'export' });
}
savedbElm.addEventListener("click", savedb, true);

/*
*       Write changes below this comment lines
*
*
*/




const create_db_employee = `
DROP TABLE IF EXISTS employees;
CREATE TABLE employees( id integer, name text,
designation text, manager integer,
hired_on date, salary integer,
commission float, dept integer);

INSERT INTO employees VALUES (1,'JOHNSON','ADMIN',6,'1990-12-17',18000,NULL,4);
INSERT INTO employees VALUES (2,'HARDING','MANAGER',9,'1998-02-02',52000,300,3);
INSERT INTO employees VALUES (3,'TAFT','SALES I',2,'1996-01-02',25000,500,3);
INSERT INTO employees VALUES (4,'HOOVER','SALES I',2,'1990-04-02',27000,NULL,3);
INSERT INTO employees VALUES (5,'LINCOLN','TECH',6,'1994-06-23',22500,1400,4);
INSERT INTO employees VALUES (6,'GARFIELD','MANAGER',9,'1993-05-01',54000,NULL,4);
INSERT INTO employees VALUES (7,'POLK','TECH',6,'1997-09-22',25000,NULL,4);
INSERT INTO employees VALUES (8,'GRANT','ENGINEER',10,'1997-03-30',32000,NULL,2);
INSERT INTO employees VALUES (9,'JACKSON','CEO',NULL,'1990-01-01',75000,NULL,4);
INSERT INTO employees VALUES (10,'FILLMORE','MANAGER',9,'1994-08-09',56000,NULL,2);
INSERT INTO employees VALUES (11,'ADAMS','ENGINEER',10,'1996-03-15',34000,NULL,2);
INSERT INTO employees VALUES (12,'WASHINGTON','ADMIN',6,'1998-04-16',18000,NULL,4);
INSERT INTO employees VALUES (13,'MONROE','ENGINEER',10,'2000-12-03',30000,NULL,2);
INSERT INTO employees VALUES (14,'ROOSEVELT','CPA',9,'1995-10-12',35000,NULL,1);
    `
// noerror();
// execute(create_db_employee + ';');

async function load_db_static(relative_file_path) {
    worker.postMessage({ action: 'open' });

    const u = new URL(`http://localhost:1313/${relative_file_path}`);
    fetch(u).then(res => res.arrayBuffer()).then(buf => {
        try {
            worker.postMessage({ action: 'open', 'buffer': buf }, [buf]);
        } catch (exception) {
            worker.postMessage({ action: 'open', 'buffer': buf });
        }
    });
}
load_db_static("sqljs/db/sql.db");
console.log();

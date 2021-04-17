"use strict";

function makeGUI() {
    let that = {};

    /**
     * The error notification system.
     */
    that.notifyError = function (error) {
        that._console_error(error);
        const message = error.message || error.reason.message || error;
        notie.alert({
            type: 'error',
            text: 'Erreur : ' + message,
            stay: false,
            time: 3,
            position: 'top',
        });
        // In case of error, force loader hiding.
        try {
            Basthon.Goodies.hideLoader();
        } catch (e) {}
    };

    /**
     * Initialize the GUI.
     */
    that.init = async function() {
        /* all errors redirected to notification system */
        const onerror = that.notifyError;
        window.addEventListener('error', onerror);
        window.addEventListener("unhandledrejection", onerror);
        /* console errors redirected to notification system */
        that._console_error = console.error;
        console.error = function() {
            onerror({message: String(arguments[0])});
        };
        
        /* state variables */
        that.initStateFromStorage('switched', false);
        that.initStateFromStorage('darkmode', true);

        /* update appearance from state variables */
        that.updateSwitchView();
        that.updateDarkLight();
        
        /* connecting buttons */
        // run
        let button = document.getElementById('run');
        button.addEventListener('click', that.runScript);
        // open
        button = document.getElementById("open");
        button.addEventListener("click", that.openFile);
        // download
        button = document.getElementById("download");
        button.addEventListener("click", that.download);
        // share
        button = document.getElementById("share");
        button.addEventListener("click", that.share);
        
        // raz
        button = document.getElementById('raz');
        button.addEventListener('click', that.restart);
        // show shell
        button = document.getElementById("btn_shell");
        button.addEventListener("click", that.showShell);
        // show graph
        button = document.getElementById("btn_graph_view");
        button.addEventListener("click", that.showGraph);
        // dark/light mode
        button = document.getElementById("darklight");
        button.addEventListener("click", that.switchDarkLight);
        // view switch
        button = document.getElementById("switch");
        button.addEventListener("click", that.switchView);
        // single/double vew
        button = document.getElementById("hide-console");
        button.addEventListener("click", that.hideConsole);
        button = document.getElementById("hide-editor");
        button.addEventListener("click", that.hideEditor);
        button = document.getElementById("show-editor-console");
        button.addEventListener("click", that.showEditorConsole);

        // initialise Basthon
        await that.basthonInit();
    };

    /**
     * Change loader text and call init function.
     * If catchError is false, in case of error, we continue the
     * init process, trying to do our best...
     */
    that.initCaller = async function (func, message, catchError) {
        Basthon.Goodies.setLoaderText(message);
        try {
            return await func();
        } catch (error) {
            if( !catchError ) throw error;
            that.notifyError(error);
        }
    };

    /**
     * Loading Basthon and connecting to events.
     */
    that.basthonInit = async function () {
        // loading Basthon (errors are fatal)
        await Basthon.Goodies.showLoader("Chargement de Basthon...", false);
        const init = that.initCaller;
        // loading shell
        await init(shell.init, "Chargement de la console...", true);
        // loading editor
        await init(editor.init, "Chargement de l'éditeur...", true);
        // loading graphics
        await init(graphics.init, "Chargement de la sortie graphique...", true);
        // loading aux files from URL
        await init(that.loadURLAux, "Chargement des fichiers auxiliaires...", true);
        // loading modules from URL
        await init(that.loadURLModules, "Chargement des modules annexes...", true);
        // end
        Basthon.Goodies.hideLoader();

        /* backup before closing */
        window.onbeforeunload = function () {
            editor.backup().catch(that.notifyError);
        };
    };

    /**
     * Load ressources from URL (common part to files and modules).
     */
    that._loadFromURL = async function (key, put) {
        const url = new URL(window.location.href);
        let promises = [];
        for( let fileURL of url.searchParams.getAll(key) ) {
            fileURL = decodeURIComponent(fileURL);
            const filename = fileURL.split('/').pop();
            let promise = Basthon.xhr({method: "GET",
                                       url: fileURL,
                                       responseType: "arraybuffer"});
            promise = promise.then(function (data) {
                return put(filename, data);
            }).catch(function () {
                throw {message: "Impossible de charger le fichier " + filename + ".",
                      name: "LoadingException"};
            });
            promises.push(promise);
        }
        await Promise.all(promises);
    };

    /**
     * Load auxiliary files submited via URL (aux= parameter) (async).
     */
    that.loadURLAux = function () {
        return that._loadFromURL('aux', Basthon.putFile.bind(Basthon));
    };

    /**
     * Load modules submited via URL (module= parameter) (async).
     */
    that.loadURLModules = function () {
        return that._loadFromURL('module', Basthon.putModule.bind(Basthon));
    };

    /**
     * Init a state variable from local storage (with default value).
     */
    that.initStateFromStorage = function(state, _default=false) {
        if( typeof(Storage) !== "undefined"
            && localStorage.getItem(state) !== null) {
            that[state] = localStorage.getItem(state) === "true";
        } else {
            that[state] = _default;
        }
    };

    /**
     * Save a state variable in local storage.
     */
    that.saveStateInStorage = function(state) {
        if (typeof(Storage) !== "undefined") {
            localStorage.setItem(state, that[state]);
        }
    };
    
    /**
     * Run the editor script in the shell.
     */
    that.runScript = function () {
        // backup the script just before running
        editor.backup().catch(that.notifyError);
        const src = editor.getValue();
        shell.launch(src, false);
        shell.focus();
    };
    
    /**
     * RAZ function.
     */
    that.restart = function () {
        Basthon.restart();
        shell.clear();
        graphics.clean();
    };

    /**
     * Loading file in the (emulated) local filesystem (async).
     */
    that.putFSRessource = function (file) {
        return new Promise(function (resolve, reject) {
            const reader = new FileReader();
            reader.readAsArrayBuffer(file);
            reader.onload = async function (event) {
                await Basthon.putRessource(file.name, event.target.result);
                notie.alert({
                    type: 'success',
                    text: file.name + " est maintenant utilisable depuis Python",
                    stay: false,
                    time: 3,
                    position: 'top'
                });
                resolve();
            };
            reader.onerror = reject;
        });
    };

    /**
     * Open file in editor.
     */
    that.openEditor = async function (file) {
        await editor.open(file);
        notie.alert({
            type: 'success',
            text: file.name + " est chargé dans l'éditeur",
            stay: false,
            time: 3,
            position: 'top'
        });
    };

    /**
     * Open *.py file by asking user what to do:
     * load in editor or put on (emulated) local filesystem.
     */
    that.openPythonFile = async function (file) {
        notie.confirm({
            text: "Que faire de " + file.name + " ?",
            submitText: "Charger dans l'éditeur",
            cancelText: "Installer le module",
            position: 'top',
            submitCallback: () => { that.openEditor(file); },
            cancelCallback: () => { that.putFSRessource(file); }
        });
    };

    /**
     * Opening file: If it has .py extension, loading it in the editor
     * or put on (emulated) local filesystem (user is asked to),
     * otherwise, loading it in the local filesystem.
     */
    that.openFile = function () {
        return new Promise(function (resolve, reject) {
            let input = document.createElement('input');
            input.type = 'file';
            input.style.display = "none";
            input.onchange = async function (event) {
                for( let file of event.target.files ) {
                    const ext = file.name.split('.').pop();
                    if(ext === 'py') {
                        await that.openPythonFile(file);
                    } else {
                        await that.putFSRessource(file);
                    }
                }
                resolve();
            };
            input.onerror = reject;

            document.body.appendChild(input);
            input.click();
            document.body.removeChild(input);
        });
    };

    /**
     * Download script in editor.
     */
    that.download = function () {
        editor.download("script.py");
    };
    
    /**
     * Displaying editor alone.
     */
    that.hideConsole = function () {
        let button = document.getElementById("hide-console");
        button.style.display = "none";
        button = document.getElementById("hide-editor");
        button.style.display = "";
        let elt = document.getElementById("right-div");
        elt.style.display = "none";
        elt = document.getElementById("left-div");
        elt.style.display = "";
        elt.style.width = "100%";
    };
    
    /**
     * Displaying console alone.
     */
    that.hideEditor = function () {
        let button = document.getElementById("hide-editor");
        button.style.display = "none";
        button = document.getElementById("show-editor-console");
        button.style.display = "";
        let elt = document.getElementById("left-div");
        elt.style.display = "none";
        elt = document.getElementById("right-div");
        elt.style.display = "";
        elt.style.width = "100%";
    };
    
    /**
     * Editor and console side by side.
     */
    that.showEditorConsole = function () {
        let button = document.getElementById("show-editor-console");
        button.style.display = "none";
        button = document.getElementById("hide-console");
        button.style.display = "";
        let elt = document.getElementById("left-div");
        elt.style.display = "";
        elt.style.width = "50%";
        elt = document.getElementById("right-div");
        elt.style.display = "";
        elt.style.width = "48%";
    };
    
    /**
     * Update switch view.
     */
    that.updateSwitchView = function () {
        let div_left = document.getElementById("left-div");
        let div_right = document.getElementById("right-div");
        
        if(that.switched) {
            div_left.style.cssFloat = "right";
            div_right.style.cssFloat = "left";
        } else {
            div_left.style.cssFloat = "left";
            div_right.style.cssFloat = "right";
        }
    };
    
    /**
     * Switching side view.
     */
    that.switchView = function () {
        that.switched = !that.switched;
        that.updateSwitchView();
        that.saveStateInStorage('switched');
    };

    /**
     * Update dark/light appearence.
     */
    that.updateDarkLight = function () {
        const elements = document.getElementsByClassName("darklighted");
        const func = that.darkmode ? 'remove' : 'add';
        for( const e of elements) e.classList[func]("light");
        const theme = that.darkmode ? "monokai" : "xcode";
        editor.setTheme(`ace/theme/${theme}`);
    };

    /**
     * Switch dark/light mode.
     */
    that.switchDarkLight = function () {
        that.darkmode = !that.darkmode;
        that.saveStateInStorage('darkmode');
        that.updateDarkLight();
    };

    /**
     * Get mode as a string (dark/light).
     */
    that.theme = function () {
        return that.darkmode ? "dark" : "light";
    };
    
    /**
     * Toggle hide/show shell/graph.
     */
    that.showShell = function () {
        shell.style.display = "block";
        graphics.style.display = "none";
    };

    /**
     * Toggle hide/show shell/graph.
     */
    that.showGraph = function () {
        shell.style.display = "none";
        graphics.style.display = "flex";
    }; 
    
    /**
     * Share script via URL.
     */
    that.share = function () {
        const url = editor.sharingURL();
        notie.confirm({
            text: document.getElementById("share_message").innerHTML,
            submitText: "Copier dans le presse-papier",
            cancelText: "Tester le lien",
            position: 'top',
            submitCallback: function() { that.copyToClipboard(url); },
            cancelCallback: function() {
                let anchor = document.createElement("a");
                anchor.href = url;
                anchor.target = "_blank";
                anchor.style.display = "none"; // just to be safe!
                document.body.appendChild(anchor);
                anchor.click();
                document.body.removeChild(anchor);
            }
        });
    };
    
    /**
     * Copy a text to clipboard.
     */
    that.copyToClipboard = function (text) {
        let textArea = document.createElement("textarea");
        
        // Precautions from https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript
        
        // Place in top-left corner of screen regardless of scroll position.
        textArea.style.position = 'fixed';
        textArea.style.top = 0;
        textArea.style.left = 0;
        
        // Ensure it has a small width and height. Setting to 1px / 1em
        // doesn't work as this gives a negative w/h on some browsers.
        textArea.style.width = '2em';
        textArea.style.height = '2em';
        
        // We don't need padding, reducing the size if it does flash render.
        textArea.style.padding = 0;
        
        // Clean up any borders.
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';
        
        // Avoid flash of white box if rendered for any reason.
        textArea.style.background = 'transparent';
        
        
        textArea.value = text;
        
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {
            let successful = document.execCommand('copy');
            let msg = successful ? 'successful' : 'unsuccessful';
            console.log('Copying text command was ' + msg);
        } catch (err) {
            console.log('Oops, unable to copy');
        }
        
        document.body.removeChild(textArea);
    };
    
    return that;
}

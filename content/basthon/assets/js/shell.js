"use strict";

function makeShell() {
    let that = document.getElementById("shell");
    
    /**
     * Common Python prompt.
     */
    that.ps1 = ">>> ";
    
    /**
     * Common Python newline in block.
     */
    that.ps2 = "... ";

    /**
     * Mimic CPython's REPL banner.
     */
    that.banner = function () {
        return Basthon.banner().replace("on WebAssembly VM", "");
    };

    /**
     * A buffer to handle multiline shell input.
     */
    that.buffer = [];

    /**
     * Reset the multiline input buffer.
     */
    that.reset_buffer = function () {
        that.buffer = [];
    };

    /**
     * Initialize the shell.
     */
    that.init = async function () {
        // just to be safe
        that.reset_buffer();
        
        function interpreter(command) {
            that.buffer.push(command);
            const source = that.buffer.join('\n');
            if( Basthon.more(source) ) {
                that.term.set_prompt(that.ps2);
            } else {
                that.term.set_prompt(that.ps1);
                that.reset_buffer();
                that.launch(source, true);
            }
        }

        that.term = $('#shell').terminal(
            interpreter,
            {
                greetings: that.banner(),
                prompt: that.ps1,
                completionEscape: false,
                completion: function(command, callback) {
                    callback(Basthon.complete(command)[0]);
                },
            }
        );
        // this prevents JQuery Terminal to redraw terminal and remove
        // script wrapping feature
        that.term.resize = () => {};


        /* Event connections */
        Basthon.addEventListener("eval.finished", function (data) {
            if( data.interactive && "result" in data ) {
                that.echo(data.result["text/plain"] + '\n');
            }
            that.wakeup();
        });

        Basthon.addEventListener("eval.output", function (data) {
            switch(data.stream) {
            case "stdout":
                that.echo(data.content);
                break;
            case "stderr":
                that.error(data.content);
                break;
            }
        });

        Basthon.addEventListener("eval.error", function (data) {
            that.wakeup();
        });
    };

    /**
     * Print a string in the shell.
     */
    that.echo = function (message) {
        // JQuery.terminal adds a trailing newline that is not easy
        // to remove with the current API. Doing our best here.

        message = message.toString();

        // prompt can be polluted with previous echo
        // _prompt_tail is the line part just before the prompt
        const term = that.term;
        term._prompt_tail = term._prompt_tail || '';
        let prompt = term.get_prompt();
        if( prompt.startsWith(term._prompt_tail) )
            prompt = prompt.slice(term._prompt_tail.length);
        else
            term._prompt_tail = '';
        // here, prompt and _prompt_tail should be correctly isolated
        const lines = message.split('\n');
        lines[0] = term._prompt_tail + lines[0];
        term._prompt_tail = lines.pop();
        term.set_prompt(term._prompt_tail + prompt);
        if( lines.length )
            term.echo(lines.join('\n'));
    };

    /**
     * Print error in shell (in red).
     */
    that.error = function (message) {
        // JQuery.terminal adds a trailing newline that is not easy
        // to remove with the current API. Doing our best here.
        message = message.toString();
        return that.term.error(message.replace(/\n+$/, ""));
    };

    /**
     * Pause the shell execution (usefull to wait for event or promise).
     */
    that.pause = function () {
        that.term.pause();
    };

    /**
     * Resume the shell execution (see `pause`).
     */
    that.wakeup = function () {
        that.term.resume();
    };

    /**
     * Recover the shell as it was at start.
     */
    that.clear = function () {
        that.term.clear();
        that.echo(that.banner() + "\n");
        that.reset_buffer();
    };

    /**
     * Show script in shell with content as dropdown
     * (should improve readability).
     */
    that.showScript = function (code) {
        code = `# script executed\n${code}`;
        let script = `${that.ps1}`;
        script += code.split('\n').join(`\n${that.ps2}`);
        script += '\n';
        that.echo(script);
        const output = that.querySelector(".terminal-output").lastChild;
        const header = output.firstChild;
        header.classList.add("exec-script-header");
        for( const e of header.children )
            e.style.backgroundColor = "inherit";
        function hideShow() {
            const converter = {"none": "block", "": "none", "block": "none"};
            for( const e of output.childNodes )
                if( e !== header )
                    e.style.display = converter[e.style.display];
        }
        header.addEventListener("click", hideShow);
        hideShow();
    };

    /**
     * Launch code in shell.
     */
    that.launch = function (code, interactive=true) {
        if( !interactive )
            that.showScript(code);
        that.pause();
        Basthon.dispatchEvent("eval.request", {code: code,
                                               interactive: interactive});
    };
    
    return that;
}

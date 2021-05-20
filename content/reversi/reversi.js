
let wasm;

let cachedTextDecoder = new TextDecoder('utf-8', { ignoreBOM: true, fatal: true });

cachedTextDecoder.decode();

let cachegetUint8Memory0 = null;
function getUint8Memory0() {
    if (cachegetUint8Memory0 === null || cachegetUint8Memory0.buffer !== wasm.memory.buffer) {
        cachegetUint8Memory0 = new Uint8Array(wasm.memory.buffer);
    }
    return cachegetUint8Memory0;
}

function getStringFromWasm0(ptr, len) {
    return cachedTextDecoder.decode(getUint8Memory0().subarray(ptr, ptr + len));
}

const heap = new Array(32).fill(undefined);

heap.push(undefined, null, true, false);

let heap_next = heap.length;

function addHeapObject(obj) {
    if (heap_next === heap.length) heap.push(heap.length + 1);
    const idx = heap_next;
    heap_next = heap[idx];

    heap[idx] = obj;
    return idx;
}

function getObject(idx) { return heap[idx]; }

function dropObject(idx) {
    if (idx < 36) return;
    heap[idx] = heap_next;
    heap_next = idx;
}

function takeObject(idx) {
    const ret = getObject(idx);
    dropObject(idx);
    return ret;
}
/**
*/
export const Player = Object.freeze({ Human:0,"0":"Human",Computer:1,"1":"Computer", });
/**
*/
export class WasmGame {

    static __wrap(ptr) {
        const obj = Object.create(WasmGame.prototype);
        obj.ptr = ptr;

        return obj;
    }

    __destroy_into_raw() {
        const ptr = this.ptr;
        this.ptr = 0;

        return ptr;
    }

    free() {
        const ptr = this.__destroy_into_raw();
        wasm.__wbg_wasmgame_free(ptr);
    }
    /**
    * @returns {WasmGame}
    */
    static create_game() {
        var ret = wasm.wasmgame_create_game();
        return WasmGame.__wrap(ret);
    }
    /**
    */
    new_game() {
        wasm.wasmgame_new_game(this.ptr);
    }
    /**
    * @returns {boolean}
    */
    is_finished() {
        var ret = wasm.wasmgame_is_finished(this.ptr);
        return ret !== 0;
    }
    /**
    * @returns {Array<any>}
    */
    grid() {
        var ret = wasm.wasmgame_grid(this.ptr);
        return takeObject(ret);
    }
    /**
    * @returns {Array<any>}
    */
    playables() {
        var ret = wasm.wasmgame_playables(this.ptr);
        return takeObject(ret);
    }
    /**
    * @param {number} x
    * @param {number} y
    * @returns {boolean}
    */
    play(x, y) {
        var ret = wasm.wasmgame_play(this.ptr, x, y);
        return ret !== 0;
    }
    /**
    */
    unplay() {
        wasm.wasmgame_unplay(this.ptr);
    }
    /**
    */
    switch() {
        wasm.wasmgame_switch(this.ptr);
    }
    /**
    * @returns {boolean}
    */
    is_human_turn() {
        var ret = wasm.wasmgame_is_human_turn(this.ptr);
        return ret !== 0;
    }
    /**
    * -1 : not finished
    * 0  : draw
    * 1  : black
    * 2  : white
    * @returns {number}
    */
    winner() {
        var ret = wasm.wasmgame_winner(this.ptr);
        return ret;
    }
    /**
    * @returns {Array<any>}
    */
    count() {
        var ret = wasm.wasmgame_count(this.ptr);
        return takeObject(ret);
    }
    /**
    * @returns {boolean}
    */
    is_black_human() {
        var ret = wasm.wasmgame_is_black_human(this.ptr);
        return ret !== 0;
    }
    /**
    * @returns {boolean}
    */
    is_white_human() {
        var ret = wasm.wasmgame_is_white_human(this.ptr);
        return ret !== 0;
    }
    /**
    * @param {number} depth
    * @returns {Array<any>}
    */
    ask_computer_to_play(depth) {
        var ret = wasm.wasmgame_ask_computer_to_play(this.ptr, depth);
        return takeObject(ret);
    }
}

async function load(module, imports) {
    if (typeof Response === 'function' && module instanceof Response) {
        if (typeof WebAssembly.instantiateStreaming === 'function') {
            try {
                return await WebAssembly.instantiateStreaming(module, imports);

            } catch (e) {
                if (module.headers.get('Content-Type') != 'application/wasm') {
                    console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n", e);

                } else {
                    throw e;
                }
            }
        }

        const bytes = await module.arrayBuffer();
        return await WebAssembly.instantiate(bytes, imports);

    } else {
        const instance = await WebAssembly.instantiate(module, imports);

        if (instance instanceof WebAssembly.Instance) {
            return { instance, module };

        } else {
            return instance;
        }
    }
}

async function init(input) {
    if (typeof input === 'undefined') {
        input = new URL('reversi_bg.wasm', import.meta.url);
    }
    const imports = {};
    imports.wbg = {};
    imports.wbg.__wbindgen_string_new = function(arg0, arg1) {
        var ret = getStringFromWasm0(arg0, arg1);
        return addHeapObject(ret);
    };
    imports.wbg.__wbindgen_object_drop_ref = function(arg0) {
        takeObject(arg0);
    };
    imports.wbg.__wbindgen_number_new = function(arg0) {
        var ret = arg0;
        return addHeapObject(ret);
    };
    imports.wbg.__wbg_log_9a99fb1af846153b = function(arg0) {
        console.log(getObject(arg0));
    };
    imports.wbg.__wbg_new_515b65a8e7699d00 = function() {
        var ret = new Array();
        return addHeapObject(ret);
    };
    imports.wbg.__wbg_push_b7f68478f81d358b = function(arg0, arg1) {
        var ret = getObject(arg0).push(getObject(arg1));
        return ret;
    };
    imports.wbg.__wbindgen_throw = function(arg0, arg1) {
        throw new Error(getStringFromWasm0(arg0, arg1));
    };

    if (typeof input === 'string' || (typeof Request === 'function' && input instanceof Request) || (typeof URL === 'function' && input instanceof URL)) {
        input = fetch(input);
    }



    const { instance, module } = await load(await input, imports);

    wasm = instance.exports;
    init.__wbindgen_wasm_module = module;

    return wasm;
}

export default init;


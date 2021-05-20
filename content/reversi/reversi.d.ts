/* tslint:disable */
/* eslint-disable */
/**
*/
export enum Player {
  Human,
  Computer,
}
/**
*/
export class WasmGame {
  free(): void;
/**
* @returns {WasmGame}
*/
  static create_game(): WasmGame;
/**
*/
  new_game(): void;
/**
* @returns {boolean}
*/
  is_finished(): boolean;
/**
* @returns {Array<any>}
*/
  grid(): Array<any>;
/**
* @returns {Array<any>}
*/
  playables(): Array<any>;
/**
* @param {number} x
* @param {number} y
* @returns {boolean}
*/
  play(x: number, y: number): boolean;
/**
*/
  unplay(): void;
/**
*/
  switch(): void;
/**
* @returns {boolean}
*/
  is_human_turn(): boolean;
/**
* -1 : not finished
* 0  : draw
* 1  : black
* 2  : white
* @returns {number}
*/
  winner(): number;
/**
* @returns {Array<any>}
*/
  count(): Array<any>;
/**
* @returns {boolean}
*/
  is_black_human(): boolean;
/**
* @returns {boolean}
*/
  is_white_human(): boolean;
/**
* @param {number} depth
* @returns {Array<any>}
*/
  ask_computer_to_play(depth: number): Array<any>;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly __wbg_wasmgame_free: (a: number) => void;
  readonly wasmgame_create_game: () => number;
  readonly wasmgame_new_game: (a: number) => void;
  readonly wasmgame_is_finished: (a: number) => number;
  readonly wasmgame_grid: (a: number) => number;
  readonly wasmgame_playables: (a: number) => number;
  readonly wasmgame_play: (a: number, b: number, c: number) => number;
  readonly wasmgame_unplay: (a: number) => void;
  readonly wasmgame_switch: (a: number) => void;
  readonly wasmgame_is_human_turn: (a: number) => number;
  readonly wasmgame_winner: (a: number) => number;
  readonly wasmgame_count: (a: number) => number;
  readonly wasmgame_is_black_human: (a: number) => number;
  readonly wasmgame_is_white_human: (a: number) => number;
  readonly wasmgame_ask_computer_to_play: (a: number, b: number) => number;
}

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {InitInput | Promise<InitInput>} module_or_path
*
* @returns {Promise<InitOutput>}
*/
export default function init (module_or_path?: InitInput | Promise<InitInput>): Promise<InitOutput>;

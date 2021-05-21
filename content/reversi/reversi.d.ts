/* tslint:disable */
/* eslint-disable */
/**
* Types of players : human or computer
*/
export enum Player {
  Human,
  Computer,
}
/**
* Holds a game shared through bindgem/
* It uses a game and two players.
*/
export class WasmGame {
  free(): void;
/**
* Rerturns a new wasmgame.
* @returns {WasmGame}
*/
  static create_game(): WasmGame;
/**
* Reset the game without changing the players.
*/
  new_game(): void;
/**
* True iff the game is over.
* @returns {boolean}
*/
  is_finished(): boolean;
/**
* binder for wasmgame. Returns a Js readable grid.
* @returns {Array<any>}
*/
  grid(): Array<any>;
/**
* binder for wasmgame. Returns a Js readable array of playable moves.
* @returns {Array<any>}
*/
  playables(): Array<any>;
/**
* Ask the game to play a move and returns `true` if the move was played.
* @param {number} x
* @param {number} y
* @returns {boolean}
*/
  play(x: number, y: number): boolean;
/**
* Ask the game to reset the position untill the human can play.
*/
  unplay(): void;
/**
* Switch the players (human <> computer)
*/
  switch(): void;
/**
* `true` iff it's human's turn.
* @returns {boolean}
*/
  is_human_turn(): boolean;
/**
* Result of the game.
* -1 : not finished
* 0  : draw
* 1  : black
* 2  : white
* @returns {number}
*/
  winner(): number;
/**
* Returns a Js readable array with the counts of black and white.
* @returns {Array<any>}
*/
  count(): Array<any>;
/**
* `true` iff black is the human player
* @returns {boolean}
*/
  is_black_human(): boolean;
/**
* `true` iff white is the human player.
* @returns {boolean}
*/
  is_white_human(): boolean;
/**
* Ask the computer to play a move. Returns an empty array if it wasn't
* possible and the move in a Js readable array if a move was played.
* log some info in browser console for easier debugging.
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

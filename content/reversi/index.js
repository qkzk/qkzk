import init, { WasmGame } from "./reversi.js";

/*
  create board
*/
var board_matrix = jsboard.board({
    attach:"game",
    size:"8x8",
    style:"checkerboard",
    stylePattern: ["#349306","#349306"]
});

/*
  setup pieces
*/
var empty = jsboard.piece({text:"E", });
var white = jsboard.piece({text:"W", background:"#FFF"});
var black = jsboard.piece({text:"B", background:"#000"});

/*
  returns an empty grid
*/
const initBoard = () => {
  let board = [];
  for (var i = 0; i < 8; i++){
    board.push([]);
    for (var j = 0; j < 8; j++){
      board[i].push({"piece":empty.clone(), "pos":[i, j] });
    }
  }
  return board
}


/*
  Runs a game of reversi
*/
const reversi = () => {


  /*
    Called when the player press a cell in the game.
  */
  const addPiece = (piece) => {
    if (game.is_human_turn()) {
      let humanPlayedMove = board_matrix.cell(piece.parentNode).where();
      let isMovePlayed = game.play(humanPlayedMove[0], humanPlayedMove[1]);
      console.log("has your move have been played ?", isMovePlayed);
      if (!isMovePlayed) {
        return;
      }
      displayRefresh(game, board, humanPlayedMove);

      // stupid hack to force the display of human move --before-- calling for a computer move
      // doesn't even work on mobile :(
      setTimeout(() => {
        while (!game.is_human_turn() && !game.is_finished()) {
          let computerPlayedMove = game.ask_computer_to_play(difficulty);
          displayRefresh(game, board, computerPlayedMove);
        }
      }, 0);
    }
  };



  /*
    Attach the functions to their respective buttons above the board.
  */
  const topButtonsSetup = (game) => {
    let btnNewgame =   document.getElementById("button_newgame");
    let btnSwitch  =   document.getElementById("button_switch");
    let btnUnplay  =   document.getElementById("button_unplay");

    btnNewgame.addEventListener("click", function() {
      game.new_game();
      displayRefresh(game, board, []);
      computerPlayIfHisTurn(game);
    });

    btnSwitch.addEventListener("click", function() {
      game.switch();
      displayRefresh(game, board, []);
      computerPlayIfHisTurn(game);
    });


    btnUnplay.addEventListener("click", function() {
      game.unplay();
      displayRefresh(game, board, []);
    });
  };

  const computerPlayIfHisTurn = (game) => {
      let computer_played_move = game.ask_computer_to_play(difficulty);
      if (computer_played_move.length != 0) {
        displayRefresh(game, board, computer_played_move);
      }
  }

  /*
    Incremenant the difficulty up to 11 then set it back to 2.
  */
  const changeDifficulty = () => {
      difficulty += 1;
      if (difficulty >= 11) {
          difficulty = 2;
      }
      displayRefresh(game, board, []);
  }

  /*
    refresh the Status Buttons below the board.
  */
  const bottomButtonsRefresh = (game) => {
      let btnWhite = document.getElementById("btn_white");
      let btnBlack = document.getElementById("btn_black");
      let counts = game.count();
      if (game.is_white_human()) {
        setWhiteHumanButtons(btnWhite, btnBlack, counts);
      } else {
        setBlackHumanButtons(btnWhite, btnBlack, counts);
      }
  };

  /*
    Set the buttons for white and black when the whites are played by human.
  */
  const setWhiteHumanButtons = (btnWhite, btnBlack, counts) => {
      let whiteText = `Human - ${counts[1]}`;
      let blackText = `Computer (depth ${difficulty}) - ${counts[0]}`;
      btnBlack.addEventListener("click", changeDifficulty);
      btnWhite.addEventListener("click", () => {});
      btnWhite.innerText = whiteText;
      btnBlack.innerText = blackText;
  };

  /*
    Set the buttons for white and black when the blacks are played by human.
  */
  const setBlackHumanButtons = (btnWhite, btnBlack, counts) => {
      let whiteText = `Computer (depth ${difficulty}) - ${counts[1]}`;
      let blackText = `Human - ${counts[0]}`;
      btnWhite.addEventListener("click", changeDifficulty);
      btnBlack.addEventListener("click", () => {});
      btnWhite.innerText = whiteText;
      btnBlack.innerText = blackText;
  };

  /*
    Display the valid moves
    The moves are sent by pair in a flat array of coordinates : [x1, y1, x2, y2, ...]
  */
  const displayValidMoves = (board) => {
    let valid_moves = game.playables();
    let len = valid_moves.length;
    for (let i=0; i < len; i+=2) {
      let x = valid_moves[i];
      let y = valid_moves[i + 1];
      board[x][y]["piece"].classList.add("valid_moves");
    }
  };

  /*
    Display the board and refresh the status buttons.
  */
  const displayRefresh = (game, board, lastMove) => {
    let grid = game.grid();
    displayBoard(grid, board);
    bottomButtonsRefresh(game);
    if (game.is_human_turn()) {
        displayValidMoves(board);
    }
    if (lastMove.length === 2)  {
        board[lastMove[0]][lastMove[1]]["piece"].classList.add("last_move");
    }
  };

  /*
    Display the board
  */
  const displayBoard = (grid, board) => {
      grid.forEach((cell, index) => {
        attachPieceAndCallbackToCell(board, cell, index);
      });
  };

  /*
    Attach a piece to the cell, depending of his value.
    Attach a click event on every cell.
  */
  const attachPieceAndCallbackToCell = (board, cell, index) => {
    let i = index % 8;
    let j = (index / 8 | 0);
    insertPieceIntoCell(cell, board, i, j);
    insertCallbackIntoPiece(board, i, j);
  };

  /*
    Insert the correct piece (black, white, empty) into the cell.
  */
  const insertPieceIntoCell = (cell, board, i, j) => {
    switch (cell) {
      case 1:
        board[i][j]["piece"] = black.clone();
        break;
      case 2:
        board[i][j]["piece"] = white.clone();
        break;
      default:
        board[i][j]["piece"] = empty.clone();
    }
  };

  /*
    Insert the correct callback into the cell
  */
  const insertCallbackIntoPiece = (board, i, j) => {
    let piece = board[i][j]["piece"];
    board_matrix.cell(board[i][j]["pos"]).place(piece);
    board[i][j]["piece"].addEventListener("click", function() {
      addPiece(piece);
    });
  };

  // runs the game
  var difficulty = 7;
  var game = WasmGame.create_game();
  var board = initBoard();
  topButtonsSetup(game);
  displayRefresh(game, board, []);
};


/*
  Init wasm and starts the game.
*/
const runWasm = async () => {
  await init();
  reversi();
};

/*
  send a move to the game and returns true iff the move has been played.
*/
const sendMove = (game, x, y) => {
    let played = game.play(x, y);
    return played
};

runWasm();

import * as render from "../functions/Render.functions.js";

const CHESS_COMPONENT = (function() {
  const CHESS = new Chess();
  const CHESSBOARD = ChessBoard('js-chessboard', CHESSBOARD_CONFIG);
  let _history = "";

  const 

  const _onDragStart = function(source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    // only pick up pieces for the side to move
    if (CHESS.game_over() === true ||
        (CHESS.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (CHESS.turn() === 'b' && piece.search(/^w/) !== -1)) {
      return false;
    }
  };

  const _onDrop = function(source, target) {
    // see if the move is legal
    let move = CHESS.move({
      from: source,
      to: target,
      promotion: 'q' // NOTE: always promote to a queen for example simplicity
    });
  
    // illegal move
    if (move === null) return 'snapback';
  
    // renderCurrentFen() - call
    render.renderCurrentFEN(CHESS.fen());
  };

  const _onSnapEnd = function() {
    CHESSBOARD.position(CHESS.fen());
  };

  // const _updateChessboardStatus = function() {
  //   let status = '';
  
  //   let moveColor = 'White';
  //   if (CHESS.turn() === 'b') {
  //     moveColor = 'Black';
  //   }
  
  //   // checkmate?
  //   if (CHESS.in_checkmate() === true) {
  //     status = 'Game over, ' + moveColor + ' is in checkmate.';
  //   }
  
  //   // draw?
  //   else if (CHESS.in_draw() === true) {
  //     status = 'Game over, drawn position';
  //   }
  
  //   // game still on
  //   else {
  //     status = moveColor + ' to move';
  
  //     // check?
  //     if (CHESS.in_check() === true) {
  //       status += ', ' + moveColor + ' is in check';
  //     }
  //   }
  // };

  const CHESSBOARD_CONFIG = {
    draggable: true,
    position: 'start',
    onDragStart: _onDragStart,
    onDrop: _onDrop,
    onSnapEnd: _onSnapEnd
  };
  
  return {
    // instance of chess.js
    CHESS,
    // instance of chessboard.js
    CHESSBOARD
  }
})();

export default CHESS_COMPONENT;
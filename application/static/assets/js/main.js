// global array with the strategy names
let strategies = [];
// global array with the strategies details
let strategiesDetails = [];
// current fen of the chessboard
let currentFEN;

// on document load using jQuery
$( document ).ready( function () {
  // Init chessboard element
  const chessboard = ChessBoard('js-chessboard', {
    draggable: true,
    dropOffBoard: 'snapback'
  });

  chessboard.start();

  // getStrategies() - call

  // renderStrategiesDetails( strategiesDetails ) - call
});

// getStrategies()

// renderStrategiesDetails( strategiesDetails )

// getSuggestedMoves( strategies )

// renderSuggestedMoves( suggestedMoves )

// setChessboardFen()
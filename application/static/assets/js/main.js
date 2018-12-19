import * as async from "./functions/Async.functions.js";
import * as clientLogic from "./functions/Client-logic.functions.js";
import CHESS_COMPONENT from "./components/Chess.component.js";

$(document).ready(function () {
  // init chessboard element
  CHESS_COMPONENT.CHESSBOARD.start();

  // init popover here
    var fenDetails = $('#fen-details').html();
    $('#js-fen-textarea').popover({
        placement: "bottom",
        trigger: "focus",
        content: fenDetails,
        html: true
    });
  // get strategies from the server
  async.getStrategies();
});

// Event Listeners

// flip button for the orientation of chessboard
const flipBtn = document.getElementById('js-flip-chessboard');
flipBtn.addEventListener('click', CHESS_COMPONENT.CHESSBOARD.flip);
// submit button for the .fen-loader component
const submitFenBtn = document.getElementById('js-fen-submit');
submitFenBtn.addEventListener('click', clientLogic.setChessboardFen);
// getMoves button for the .suggested-moves component
const getMovesBtn = document.getElementById('js-get-moves');
getMovesBtn.addEventListener('click', async.getSuggestedMoves);

//Help center
const helpTrigger = document.getElementById('js-help-trigger');
const closeHelpTrigger = document.getElementById('js-close-help'); 

helpTrigger.addEventListener('click', toggleHelp);
closeHelpTrigger.addEventListener('click', toggleHelp);

function toggleHelp() {
	const helpEl = document.getElementById('js-help')
	helpEl.classList.toggle('in-view');
}
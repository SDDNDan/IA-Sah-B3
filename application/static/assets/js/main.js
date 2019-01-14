import * as async from "./functions/Async.functions.js";
import * as clientLogic from "./functions/Client-logic.functions.js";
import CHESS_COMPONENT from "./components/Chess.component.js";
import * as renderer from "./functions/Render.functions.js";

$(document).ready(function () {
  // init chessboard element
  CHESS_COMPONENT.CHESSBOARD.start();

  // init popover here
  let fenDetails = $('#js-fen-details').html();

  $('#js-fen-textarea').popover({
      placement: "left",
      trigger: "focus",
      content: fenDetails,
      html: true
  });

  $('.copy-current-fen').popover({
    placement: 'top',
    trigger: 'hover'
  });

  // init clipboard.js
  const clipboard = new ClipboardJS('#js-copy-current-fen');
  clipboard.on('success', (e) => {
    const copyFenFeedback = document.querySelector('.current-fen > .feedback.bg-success');

    // make it visible
    copyFenFeedback.style.opacity = 1;
    copyFenFeedback.style.pointerEvents = 'auto';
    // hide it after a delay of 1.5s
    setTimeout( function () {
      copyFenFeedback.style = '';
    }, 3000);

    e.clearSelection();
  });

  // get strategies from the server
  async.getStrategies();

  renderer.renderCurrentFEN(CHESS_COMPONENT.CHESS.fen());

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

// toggleHelp open
const helpButtonOpen = document.getElementById('js-help-trigger');
helpButtonOpen.addEventListener('click', clientLogic.toggleHelp);

// toggleHelp close
const helpButtonClose = document.getElementById('js-close-help');
helpButtonClose.addEventListener('click', clientLogic.toggleHelp);

// toggleStrategiesDetails
const suggestedMovesContainer = document.getElementById('js-suggested-moves-container');
const strategyDetailsSectionEl = document.getElementById('js-strategies-details-section');
const strategyDetailsClose = document.getElementById('js-close-strategies-details');

suggestedMovesContainer.addEventListener('click', (e) => {
  // show only the clicked strategy's details
  clientLogic.toggleStrategyDetails( e.target );
  // toggle the .strategies-details
  // only if it isn't already in view
  if( !strategyDetailsSectionEl.classList.contains('in-view') ) {
    strategyDetailsSectionEl.classList.toggle('in-view');
  }
});

strategyDetailsClose.addEventListener('click', () => strategyDetailsSectionEl.classList.toggle('in-view') );

// toggle between fen and match input
const fenMatchSwitchBtn = document.getElementById('js-switch-fen-match');
const fenLoader = document.getElementById('js-fen-loader');
const matchLoader = document.getElementById('js-match-loader');

fenMatchSwitchBtn.addEventListener('click', () => {
  fenMatchSwitchBtn.innerHTML === 'Switch to match input' ? fenMatchSwitchBtn.innerHTML = 'Switch to FEN input'
    : fenMatchSwitchBtn.innerHTML = 'Switch to match input';
  fenLoader.classList.toggle('in-view');
  matchLoader.classList.toggle('in-view');
});


// match input submit button
// const matchInputSubmitBtn = document.getElementById('js-match-submit');
// let matchHistory = [];
// matchInputSubmitBtn.addEventListener('click', () => {
//   const matchTextarea = document.getElementById('js-match-textarea');
//   let match = matchTextarea.value;

//   matchHistory = clientLogic.chunkString(match, 4);
//   // console.log(matchHistory);
//   async.getMatchCommentary( match );
// });

// 
const matchSubmitBtn = document.getElementById('js-match-submit');
matchSubmitBtn.addEventListener('click', () => {
    let matchCommentary = async.getCommentary();
});

// copy current fen
const copyCurrentFenBtn = document.getElementById('js-copy-current-fen');
copyCurrentFenBtn.addEventListener('click', clientLogic.copyCurrentFen);

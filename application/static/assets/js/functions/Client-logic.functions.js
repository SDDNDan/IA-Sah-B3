import CHESS_COMPONENT from "../components/Chess.component.js";

/* ********Client-side logic functions******** */

export function setChessboardFen() {
  // grab the textarea from the .fen-loader component
  const fenTextarea = document.getElementById('js-fen-textarea');
  // element that displays an error if 
  // a non-FEN string is entered in the textarea
  const fenFeedback = document.querySelector('.fen-loader ~ .fen-feedback');
  // get the value of the textarea
  const fen = fenTextarea.value;
  
  // check if fen is valid
  if( parseFEN(fen) ) {
    // update currentFen global
    // currentFEN = fen;
    CHESS_COMPONENT.CHESSBOARD.position(fen);
    CHESS_COMPONENT.CHESS.load(fen);
  } else {
    let validationResult = CHESS_COMPONENT.CHESS.validate_fen(fen);
    $(fenFeedback).html(validationResult.error);
    // make it visible
    fenFeedback.style.opacity = 1;
    // hide it after a delay of 1.5s
    setTimeout( function () {
      fenFeedback.style = '';
    }, 3000);
  }
}

//Help center
export function toggleHelp() {
	const helpEl = document.getElementById('js-help')
	helpEl.classList.toggle('in-view');
}

export function toggleStrategyDetails( eventTarget ) {
  // get parent of the cards
  // containing the strategies details
  let cardsParent = $( "#js-strategies-details .container-fluid .row .col-12" );
  // hide all the cards
  $.each(cardsParent.children(), (index, child) => child.style.opacity = 0);

  console.log(eventTarget.tagName);
  // if( eventTarget.parentElement.getAttribute('data-strategy-name') || eventTarget.getAttribute('data-strategy-name') ) {
  //   cardsParent.children().closest('[data-strategy-name]')
  // }
}

// https://stackoverflow.com/questions/7033639/split-large-string-in-n-size-chunks-in-javascript
export function chunkString(str, length) {
  return str.match(new RegExp('.{1,' + length + '}', 'g'));
}

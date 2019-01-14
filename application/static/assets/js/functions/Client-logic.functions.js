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
  let cardsParent = $( '#js-strategies-details .container-fluid .row .col-12' );
  // hide all the cards
  $.each(cardsParent.children(), (index, child) => child.style.opacity = 0);

  // get the data attribute value
  // of the clicked strategy
  const detailsToShow = $( eventTarget ).closest('[data-strategy-name]').data('strategy-name');
  // show only the clicked strategy's details
  cardsParent.find(`[data-strategy-name="${detailsToShow}"]`).css({ opacity: 1 });
}

// https://stackoverflow.com/questions/7033639/split-large-string-in-n-size-chunks-in-javascript
export function chunkString(str, length) {
  return str.match(new RegExp('.{1,' + length + '}', 'g'));
}

// copy current fen to clipboard
export function copyCurrentFen() {
  const currentFen = document.querySelector('.border.border-info');
  const copyFenFeedback = document.querySelector('.current-fen > .feedback.bg-success');

  // https://stackoverflow.com/questions/36639681/how-to-copy-text-from-a-div-to-clipboard
  if (document.selection) { 
    let range = document.body.createTextRange();
    range.moveToElementText(currentFen);
    range.select().createTextRange();
    document.execCommand("copy"); 
  } else if (window.getSelection) {
      let range = document.createRange();
      range.selectNode(currentFen);
      window.getSelection().addRange(range);
      document.execCommand("copy");
  }

  // make it visible
  copyFenFeedback.style.opacity = 1;
  copyFenFeedback.style.pointerEvents = 'auto';
  // hide it after a delay of 1.5s
  setTimeout( function () {
    copyFenFeedback.style = '';
  }, 3000);
}
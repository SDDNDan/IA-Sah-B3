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
    CHESS_COMPONENT.history = "";
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
  // let cardsParent = $( '#js-strategies-details .container-fluid .row .col-12' );
  let cardsParent = document.querySelector("#js-strategies-details .container-fluid .row .col-12");
  // hide all the cards
  // $.each(cardsParent.children(), (index, child) => child.style.opacity = 0);
  const cards = Array.from(cardsParent.children);
  cards.forEach((card) => {
    card.style.opacity = 0;
  });

  // get the data attribute value
  // of the clicked strategy
  const detailsToShow = $( eventTarget ).closest('[data-strategy-name]').data('strategy-name');
  // const detailsToShow = eventTarget.dataset.strategyName;
  // console.log(detailsToShow);

  // show only the clicked strategy's details
  cardsParent.querySelector(`[data-strategy-name="${detailsToShow}"]`).style.opacity = 1;
  cardsParent.querySelector(`[data-strategy-name="${detailsToShow}"]`).style.pointerEvents = "auto";
}

// https://stackoverflow.com/questions/7033639/split-large-string-in-n-size-chunks-in-javascript
export function chunkString(str, length) {
  return str.match(new RegExp('.{1,' + length + '}', 'g'));
}

export function commentaryLinksEvents() {
  const moveLinks = document.querySelectorAll(`#js-commentary .commentary__line .commentary-text a.user-move,
    #js-commentary .commentary__line .commentary-text a.suggested-move`
  );

  const userMoves = Array.from(moveLinks).filter(link => link.classList.contains("user-move"));
  const suggestedMoves = Array.from(moveLinks).filter(link => link.classList.contains("suggested-move"));

  moveLinks.forEach( (link) => {
    link.addEventListener('click', () => {
      let fen = link.dataset.fen;

      if( parseFEN(fen) ) {
        CHESS_COMPONENT.CHESSBOARD.position(fen);
        CHESS_COMPONENT.CHESS.load(fen);
      } else {
        console.log("Error with fen", fen);
      }
    });
  });

  suggestedMoves.forEach( (sMove) => {
    sMove.addEventListener("mouseenter", () => {
      highlightCommentMove(sMove, true, true);
    });

    sMove.addEventListener("mouseleave", () => {
      highlightCommentMove(sMove, false, true);
    });
  });

  userMoves.forEach( (uMove) => {
    uMove.addEventListener("mouseenter", () => {
      highlightCommentMove(uMove, true, false);
    });

    uMove.addEventListener("mouseleave", () => {
      highlightCommentMove(uMove, false, false);
    });
  });
}

export function highlightSuggestedMove( strategyName, onHover = true) {
  const chessboadContainer = document.getElementById("js-chessboard");
  const chessboardEl = chessboadContainer.querySelector(`div[class^="chessboard"] > div[class^="board"]`);
  const move = document.getElementById(`js-move-${strategyName}`).innerText;

  if ( move === "" ) {
    return
  } else {
    const fromTo = chunkString(move, 2);
    const fromSquareEl = chessboardEl.querySelector(`[data-square=${fromTo[0]}]`);
    const toSquareEl = chessboardEl.querySelector(`[data-square=${fromTo[1]}]`);

    if ( onHover ) {
      fromSquareEl.classList.add("highlight");
      toSquareEl.classList.add("highlight");
    } else {
      fromSquareEl.classList.remove("highlight");
      toSquareEl.classList.remove("highlight");
    }
  }
}

export function highlightCommentMove(el, onHover = true, suggested = true) {
  const chessboadContainer = document.getElementById("js-chessboard");
  const chessboardEl = chessboadContainer.querySelector(`div[class^="chessboard"] > div[class^="board"]`);

  if ( el.getAttribute("data-fen") !== CHESS_COMPONENT.CHESS.fen() ) {
    return
  } else {
    const move = el.dataset.move;
    const fromTo = chunkString(move, 2);
    const fromSquareEl = chessboardEl.querySelector(`[data-square=${fromTo[0]}]`);
    const toSquareEl = chessboardEl.querySelector(`[data-square=${fromTo[1]}]`);

    if ( onHover ) {
      if ( suggested ) {
        fromSquareEl.classList.add("highlight--s");
        toSquareEl.classList.add("highlight--s");
      } else {
        fromSquareEl.classList.add("highlight--u");
        toSquareEl.classList.add("highlight--u");
      }
    } else {
      if ( suggested ) {
        fromSquareEl.classList.remove("highlight--s");
        toSquareEl.classList.remove("highlight--s");
      } else {
        fromSquareEl.classList.remove("highlight--u");
        toSquareEl.classList.remove("highlight--u");
      }
    }
  }
}

export function clearSuggestedMoves() {
  const suggestedMovesContainer = document.getElementById("js-suggested-moves-container");
  const movesEls = suggestedMovesContainer.querySelectorAll(".strategy .strategy__move");
  const loaders = suggestedMovesContainer.querySelectorAll(".strategy .strategy__move + .lds-ellipsis");

  movesEls.forEach( (moveEl) => {
    moveEl.innerText = "";
    moveEl.style.opacity = 0;
  });

  loaders.forEach( (loader) => {
    if ( loader.classList.contains("in-view") ) {
      loader.classList.remove("in-view");
    }
  });
}
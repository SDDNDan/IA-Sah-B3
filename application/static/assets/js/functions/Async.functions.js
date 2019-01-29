import * as constants from "../utils/Constants.utils.js";
import * as render from "./Render.functions.js";
import * as clientLogic from "../functions/Client-logic.functions.js"
import CHESS_COMPONENT from "../components/Chess.component.js";

/* ********Async functions******** */

// array with the strategy names
export let strategies = [];

export function getStrategies() {
  const STRATEGIES_URL = '/strategies';
  $.getJSON( `${constants.BASE_URL}${STRATEGIES_URL}`, function( data ) {
    $.each(data, function (key, val) {
      if ("strategy" in val) {
        strategies.push(val.strategy);
      }
    });

    // render strategies details
    render.renderStrategiesDetails( data );
    render.renderSuggestedMovesMarkup( data );
  });
}

export function getSuggestedMoves() {
  let currentFEN = CHESS_COMPONENT.CHESS.fen();
  let url = `${constants.BASE_URL}/moves?fen=${currentFEN}&strategy=`;

  for (let i = 0; i < strategies.length; i++) {
    let strategyName = strategies[i];
    let moveEl = document.getElementById(`js-move-${strategyName}`);
    let loader = document.getElementById(`js-loader-${strategyName}`);
    // hide move element
    moveEl.style.opacity = 0;
    moveEl.innerText = "";

    if ( loader.classList.contains('in-view') ) {
      loader.classList.remove('in-view');
    }
    // show loader
    loader.classList.add('in-view');

    $.getJSON( `${url}${strategyName}`, function( data ) {
      let response = data[0];

      // hide loader
      loader.classList.remove('in-view');
      // show move element
      render.renderSuggestedMove(strategyName, response.move);
    });
  }
}

export function getCommentary( matchString ) {
  
  if( matchString !== "" ) {
    let commentaryEl = document.getElementById('js-commentary');
    let placeholder = commentaryEl.children[0];
  
    // hide placeholder text
    placeholder.style.display = 'none';
    commentaryEl.style.overflowY = 'scroll';

    let loader = document.querySelector('#js-commentary > .loader');
    
    if( loader.classList.contains('in-view') ) {
      loader.classList.remove('in-view');
    }

    // show loader
    loader.classList.toggle('in-view');

    $.ajax({
        url: constants.BASE_URL + '/commentary',
        type: "get",
        data: {
          game: matchString
        },
        success: function(response) {
            render.renderCommentary( response );

            // hide loader
            loader.classList.toggle('in-view');

            // add eventListeners for the moves
            // in the commentary
            clientLogic.commentaryLinksEvents();
        },
        error: function(error) {
          console.log('An error was encountered:', error);
        }
    });
  } else {
    console.log("Match input empty!", matchString);
  }
}
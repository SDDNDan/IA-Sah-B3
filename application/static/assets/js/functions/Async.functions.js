import * as constants from "../utils/Constants.utils.js";
import * as render from "./Render.functions.js";
import CHESS_COMPONENT from "../components/Chess.component.js";

/* ********Async functions******** */

// array with the strategy names
export let strategies = [];
// sugestedMoves array
export let suggestedMoves = [];

export function getStrategies() {
  const STRATEGIES_URL = '/strategies';
  $.getJSON(`${constants.BASE_URL}${STRATEGIES_URL}`, function (data) {
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

    if( loader.classList.contains('in-view') ) {
      loader.classList.remove('in-view');
    }
    // show loader
    loader.classList.toggle('in-view');

    $.getJSON(url + strategyName, function (data) {
      // ATM the response to the request has the form
      // [{strategy: ..., move: ...}]
      // It should be an object though
      let response = data[0];

      // suggestedMoves.push(response);
      // hide loader
      loader.classList.toggle('in-view');
      // show move element
      // moveEl.classList.toggle('in-view');
      render.renderSuggestedMove(strategyName, response.move);
    });
  }
}

// export function getMatchCommentary( match, matchHistory ) {
//   $.ajax({
//     type: 'GET',
//     url: `${constants.BASE_URL}/commentary?game=${match}`,
//     succes: data => {
//       data.forEach(element => {
//         if( element.length != 0 ) {
          
//         }
//       });
//     }
//   });
// }
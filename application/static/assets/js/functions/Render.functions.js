import * as markup from "./Markup.functions.js";
import * as clientLogic from "./Client-logic.functions.js";

/* ********render functions******** */

export function renderStrategiesDetails( strategiesResponse ) {
  // grab the strategies details container
  const strategiesDetails = document.getElementById('js-strategies-details');
  // navigate down to the .row descendant
  const container = strategiesDetails.children[1];
  const row = container.children[0];
  const col = row.children[0];

  strategiesResponse.forEach( strategyObj => {
    // .card
    let card = markup.createCardMarkup(strategyObj);

    // append .card to .col
    col.appendChild(card);
  });
}

export function renderSuggestedMovesMarkup( strategiesResponse ) {
  const suggestedMovesContainer = document.getElementById('js-suggested-moves-container');

  strategiesResponse.forEach( (strategy) => {
    let groupItem = markup.createListGroupItemMarkup( strategy );
    suggestedMovesContainer.appendChild( groupItem );
  });

  // highlight suggested move
  const strategyEls = suggestedMovesContainer.querySelectorAll(".strategy");

  strategyEls.forEach((strategyEl) => {
    strategyEl.addEventListener("mouseenter", () => {
      const strategyName = strategyEl.getAttribute("data-strategy-name");
      clientLogic.highlightSuggestedMove(strategyName);
    });
    
    strategyEl.addEventListener("mouseleave", () => {
      const strategyName = strategyEl.getAttribute("data-strategy-name");
      clientLogic.highlightSuggestedMove(strategyName, false);
    });
  });
}

export function renderSuggestedMove( strategyName, strategyMove ) {
  const moveEl = document.getElementById(`js-move-${strategyName}`);

  moveEl.innerText = strategyMove;
  moveEl.style.opacity = 1;
}

export function renderCurrentFEN( currentFEN ) {
    const fenContainer = document.getElementsByClassName('current-fen')[0];
    const width = document.getElementById('js-chessboard').firstChild.firstChild.style.width;
    const currentFenEl = document.getElementById('js-current-fen-value');

    fenContainer.width = width;
    currentFenEl.innerText = currentFEN;
}

export function renderCommentary( commentaryText ) {
  let commentary = JSON.parse(commentaryText);
  let commentaryEl = document.getElementById('js-commentary');

  jQuery.each(commentary, function(index, el) {
    if(el.length > 0 && el[0] !== "undefined") {
      let comment = markup.createCommentMarkup(el[0]);

      $(commentaryEl).append(comment);
    }
  });
}
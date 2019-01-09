import * as markup from "./Markup.functions.js";

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
}

export function renderSuggestedMove( strategyName, strategyMove ) {
  const moveEl = document.getElementById(`js-move-${strategyName}`);

  moveEl.innerText = strategyMove;
  moveEl.style.opacity = 1;
}

export function renderCurrentFEN( currentFEN ) {
    const fenContainer = document.getElementsByClassName(`current-fen`)[0];
    const width = document.getElementById('js-chessboard').firstChild.firstChild.style.width;

    fenContainer.width = width;
    fenContainer.getElementsByTagName("p")[0].innerHTML = currentFEN;
}
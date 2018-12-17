import * as markup from "./Markup.functions.js";

/* ********render functions******** */

export function renderStrategiesDetails( strategiesResponse ) {
  // grab the strategies details container
  const strategiesDetails = document.getElementById('js-strategies-details');
  // navigate down to the .row descendant
  const container = strategiesDetails.children[1];
  const row = container.children[0];

  strategiesResponse.forEach( strategy => {
    // .col element
    let col = document.createElement('div');
    col.classList = 'col-12 col-md-6 mb-3';

    // .card
    let card = markup.createCardMarkup(strategy);

    // append .card to .col
    col.appendChild(card);

    // append markup to the .row
    row.appendChild(col);
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
// global array with the strategy names
let strategies = [];
// global array with the strategies details
// let strategiesDetails = [];
// current fen of the chessboard
let currentFEN;

// todo: change accordingly when is necessary (ex: move project on an online server)
const BASE_URL = 'http://127.0.0.1:5000';

// on document load using jQuery
$( document ).ready( function () {
  // Init chessboard element
  const chessboard = ChessBoard('js-chessboard', {
    draggable: true,
    dropOffBoard: 'snapback'
  });

  chessboard.start();
  
  // get strategies from the server
  getStrategies();
});

function getStrategies() {
  const STRATEGIES_URL = '/strategies';
  $.getJSON( BASE_URL + STRATEGIES_URL, function( data ) {
    $.each( data, function( key, val ) {
        if("strategy" in val){
            strategies.push(val.strategy);
        }
    });
      
    // render strategies details
    renderStrategiesDetails( data );
  });
}

// renderStrategiesDetails( strategiesDetails )
function renderStrategiesDetails ( strategies ) {
  // grab the strategies details container
  const strategiesDetails = document.getElementById('js-strategies-details');
  // navigate down to the .row descendant
  const container = strategiesDetails.children[1];
  const row = container.children[0];

  strategies.forEach( strategy => {
    // .col element
   let col = document.createElement('div');
   col.classList = 'col-12 col-md-6 mb-3';

   // .card
   let card = createCardMarkup( strategy );

   // append .card to .col
   col.appendChild( card );

   // append markup to the .row
   row.appendChild( col );
 });
}

function createCardMarkup( strategyDetails ) {
  // Create Bootstrap card markup
  // https://getbootstrap.com/docs/4.1/components/card/#using-grid-markup
  // .card element
  let card = document.createElement('div');
  card.classList = 'card';

  // .card-body container
  let cardBody = document.createElement('div');
  cardBody.classList = 'card-body';

  // .card-title 
  let cardTitle = document.createElement('h2');
  cardTitle.classList = 'card-title';
  cardTitle.innerText = strategyDetails.strategy;

  // .card-text
  let cardText = document.createElement('p');
  cardText.classList = 'card-text';
  cardText.innerText = strategyDetails.description;

  // .btn.btn-primary link to documentation
  let link = document.createElement('a');
  link.classList = 'btn btn-primary';
  link.innerText = 'Documentation';
  link.href = strategyDetails.documentation;

  // append everything to .card-body
  cardBody.appendChild( cardTitle );
  cardBody.appendChild( cardText );
  cardBody.appendChild( link );

  // append .card-body to .card container
  card.appendChild( cardBody );

  return card;
}

// getSuggestedMoves( strategies )

// renderSuggestedMoves( suggestedMoves )

// setChessboardFen()
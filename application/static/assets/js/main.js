// global array with the strategy names
let strategies = [];
// global array with the strategies details
// let strategiesDetails = [];
// current fen of the chessboard
let currentFEN;

//sugestedMoves
let suggestedMoves = []

// todo: change accordingly when is necessary (ex: move project on an online server)
const BASE_URL = 'http://127.0.0.1:5000';

//Chessboard
const CHESSBOARD = ChessBoard('js-chessboard', {
  draggable: true,
  dropOffBoard: 'snapback'
});

$(document).ready(function () {
  //Init chessboard element
  CHESSBOARD.start();

  //get trategies from the server
  getStrategies();
});

function getStrategies() {
  const STRATEGIES_URL = '/strategies';
  $.getJSON(BASE_URL + STRATEGIES_URL, function (data) {
    $.each(data, function (key, val) {
      if ("strategy" in val) {
        strategies.push(val.strategy);
      }
    });

    // render strategies details
    renderStrategiesDetails( data );
    renderSuggestedMovesMarkup( data );
  });
}

function renderStrategiesDetails( strategiesResponse ) {
  // grab the strategies details container
  const strategiesDetails = document.getElementById('js-strategies-details');
  // navigate down to the .row descendant
  const container = strategiesDetails.children[1];
  const row = container.children[0];

  strategiesResponse.forEach(strategy => {
    // .col element
    let col = document.createElement('div');
    col.classList = 'col-12 col-md-6 mb-3';

    // .card
    let card = createCardMarkup(strategy);

    // append .card to .col
    col.appendChild(card);

    // append markup to the .row
    row.appendChild(col);
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
  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);
  cardBody.appendChild(link);

  // append .card-body to .card container
  card.appendChild(cardBody);

  return card;
}

function getSuggestedMoves() {

  myUrl = BASE_URL + "/moves?fen=" + "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" + "%20w%20KQkq%20-%200%201&strategy=";

  for (var i = 0; i < strategies.length; i++) {
    let strategyName = strategies[i];
    
    $.getJSON(myUrl + strategies[i], function (data) {
      $.each(data, function (key, val) {
        if ("strategy" in val) {
          let res = {
            strategy: val.strategy,
            move: val.move
          }

          suggestedMoves.push(res);
          renderSuggestedMove(strategyName, res.move);
        }
      });
    });
  }
}

function renderSuggestedMove( strategyName, strategyMove ) {
  const moveEl = document.getElementById(`js-move-${strategyName}`);

  moveEl.innerText = strategyMove;
  moveEl.style.opacity = 1;
}

function createListGroupItemMarkup( strategyDetails ) {
  // link
  let link = document.createElement('a');
  link.classList = 'list-group-item list-group-item-action strategy';

  // .container-fluid
  let container = document.createElement('div');
  container.classList = 'container-fluid';

  // .row
  let row = document.createElement('div');
  row.classList = 'row';
  
  // .strategy__info.col
  let strategyInfo = document.createElement('div');
  strategyInfo.classList = 'strategy__info col p-0';
  
  // strategy .name
  let strategyName = document.createElement('h5');
  strategyName.classList = 'mb-1 name';
  strategyName.innerText = strategyDetails.strategy;
  
  // strategy .desc
  let strategyDesc = document.createElement('p');
  strategyDesc.classList = 'mb-1 desc';
  strategyDesc.innerText = strategyDetails.description;

  // .col-2.align-self-center
  let col = document.createElement('div');
  col.classList = 'col-2 align-self-center';

  // .strategy-move
  let strategyMove = document.createElement('span');
  strategyMove.classList = 'alert alert-success strategy__move';
  strategyMove.id = `js-move-${strategyDetails.strategy}`;


  // append .name & .desc to .strategy__info
  strategyInfo.appendChild(strategyName);
  strategyInfo.appendChild(strategyDesc);

  // append .strategy-move to .col-2.align-self-center
  col.appendChild(strategyMove);
  
  // append .strategy__info & .col-2.align-self-cente
  // to .row
  row.appendChild(strategyInfo);
  row.appendChild(col);
  
  // append .row to .container-fluid
  container.appendChild(row);

  // append .container to link
  link.append(container);

  return link;
}

function renderSuggestedMovesMarkup( strategiesResponse ) {
  const suggestedMovesContainer = document.getElementById('js-suggested-moves-container');

  strategiesResponse.forEach( (strategy) => {
    let groupItem = createListGroupItemMarkup( strategy );
    suggestedMovesContainer.appendChild( groupItem );
  });
}

function setChessboardFen() {
  // grab the textarea from the .fen-loader component
  const fenTextarea = document.getElementById('js-fen-textarea');
  // element that displays a warning if 
  // a non-FEN string is entered in the textarea
  const fenFeedback = document.querySelector('.fen-loader + .fen-feedback');
  // get the value of the textarea
  const fen = fenTextarea.value;

  // check if fen is valid
  if( parseFEN(fen) ) {
    CHESSBOARD.position(fen);
  } else {
    // make it visible
    fenFeedback.style.opacity = 1;
    // hide it after a delay of 1.5s
    setTimeout( function () {
      fenFeedback.style = '';
    }, 1500)
  }
}

// Event Listeners

// submit button for the .fen-loader component
const submitFenBtn = document.getElementById('js-fen-submit');
submitFenBtn.addEventListener('click', setChessboardFen);
// get-moves button for the .suggested-moves component
const getMovesBtn = document.getElementById('js-get-moves');
getMovesBtn.addEventListener('click', getSuggestedMoves);

/* ********Markup creation functions******** */

export function createCardMarkup( strategyDetails ) {
  // Create Bootstrap card markup
  // https://getbootstrap.com/docs/4.1/components/card/#using-grid-markup
  // .card element
  let card = document.createElement('div');
  card.classList = 'card mb-3';
  card.setAttribute('data-strategy-name', strategyDetails.strategy);

  // .card-body container
  let cardBody = document.createElement('div');
  cardBody.classList = 'card-body';

  // .card-title 
  let cardTitle = document.createElement('h2');
  cardTitle.classList = 'card-title';
  cardTitle.innerText = strategyDetails.strategyPrettyName;

  // .card-text
  let cardText = document.createElement('p');
  cardText.classList = 'card-text lead';
  cardText.innerText = strategyDetails.description;

  // .btn.btn-primary link to documentation
  let link = document.createElement('a');
  link.classList = 'btn btn-primary';
  link.innerText = 'Documentation';
  link.setAttribute('target', '_blank');
  link.href = strategyDetails.documentation;

  // append everything to .card-body
  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);
  cardBody.appendChild(link);

  // append .card-body to .card container
  card.appendChild(cardBody);

  return card;
}

export function createListGroupItemMarkup( strategyDetails ) {
  // link
  let link = document.createElement('a');
  link.classList = 'list-group-item list-group-item-action strategy';
  link.setAttribute('data-strategy-name', strategyDetails.strategy)

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
  strategyName.innerText = strategyDetails.strategyPrettyName;

  // strategy .desc
  let strategyDesc = document.createElement('p');
  strategyDesc.classList = 'mb-1 desc';
  strategyDesc.innerText = strategyDetails.shortDescription;

  // .col-2.align-self-center
  let col = document.createElement('div');
  col.classList = 'col-2 p-0 d-flex justify-content-center align-items-center';

  // .strategy-move
  let strategyMove = document.createElement('span');
  strategyMove.classList = 'strategy__move';
  strategyMove.id = `js-move-${strategyDetails.strategy}`;

  // append .name & .desc to .strategy__info
  strategyInfo.appendChild(strategyName);
  strategyInfo.appendChild(strategyDesc);

  // loader
  // markup here https://loading.io/css/
  let loader = document.createElement('div');
  loader.classList = 'lds-ellipsis';
  loader.id = `js-loader-${strategyDetails.strategy}`;
  let div1 = document.createElement('div');
  let div2 = document.createElement('div');
  let div3 = document.createElement('div');
  let div4 = document.createElement('div');

  loader.appendChild(div1);
  loader.appendChild(div2);
  loader.appendChild(div3);
  loader.appendChild(div4);

  // append .strategy-move to .col-2.align-self-center
  col.appendChild(strategyMove);
  col.appendChild(loader);

  // create .consecutive-moves button here

  // append .strategy__info & .col-2.align-self-cente
  // to .row
  row.appendChild(strategyInfo);
  row.appendChild(col);
  // append .consecutive-moves button to .row here

  // append .row to .container-fluid
  container.appendChild(row);

  // append .container to link
  link.append(container);

  return link;
}

export function createCommentMarkup( comment ) {
  if(comment.strategy != "undefined" && comment.commentary != "undefined" && comment.userMove !== comment.suggestedMove) {
    let strategyLabel = document.createElement('span');
    strategyLabel.classList = 'strategy-label';
    strategyLabel.innerText =  comment.strategy + ": ";

    let suggestedMove = document.createElement('a');
    suggestedMove.classList = 'suggested-move shadow-sm';
    suggestedMove.setAttribute('href', "#");
    suggestedMove.setAttribute('data-fen', comment.fen);
    suggestedMove.setAttribute('data-move', comment.suggestedMove);
    suggestedMove.innerText = comment.suggestedMove;

    let userMove = document.createElement('a');
    userMove.classList = 'user-move shadow-sm';
    userMove.setAttribute('href', "#");
    userMove.setAttribute('data-fen', comment.fen);
    userMove.setAttribute('data-move', comment.userMove);
    userMove.innerText =  comment.userMove;

    let parsedCommentary = comment.commentary;
    parsedCommentary = parsedCommentary.replace(comment.suggestedMove, suggestedMove.outerHTML)
    parsedCommentary = parsedCommentary.replace(comment.userMove, userMove.outerHTML)

    let commentaryText = document.createElement('span');
    commentaryText.classList = 'commentary-text';
    commentaryText.innerHTML =  parsedCommentary;

    let commentaryContent = document.createElement('p');
    commentaryContent.classList = 'commentary__line';

    commentaryContent.appendChild(strategyLabel);
    commentaryContent.appendChild(commentaryText);
    
    return commentaryContent;
  }
}
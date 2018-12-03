# Task-uri s10
După discuția de la laboratorul din **săptămâna 7** au reieșit următoarele cerințe:
* oferirea de mutări sugerate pentru starea curentă
* oferirea de detalii despre algoritmii/strategiile implementate
* posibilitatea de a introduce o stare a jocului (FEN, utilizând tabla interactivă)
* comentariu pentru partidă

## 1. Sugerare mutări pentru starea curentă
### 1.1 HTML+CSS
* `.suggested-moves` - componentă care să conțină:
  * o zonă pentru afișarea listei de perechi (nume-strategie, mișcare-sugerată). Numele strategiilor vor fi hardcodate.
  * un button pentru sugerarea mișcărilor (buton ce va apela funcția `getSuggestedMoves` la event-ul de `click`)
### 1.2 Implementarea unor funcții JavaScript:
* `getSuggestedMoves( fen, strategies )` - lansează mai multe request-uri asincrone de tip `GET` (câte unul pentru fiecare strategie din `Array`-ul global `strategies`). Route-ul la care se lansează fiecare cerere este `/moves` și acceptă parametrii `fen` (poziția curentă a tablei, se poate obține din *chessboard.js*) și `strategy`. 

  Vezi [Promises](https://www.youtube.com/watch?v=2d7s3spWAzo) sau [async/await](https://www.youtube.com/watch?v=vn3tm0quoqE).

  *chessboard.js* folosește jQuery așa că sugerez să folosim [implementarea](https://api.jquery.com/jquery.ajax/) de acolo pentru request-uri asincrone.

  Exemplu de route cu parametri:
  ```
  /moves?fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201&strategy=stockfish
  ```
  P.S.: Vezi [JavaScript template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).

  Funcția va returna un `Array` de tipul:
    ```
    [
      {
        "strategy": "strategy1",
        "move": "move1",
      },
      ...
    ]
  ```
* `renderSuggestedMoves ( suggestedMoves )` - funcție ce afișează în componenta `.suggested-moves` rezultatul funcției `getSuggestedMoves`.

## 2. Detalii despre algoritmii implementați
### 2.1 HTML+CSS
* Stilizarea componentei `strategies-details`:

  `.strategies-details` - componentă care să conțină:
  * o listă de elemente unde fiecare element este o subcomponentă ce conține
    * titlul algoritmului
    * descriere
    * link către documentație

### 2.2 Implementarea unor funcții *JavaScript*
* `getStrategies()` lansează un request **asincron** de tip `GET` la ruta `/strategies`.
  **Funcția se va executa la încărcarea paginii.**
  
  Răspunsul va fi un `Array` de tipul:
  ```
  [
    {
      "strategy": "name-of-strategy",
      "description": "description-of-strategy",
      "link": "link-to-documentation"
    },
    ...
  ]
  ```
  Funcția va adăuga într-un `Array` **global** ( `strategies` ) valorile câmpurilor "strategy" pentru a servi și altor funcții (e.g. `getSuggestedMoves`). Valoare returnată va fi răspunsul primit de la server.

  *chessboard.js* folosește jQuery așa că sugerez să folosim [implementarea](https://api.jquery.com/jquery.ajax/) de acolo pentru request-uri asincrone.

* `renderStrategiesDetails( strategiesDetails )` - funcție ce va crea câte o "componentă" pentru fiecare strategie/algoritm și detaliile sale și o va adaugă în interiorul container-ului `.strategies-details`.

  Exemplu structură HTML pentru fiecare "componentă":
  ```
  <div class="strategy">
    <h2 class="strategy__title">name-of-strategy</h2>
    <p class="strategy__description">
      description-of-strategy
    </p>
    <a class="strategy__link" href="link-to-documentation">Documentation</a>
  </div>
  ```
  Vezi [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) sau [document.createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement).

## 3. Posibilitatea de a introduce o stare a jocului (FEN, utilizând tabla interactivă)
### 3.1 HTML+CSS
* `.fen-loader` - componentă ce conține:
  * `textarea` unde se introduce fen-ul
  * buton de `submit` pentru încărcarea fen-ului (ce va avea ca `eventListener` pe `click` funcția `setChessboardFen`)
### 3.2 Implementarea unei funcții *JavaScript*:
* `setChessboardFen()` - la apăsarea unui buton de *submit* afișează *input*-ul (FEN) introdus într-un *textarea* pe tabla de joc interactivă. Input-ul din textarea trebuie validat ( [sugestie](https://github.com/jayasurian123/fen-validator) dacă se pricepe cineva cu npm ) după formatul [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation). 
  
  Consultați [documentația chessboard.js](http://chessboardjs.com/docs) pentru a afla cum se poate încărca un FEN pe tabla interactivă.

## 4. Comentarii pentru o partidă
Va fi postat după ce discut cu băieții de la Back-End despre cum vom face cu rutele și procesarea.
# Also
## GitHub !
Datorită naturii task-urilor suntem nevoiți să lucrăm pe aceleași 3 fișiere (`styles.css`, `main.js`, `index.html`). 

**După pașii de `add` și `commit` faceți `pull` ca să vă asigurați că aveți ultima versiune.** Atâta timp cât fiecare lucrează în zona asociată funcției JS/componentei html asociată nu ar trebui să fie probleme.

Dacă aveți vreo sugestie pentru evitarea situațiilor de conflicte **nu ezitați** să o faceți publică!

Dacă cumva apar conflicte, PHPStorm & WebStorm de la Intellij au un tool de diff pentru conflicte foarte eficient și intuitiv. Sunt și extensii pentru VS Code (e.g. GitLens).
## Stiluri
În fișierul `styles.css`. 

Folosim metodologia [BEM](https://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/) pentru lizibilitate în CSS, dar nu coborâm mai mult de 2 nivele pentru că numele clasei devine prea lung (e.g. block__element1__element2___element3--modifier1). [Articolul acesta](https://medium.com/fed-or-dead/battling-bem-5-common-problems-and-how-to-avoid-them-5bbd23dee319) explică destul de bine cum se poate folosi BEM eficient.

De asemenea, vom lăsa id-urile pentru JavaScript ( [prefixate cu `js-` e.g. `id="js-suggested-moves`] pentru a selecta mai ușor elementele ) și stilizarea o facem cu ajutorul claselor și/sau a [pseudo-claselor](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).
## JavaScript
În fișierul `main.js`. Comentați-vă codul ca să fie clar pentru toată lumea.

O să folosim [let & const](https://www.youtube.com/watch?v=sjyJBL5fkp8&t=1s) din specificația ES6.

Convenția de numire este camelCase.
## chessboard.js
[docs](http://chessboardjs.com/docs)
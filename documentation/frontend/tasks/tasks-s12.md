# Task-uri s12 - Front-End
După discuția de la laboratorul din **săptămâna 10** au reieșit următoarele cerințe:
* `header` care să conțină:
  * logo
  * denumirea aplicației (un acronim)
  * help
    * o componentă ce conține informații despre cum se folosește aplicația
  * un link pentru tranziție între modurile de *analiză partidă* și *obținerea mișcărilor sugerate de algoritmi*
  * un link pentru detalii legate de algoritmii implementați
* crearea paginii de *analiză a unei partide* și a logicii aferente
* fiecare strategie să ofere, la apăsarea unui *buton de detalii*, mai mult de o mișcare (3 consecutive + scoruri fiecare mutare)
* `tooltip` pentru componenta `.fen-loader`
  * apare la selectarea elementului `<textarea>`
  * conține detalii despre notația **FEN**
* feedback-ul componentei `.fen-loader` trebuie să afișeze mai multe detalii atunci când validarea eșuează
* posibilitatea de a selecta culoarea cu care se joacă
* crearea unei componente pentru comentarii
* reîmprospătarea paginii de prezentare (cea de pe **branch**-ul `gh-pages`)
* crearea unei funcții de highlight pentru mutări. Funcția va evidenția mutarea sugerată pe tabla interactivă
  
# Precizări importante
Nu toate task-urile vor avea issue-uri pe GitHub inițial. Pentru unele e necesar să mă consult cu echipa de Back-End pentru a conveni cum/ce date vor veni ca răspuns la request-urile pe anumite rute.
## GitHub
**După pașii de `add` și `commit` faceți `pull` ca să vă asigurați că aveți ultima versiune.**

Dacă cumva apar conflicte, [PHPStorm](https://www.jetbrains.com/phpstorm/) & [WebStorm](https://www.jetbrains.com/webstorm/) de la Intellij au un tool de diff pentru conflicte foarte eficient și intuitiv. Sunt și extensii pentru VS Code (e.g. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)).
## CSS
În fișierul `styles.css`.

Folosim metodologia [BEM](https://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/) pentru lizibilitate în CSS, dar nu coborâm mai mult de 2 nivele pentru că numele clasei devine prea lung (e.g. block__element1__element2___element3--modifier1). [Articolul acesta](https://medium.com/fed-or-dead/battling-bem-5-common-problems-and-how-to-avoid-them-5bbd23dee319) explică destul de bine cum se poate folosi BEM eficient.

De asemenea, vom lăsa id-urile pentru JavaScript ( [prefixate cu `js-` e.g. `id="js-suggested-moves"`] pentru a selecta mai ușor elementele ) și stilizarea o facem cu ajutorul claselor și/sau a [pseudo-claselor](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

### Style Guide
**Friendly reminder**:
* Dacă sunt mai mulți selectori separați prin ',' (virgulă), fiecare selector pe o linie nouă
* Un spațiu între selector și '{'
* Indentare cu un tab pentru proprietăți
* Un enter distanță între seturi de reguli diferite

Exemplu de indentare și spațiere
```
.some-class,
.some-other-class {
  background-color: lightgrey;
}

.navbar {
  display: flex;
}
```
## JavaScript
Pentru a modulariza codul vom folosi feature-urile ES6 [import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) și [export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) ([in-depth docs](http://exploringjs.com/es6/ch_modules.html)) + [let & const](https://www.youtube.com/watch?v=sjyJBL5fkp8&t=1s).

# Important
Un nou folder-tree:
* **components** - cod pentru module (de exemplu modulul/componenta pentru tabla de șah)
  * `Chess.component.js`
* **functions** - fișiere ce conțin funcții care servesc unui scop mai general, dar nu constituie neapărat un modul
  * `Async.functions.js`
  * `Client-logic.functions.js`
  * `Markup.functions.js`
  * `Render.functions.js`
* **utils** - momentan e doar un fișier pentru constante aici
  * `Constants.utils.js`
 
**A se observa convenția de numire a fișierelor**.

De asemenea vom folosi și [module pattern](https://toddmotto.com/mastering-the-module-pattern/) acolo unde este cazul (e.g. pentru a grupa codul unei componente cu mai multe funcționalități).


### Style guide
**Friendly reminder**:
* Constantele - UPPERCASE_CU_UNDERSCORES
* variabile&funcții - camelCase.

Exemplu de indentare și spațiere
```
function someFunction( param1, param2 ) {
  const THE_STRING = "this is the string";

  if( param1 > param2 ) {
    let temp;

    temp = param1;
    param1 = param2;
    param2 = temp;
  }

  return `${param1}${THE_STRING}${param2}`;
}
```
# Detalii task-uri
## 1. Componenta `header`
### 1.1 HTML + CSS - `.nav--header`
Crearea unei componente care să conțină:
* un logo (am impresia că Teodor Almășanu l-a făcut deja)
* un titlu cu denumirea aplicației (un acronim)
* un link pentru `Help`
* un link către pagina de `Match analysis`
* un link pentru detaliile legate algoritmii implementați (`Strategies details`).
### 1.2 HTML + CSS - `.help`
Crearea unei componente care să conțină detalii despre aplicație și utilizarea acesteia. Textul va fi în limba engleză. 
Sugestie poate fi un [jumbotron](https://getbootstrap.com/docs/4.1/components/jumbotron/) având conținutul textual aferent (descrierea aplicației).
## 2. Pagina `match analysis`
### 2.1 HTML + CSS
Crearea paginii de `match analysis` care să conțină:
* tabla interactivă (la fel ca și pe pagina `index.html`)
* `.analysis-player` - o componentă cu zonele de:
  * afișare a istoricului partidei (istoricul mutărilor)
  * controlul derulării partidei (play, pause, undo, reset)
    * vezi [FontAwesome](https://fontawesome.com/icons?d=gallery) pentru icon-uri
Exemple de layout: [aici](https://lichess.org/analysis) și [aici](https://www.chess.com/analysis-board-editor).
### 2.2 JS
TBA
## 3. Fiecare strategie să ofere, la apăsarea unui *buton de detalii*, mai mult de o mișcare (3 consecutive + scoruri fiecare mutare)
### 3.1.1 JS
Crearea unui buton cu textul "Get 3 consecutive moves" și a unei zone pentru afișarea respectivelor mutări. Crearea butonului va avea loc în funcția `createListGroupItemMarkup()` din fișierul `Markup.functions.js`.
### 3.1.2 JS
TBA
## 4. Tooltip pentru componenta `.fen-loader`
### 4.1 HTML + CSS
În momentul în care `<textarea>`-ul este selectat (în **focus**) trebuie să apară un [popover](https://getbootstrap.com/docs/4.1/components/popovers/) cu câteva detalii despre notația FEN + link către un articol care descrie în detaliu standardul de notație.

Inițializarea `popover`-ului (vezi documentația) se va face în funcția `$( document ).ready()`.
## 5. Feedback-ul componentei `.fen-loader`
### 5.1 JS
Oferirea mai multor detalii atunci când validarea  din componenta `.fen-loader` eșuează. Vezi [.validate_fen()](https://github.com/jhlywa/chess.js#validate_fenfen) din [documentația](https://github.com/jhlywa/chess.js) *chess.js*.
Feedback-ul va fi afișat în elementul cu clasa `.fen-feedback`.

Acest task presupune lucrul pe ramura `else` din funcția `setChessboardFen` care se află în fișierul `Client-logic.functions.js`.
## 6. Posibilitatea de a selecta culoarea cu care se joacă
### 6.1 HTML + CSS + JS
* Crearea unui buton cu textul "Flip board" care la apăsarea lui va întoarce orientarea tablei.
* Crearea unei funcții ce va fi atașată cu un `eventListener` pe buton. Această funcție apelează metoda [.flip()](http://chessboardjs.com/docs#methods:flip) a tablei interactive.

`eventListener`-ul va fi scris în `main.js`.
## 7. Crearea unei componente de comentarii
### 7.1 HTML + CSS
#### 7.1.1 `.commentary`
Crearea unei componente `.commentary` care să conțină:
* o zonă pentru istoricul mutărilor(`.commentary__history`) cu 3 coloane ([sugestie layout](https://lichess.org/M8B5xCTF/black)):
  * una pentru numerotarea turelor/rundelor
  * una pentru mutările culorii albe
  * una pentru mutările culorii negre
#### 7.1.2 `.commentary-modal`
* Crearea unui buton de trigger cu textul "Get commentary"
* Crearea unui modal ce va avea în `.modal-body` o listă de elemente de forma:
  * `.strategy-name` - un element HTML de tip *heading*
  * `commentary-content` - un element de tip *paragraph* pentru textul comentariului
#### 7.1.3 `.load-match`
O componentă formată din:
* un `textarea`
* un buton de submit
### 7.2 JS
#### 7.2.1 `getCommentary()`
Funcție ce va face un request asincron de tip `GET` la ruta `/commentary` folosind ca valoare pentru parametrul `game` input-ul din componenta `.load-match`. Momentan pe back-end nu este nici o restricție pentru parametrul `game` așa că pentru testare se poate folosi orice string. Funcția va returna răspunsul primit.

Funcția va fi scrisă în fișierul `Async.functions.js` și va fi atașată printr-un `eventListener` (în `main.js`) pe butonul de submit al componentei `.load-match`.
#### 7.2.2 `renderCommentary( commentary )`
Funcția va primi ca parametru un obiect de forma:
```
{
  "strategy": "strategyName",
  "commentary": "commentaryContent"
}
```
Aceasta va insera în modalul `.commentary-modal`:
* în câmpul `.strategy-name` valoare atributului `strategy`
* în câmpul `commentary-content` valoarea atributului `commentary`

Funcția va fi scrisă în fișierul `Render.functions.js`.
#### 7.2.3 `renderCommentaryModal()`
Funcție ce va apela `createCommentaryModalMarkup` și va adăuga pe `<body>` modalele respective
## 8. Reîmprospătarea paginii de prezentare (cea de pe **branch**-ul `gh-pages`)
### 8.1 HTML + CSS
Aplicarea unui design, la alegere, mai atrăgător decât cel actual. Conținutul textual al paginii va fi static, inclus în markup.
### 8.2 Text de prezentare
Formularea unei text de prezentare a aplicației și funcționalităților acesteia.
## 9. Crearea unei funcții de highlight pentru mutări
### 9.1 JS
Hover-ul pe un element din lista de mișcări sugerate face trigger la highlight-ul mișcării pe tablă.
Se vor respecta culorile asociate algoritmilor.
`eventListener`-ul va trata evenimentele de `mouseover`, respectiv `mouseleave`( [vezi aici](https://javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave) ). Funcția va fi scrisă în fișierul `Client-logic.functions.js`.
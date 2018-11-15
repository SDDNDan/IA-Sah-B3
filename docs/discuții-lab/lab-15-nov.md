## Design aplicație
* tutorial ❌
* login ❌
* aplicația să ofere un insight legat de cum aleg diversele strategii mutările optime
* nivele diferite de a nuanța output-ul legat de mutările alese de diversele strategii (mai multe sau mai puține informații legate de cum funcționează platforma când alege mutările)

## Back-End
* mai mult research legat de ce strategie implementează Stockfish
* reverse-engineering 
* trebuie implementate și alte strategii decât cea din Stockfish
* utilizatorul cere sugestii pentru o mutare -> mai multe strategii pentru răspuns (vizualizarea modului în care diversele strategii iau decizii)
* comentariile vor fi generate după terminarea meciului
* la fiecare tură output-ul va fi format din mutările sugerate de strategiile implementate
  
## Front-End
* informații despre modul în care funcționează platforma (algoritmi, strategii, funcții de evaluare) trebuie să fie disponibile pe site
* comentariile vor fi generate după terminarea meciului
* mod atractiv de derulare a partidei (highlight pentru diversele mutări sugerate de strategii + highlight&animații pentru mutări)

## QA
* framework-uri pentru testare
* e.g. Selenium
* teste pentru
  * greșeli în reprezentarea stărilor (FEN)
  * dacă un meci ar trebui să se termine după mutarea 20, dar el continuă
  * etc.

## Extra
* "... strategii care explică cum se combină strategii ..."
* s13-s14 documentație pentru Learn&Earn (alte criterii de evaluare)

# Următorul deadline: săpt. 10
## Front-end
* să pot oferi sugestii pentru mutări
* comentarii pentru o partidă
* chestiile esențiale (să pot introduce o stare a meciului [text, vizual folosind chessboard.js] + sugestii mutări)

## Back-end
* măcar 1-2 strategii implementate
* generare comentarii

## QA
* design teste
* metode de a testa programul
* testare automată: scalabilitate + framework
  * back-end
  * front-end
* document cu teste ASAP
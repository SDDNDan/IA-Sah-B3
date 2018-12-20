# Front-End
* strategy-details dispare din nav; click pe o strategie din suggested moves deschide elem. din stânga cu detalii doar despre algoritmul pe care s-a făcut click
* după fiecare mutare să fie afișat sub tablă notația fen corespunzătoare stării curente
* suggested moves + commentary -> collapsible
* posibilitate de filtrare a algoritmilor (ascundere + eliminare din apeluri asincrone)
  * reset filter
* help
  * textul pentru fiecare feature să fie în pagină
  * background cu o imagine cu minimul de conținut al paginii pentru zonele de explicare
    * fie întunecată și doar feature-urile cu highlight
    * fie imagine cu elemente html

# Back-End
* denumirea strategiilor/engine după ce implementează (euristici diferite)
* comentariile să fie pentru un meci finalizat => verbele la trecut
  * având în vedere că se știe concluzia meciului, se poate folosi acest lucru pentru a genera comentariile
  * trebuie identificate mutările la care se referă comentariile
    * referințe la diverse stări în comentariu
* ce strategie folosește Stockfish ?
* euristică la alphabeta_prunning

# Extra
* un mod (free mode) pentru a muta liber piesele pe tabla cu scopul generării unui anumit fen

# După vacanță
* tema Rock-Paper-Scissors (S13)
* tema suplimentară (S13)
* documentație
  * front-end
    * feature-uri și cum au fost implementate
    * minim 20-25 de pagini
      * exemple de cod pot fi folosite și/sau imagini
      * verificat licențe
  * back-end
    * feature-uri și cum au fost implementate
    * minim 20-25 de pagini
  * qa
    * feature-uri și cum au fost implementate
    * minim 20-25 de pagini => raportul final de testare
      * testare manuală/automată 
      * puzzle-uri de șah -> care din strategii rezolvă provocările respective
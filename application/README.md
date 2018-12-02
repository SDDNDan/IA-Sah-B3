# Modul de lucru / Cum se porneste aplicatia

Pe partea de backend vom folosi Python 3.7.0 (https://www.python.org/downloads/release/python-370/) in combinatie cu Flask (http://flask.pocoo.org/). Pentru a nu aparea probleme de compatibilitate o sa va rog pe toti sa instalati si sa folositi python 3.7.0.

Inainte de a incepe lucrul trebuie creat un mediu virtual de lucru urmand pasii urmatori (se presupune Python 3.7.0 instalat, ghidul este pentru Windows 10):

1. Deschideti Windows PowerShell cu drepturi de administrator (https://www.top-password.com/blog/5-ways-to-run-powershell-as-administrator-in-windows-10/).
2. Navigati, din consola deschisa, in directorul 'application' din proiect (navigarea se face la fel ca pe pe shellul de la Linux).
3. Rulati ```py -3.7 --version```. Outputul ar trebuie sa fie **Python 3.7.0**. In caz contrar, asigurati-va ca aveti Python 3.7.0 instalat.
4. Rulati ```py -3.7 -m venv venv``` si asteptati sa se termine executia.
5. Rulati ```venv\Scripts\activate```. In cazul in care primti o eroare legata de Execution Policy, rulati ```Set-ExecutionPolicy RemoteSigned``` si incercati din nou.
6. Acum in fata terminalului ar trebui sa apara (venv).
7. Rulati ```pip install -r requirements.txt```.

Ca sa porniti aplicatia urmati pasii urmatori:

1. Asigurati-va ca sunteti in mediul virtual de lucru, apare (venv) in fata terminalului, si ca sunteti in directorul 'application'. Daca nu, navigati in directorul 'application' din proiect si rulati ```venv\Scripts\activate```.
2. Rulati ```$env:FLASK_APP = "application.py"```
3. Rulati ```flask run```.

Cum sa testati daca aplicatia merge:

1. Dupa ce ati urmat pasii de mai sus, deschideti un browser si conectati-va pe http://127.0.0.1:5000/moves?fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201.
2. Raspunsul ar trebuie sa fie de forma **[{"Strategy": "Random", "Move": "D2D4"}]**.

**In cazul in care aveti nevoie sa adaugati o dependenta noua, instalati-o din mediul de lucru virtual si apoi din directorul 'application' rulati ```pip freeze > requirements.txt```.**

**In cazul in care primiti vreo eroare legata de o dependenta, din directorul 'application' rulati ```pip install -r requirements.txt```**.

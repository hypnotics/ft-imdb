Krav
- Firefox med GreaseMonkey installerat
- Python

1. Installera scriptet: https://greasyfork.org/sv/scripts/11617-imdb-list-helper i Firefox. 

2. Ladda ner alla dina betyg från filmtipset som excel
3. Kopiera de två kolumnerna Betyg och imdb# till ett nytt dokument
4. Dubblera rating (eller hur du nu vill göra) med en formel för att omvandla till imdb’s tio-skala.
5. Exportera bladet med din nya imdb-rating och imdbnummer (två kolumner) som csv.
6. Öppna i Texteditor
7. Sök och ersätt med regexp .,\n för att ta bort filmer utan imdbnr

8. Modifiera file och outfile i imdb.py så att sökvägarna till filerna blir rätt.

9. Kör python3 imdb.py
Kopiera innehållet i filen outfile till urklipp

10. Logga in på imdb och skapa en ny lista.
Greasemonkey scriptet borde låta dig pasta in listan med betyg. Formatet är:

1,tt3630276
4,tt0022142
2,tt0453453
…

Välj Import Mode: Ratings och tryck start. 

10. Spara listan och du e klar. Filmerna läggs in i en lista och dina betyg kopieras till dina ratings :)


KOMMENTARER:
De filmer som saknar imdb-nr i din filmtipset excel måste läggas in manuellt.
https://contribute.imdb.com/updates?update=title&ref_=login

Det kan vara en god idé att köra 500 i taget då det tar en stund och scriptet kan stanna om den inte hittar nån film. T.ex. har Turist bytt imdbnr.
Man kan alltid försöka
http://www.imdb.com/title/ttGAMMALT-NR/ för att hitta det aktuella imdb-numret.

Om skriptet fastnar så bara kopiera imdb-numret för manuell hantering senare och tryck skip.

PROBLEM:
tt3630276 - Turist

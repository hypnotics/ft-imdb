#Filmtipset -> IMDB

## Krav
- Firefox med GreaseMonkey installerat
- Python 3 med xlrd (pip3 install xlrd)

## Hur man importerar sina betyg från filmtipset till imdb

1. Installera scriptet: https://greasyfork.org/sv/scripts/11617-imdb-list-helper i Firefox. 
2. Ladda ner alla dina betyg från filmtipset som excel
3. Kör 
```
python3 ft_to_imdb.py <path/to/filmtipset_betyg.xls>
```
Kopiera innehållet från filen ratings.txt till urklipp.
4. Logga in på imdb och skapa en ny lista.
Greasemonkey scriptet borde låta dig pasta in listan med betyg. Formatet är:

```
1,tt3630276
4,tt0022142
2,tt0453453
…
```

Välj Import Mode: Ratings och tryck start. 

Spara listan och du e klar. Filmerna läggs in i en lista och dina betyg kopieras till dina ratings :)


## Kommentarer:
De filmer som saknar imdb-nr i din filmtipset excel måste läggas in manuellt.
https://contribute.imdb.com/updates?update=title&ref_=login

En fil skapas med dina betygsättningar som saknar imdb id: not_in_imdb.csv

Det kan vara en god idé att köra 500 i taget då det tar en stund och scriptet kan stanna om den inte hittar nån film. T.ex. har Turist bytt imdbnr.
Man kan alltid försöka
http://www.imdb.com/title/ttGAMMALT-NR/ för att hitta det aktuella imdb-numret.

Om skriptet fastnar så bara kopiera imdb-numret för manuell hantering senare och tryck skip.

## Problem:
tt3630276 - Turist

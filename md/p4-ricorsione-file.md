title: Ricorsione e file
subtitle: Introduzione alla programmazione
figure: images/fun/matryoshka.png

---

title: Programmazione ricorsiva

- Molti linguaggi consentono ad una funzione (o procedura) di chiamare se stessa
- Chiamata ricorsiva, diretta o indiretta

![](images/fun/recursion.svg)

---

title: Fattoriale, ricorsione
figure: images/fun/stack.svg

- Ad ogni invocazione di una funzione, viene creato nello **stack** un nuovo record
- **Contesto locale** alla particolare attivazione della funzione stessa

code: python

    def factorial(n: int) -> int:
        result = 1
        if n > 1:
            result = n * factorial(n - 1)
        return result

Ai primordi (Fortran 66 ecc.) solo allocazione statica <br> Spazio fisso ed unico per dati locali ad una funzione → no ricorsione

---

title: Stack dell'applicazione
figure: images/fun/books-stack.png

- Pila: memoria dinamica *LIFO (Last In First Out)*
    - Dimensione massima prefissata
- Il programma ci memorizza automaticamente:
    - **Indirizzo di ritorno** per la funzione <br> Inserito alla chiamata, estratto all'uscita
    - **Parametri** della funzione <br> Inseriti alla chiamata, eliminati all'uscita
    - **Variabili locali**, definite nella funzione <br> Eliminate fuori dall'ambito di visibilità

---

title: Vista semplificata dello stack
class: large-image

![](images/fun/stack-content.svg)

---

title: Record di attivazione
class: large-image

![](images/fun/records.svg)

---

title: Visibilità di una variabile

- Insieme di istruzioni da cui è accessibile
    - *Ciclo di vita*: esistenza in memoria della var (etichetta)
    - I valori (oggetti) in Python sono tutti gestiti dinamicamente
- Visibilità **globale**
    - Variabili fuori da ogni funzione - *Meglio evitare!*
    - Allocazione *statica* in alcuni linguaggi
- Visibilità **locale** alla funzione
    - Variabili locali e parametri
    - Allocazione *automatica* di spazio in *stack* ad ogni attivazione della funzione (possibile la ricorsione)
- Visibilità locale al blocco (es. `if`): non in Python!

---

title: Esempi di ricorsione
class: segue dark

---

title: I conigli di Fibonacci
class: large-image

![](images/fun/fib-rabbits.png)

>

fib(0) = fib(1) = 1;  fib(n) = fib(n-1) + fib(n-2);

---

title: Fibonacci, ricorsione

code: python

    def fibonacci(n: int) -> int:
        result = 1
        if n > 1:
            result = fibonacci(n-1) + fibonacci(n-2)
        return result

![](images/fun/fib-calls.svg)

---

title: Fibonacci, memoization

code: python

    _fibonacci_lookup = [1, 1]

    def fibonacci(n: int) -> int:
        if n < len(_fibonacci_lookup):
            return _fibonacci_lookup[n]
        result = fibonacci(n - 1) + fibonacci(n - 2)
        _fibonacci_lookup.append(result)
        return result

code: python

    from functools import lru_cache
    
    @lru_cache()                   # function decoration
    def fibonacci(n: int) -> int:
        result = 1
        if n > 1:
            result = fibonacci(n-1) + fibonacci(n-2)
        return result

---

title: Fibonacci, iterazione

code: python

    def fibonacci(n: int) -> int:
        value = 1
        previous = 0

        for i in range(n):
            value, previous = value + previous, value

        return value

---

title: N regine, backtracking
class: large-image

![](images/fun/queens.svg)

---

title: N regine, verifica
figure: images/fun/queens-sol.svg

code: python

    def print_board(board: list):
        for y in range(len(board)):
            for x in range(len(board)):
                if x == board[y]: print('|Q', end='')
                else: print('| ', end='')
            print('|')

    def under_attack(board: list, x: int, y: int) -> bool:
        for i in range(y):  # for all rows above y
            d = y - i
            # directions: ↖↑↗ (no queens below)
            if board[i] in (x - d, x, x + d):
                return True
        return False

>

`board` è una lista di `int`: per ogni riga della scacchiera, memorizza la posizione `x` della regina

---

title: N regine, ricorsione

code: python

    def place_queens(board: list, y=0) -> bool:
        if y == len(board):
            return True  # all queens already placed
        for x in range(len(board)):
            if not under_attack(board, x, y):
                board[y] = x  # (x, y) is safe: place a queen

                # try and place queens in the following rows
                if place_queens(board, y + 1):
                    return True

                board[y] = None  # no luck, backtrack
        return False

---

title: Esercizio - Massimo Comun Divisore
figure: images/hist/euclid.jpg

- Leggere due numeri
- Calcolare in una funzione il loro Massimo Comun Divisore
- Visualizzare il risultato della funzione

>

Provare ad usare sia l'iterazione che la ricorsione

Euclide: MCD(a, b) = a, se b = 0; <br>
MCD(a, b) = MCD(b, a mod b), se b > 0

---

title: Esercizio - Torre di Hanoi
figure: images/misc/hanoi-tower.png

- Tre paletti + N dischi di diametro decrescente
- Portare tutti i dischi dal primo all'ultimo paletto
- Si può spostare solo un disco alla volta
- Non si può mettere un disco su uno più piccolo

>

Usare la ricorsione. Immediato spostare un solo disco. <br>
N dischi: spostarne N-1 sul piolo né origine né dest., <br>
spostare l'ultimo disco sul piolo giusto, <br>
spostare ancora gli altri N-1 dischi.

---

title: Esercizio - Spirale
figure: images/misc/spiral.png

- Scrivere una funzione per riempire di numeri crescenti una matrice quadrata (o rettangolare)
- Seguire il percorso a spirale suggerito nella figura a fianco
- Dimensioni della matrice indicate dall'utente a runtime

>

Tenere traccia della direzione attuale (∆y, ∆x) <br>
Avanzare fino al bordo o ad una cella già visitata, <br>
poi cambiare la direzione in senso orario

Coordinate raster, rotazione oraria di 90°: `(x', y') = (-y, x)` <br>
In generale: `(x', y') = (x⋅cos(θ) - y⋅sin(θ), x⋅sin(θ) + y⋅cos(θ))` <br>

---

title: Sequenze annidate
class: segue dark

---

title: List comprehension (++)
figure: images/misc/lightsaber.png

- Modo conciso per creare una lista
- Ogni elemento: risultato di una operazione su un membro di altro iterabile
- Condizione sugli elementi, opzionale

code: python

    squares = [x ** 2 for x in range(12)]
    # squares = []
    # for x in range(12):
    #    squares.append(x ** 2)
    
code: python

    even_nums = [str(x) for x in range(12) if (x % 2) == 0]
    
---

title: Enumerate (++)
figure: images/repr/child-fingers.png

- Accoppia ciascun valore di una sequenza ad un indice crescente
- Genera una sequenza di tuple (coppie)
- Spesso si usa nei cicli `for`, quando serve sia il valore che l'indice

code: python

    >>> shopping_list = ["spam", "eggs", "bacon", "ketchup"]
    >>> list(enumerate(shopping_list))
    [(0, "spam"), (1, "eggs"), (2, "bacon"), (3, "ketchup")]

code: python

    shopping_list = ["spam", "eggs", "bacon", "ketchup"]
    for i, val in enumerate(shopping_list):
        print(i, val)

Risultati in lista, solo (!) per visualizzarli <br>
Altrimenti, Python non genera immediatamente i risultati (*lazy*)

---

title: Zip (++)
figure: images/fun/zip.jpg

- Accoppia gli elementi di due sequenze
- Genera una sequenza di tuple (coppie)
- Il risultato ha la lunghezza della sequenza più breve

code: python

    >>> shopping_list = ["spam", "eggs", "bacon", "ketchup"]
    >>> quantities = ["100 g", "6 pc", "200 g", "1 bottle", "too much"]
    >>> list(zip(shopping_list, quantities))
    [("spam", "100 g"), ("eggs", "6 pc"), ("bacon", "200 g"),
    ("ketchup", "1 bottle")]

Risultati in lista, solo (!) per visualizzarli

---

title: Map (++)
figure: images/misc/lightsaber.png

- Prende come parametri una funzione ed una sequenza
- *Funzione di ordine superiore*
- Applica la funzione a ciascuno dei valori
- Restituisce la sequenza di risultati

code: python

    >>> from math import sqrt
    >>> values = [0, 1, 2, 3, 4]
    >>> list(map(sqrt, values))
    [0.0, 1.0, 1.4142, 1.7320, 2.0]
    
code: python

    >>> from math import sqrt
    >>> list(map(sqrt, range(5)))
    [0.0, 1.0, 1.4142, 1.7320, 2.0]
    
Risultati in lista, solo (!) per visualizzarli

---

title: Dizionario (++)
figure: images/fun/dictionary.png

- A volte chiamato *mappa* o *array associativo*
- Insieme non ordinato di coppie chiave / valore
    - Le chiavi sono *uniche*: come nelle liste fanno da *indice* per accedere al valore corrispondente
    - Ma possono essere `int` o **`str`** (o altro tipo immutabile)

code: python

    >>> tel = {"john": 4098, "terry": 4139}
    >>> tel["john"]
    4098
    >>> tel["graham"] = 4127
    >>> tel
    {"graham": 4127, "terry": 4139, "john": 4098}

Provare anche `list(tel)` e `list(tel.items())`
    
---

title: Liste multidimensionali
- Liste di liste di ...
    - Accesso agli elementi: due o più indici (o *dimensioni*)
    - Se bidimensionali, denominate *matrici*

code: python

    a = [['A', 'B', 'C', 'D'],
         ['E', 'F', 'G', 'H'],
         ['I', 'L', 'M', 'N']]          # 2D
         
    b = ['A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H',
         'I', 'L', 'M', 'N']            # 1D

    i = y * cols + x                    # 2D -> 1D
    
    y = i // cols
    x = i % cols                        # 1D -> 2D

---

title: Somma colonne: matrice

code: python

    matrix = [[2, 4, 3, 8],
              [9, 3, 2, 7],
              [5, 6, 9, 1]]
    rows = len(matrix)
    cols = len(matrix[0])

    for x in range(cols):
        total = 0
        for y in range(rows):
            val = matrix[y][x]
            total += val
        print("Col #", x, "sums to", total)
    
---

title: Lista come pseudo-matrice

code: python

    matrix = [2, 4, 3, 8,
              9, 3, 2, 7,
              5, 6, 9, 1]
    rows = 3  # Cannot be guessed from matrix alone
    cols = len(matrix) // rows

    for x in range(cols):
        total = 0
        for y in range(rows):
            val = matrix[y * cols + x]   # 2D -> 1D
            total += val
        print("Col #", x, "sums to", total)
    
---

title: Matrici di dimensioni note

code: python

    matrix = [[' ' for x in range(cols)] for y in range(rows)]
    # all elements are inited as ' ' -- your need may vary

code: python

    matrix = []
    for y in range(rows):
        new_row = []
        for x in range(cols):
            new_row.append(' ')
        matrix.append(new_row)
    
---

title: Flussi di dati
figure: images/fun/magnetic-tape.png

- **Stream**: astrazione per flussi di informazione
    - Lettura o scrittura di informazioni su *qualunque* dispositivo I/O (*file, ma non solo*)
- **File di testo**
    - Varie codifiche (*UTF-8* o altro)
    - Conversioni automatiche, es. `"\n"` → `"\r\n"`
- **File binari**
    - I/O preciso byte a byte, senza nessuna conversione
    - Qualsiasi file... anche di testo!

---

title: Scrittura su file

- Funzione `open` per accedere ad un file (di testo)
    - Modalità scrittura o lettura: `"w"`, o `"r"`
- Scrittura su file: funzione `print`, o metodo `write`
- Blocco `with`: chiude il file al termine delle operazioni (anche in caso di errore)

code: python

    with open("some_file.txt", "w") as f1:
        f1.write("First line\n")   # explicit newline
        f1.write("Second line\n")  # continue writing here...
          
    with open("other_file.txt", "w") as f2:
        for x in range(10):
            print(x, x ** 2, file=f2)
          
---

title: Lettura da file

code: python

    with open("some_file.txt", "r") as f1:
        first_line = f1.readline()
        second_line = f1.readline()
        # both strings contain '\n' at the end
        # at end of file, an empty string is read

    with open("other_file.txt", "r") as f2:
        whole_text = f2.read()
        # do stg with whole_text

    with open("last_file.txt", "r") as f3:
        for line in f3:
            # line contains '\n' at the end
            # strip() removes withespaces at both ends
            print(line.strip(), ':', len(line))

---

title: I/O su stringhe e console (++)

- Stringhe come stream: `io.StringIO`
- Console come stream: `sys.stdin`, `sys.stdout`, `sys.stderr`

code: python

    import io, sys

    with io.StringIO() as output:
        output.write("First line.\n")
        print("Second line.", file=output)
        # Retrieve stream contents, i.e. "First line.\nSecond line.\n"
        contents = output.getvalue()        
        sys.stdout.write(contents)

code: python

    for line in sys.stdin:  # CTRL-D (Lin) or CTRL-Z (Win) to end the input
        print(len(line))    # notice '\n' at the end

---

title: Errori da file (++)
figure: images/fun/garbled-tape.png

- **Eccezioni**: per gestire separatamente i casi inattesi
    - Errore all'interno di `try`: esecuzione interrotta subito
    - Eseguito il blocco `except` che gestisce il tipo di errore verificatosi (possibile avere diversi blocchi `except`)
    - Il blocco `with` assicura la chiusura del file

code: python

    try:
        with open("other_file.txt", "r") as f:
            whole_text = f.read()
            # do stg with whole_text
    except IOError as err:
        print("Oh, my!")
          
---

title: Es.: Memory
figure: images/misc/memory.png

- Allocare una lista, di dimensione `rows×cols`
    - L'utente sceglie `rows` e `cols`, però celle in numero pari
- Inserire in ordine le prime lettere dell'alfabeto, ciascuna ripetuta due volte
- Mescolare le celle
    - Per ciascuna cella, scegliere una posizione a caso e scambiare il contenuto delle celle
- Mostrare all'utente la lista risultante, andando a capo per ogni riga

>

Usare una lista semplice, ma nella visualizzazione introdurre dei ritorni a capo

Cella a inizio riga: il suo indice `i` è multiplo di `cols`, ossia `i % cols == 0`
<br>
Cella a fine riga: `i % cols == cols - 1`

Per cominciare, inserire nella lista valori numerici crescenti, anzichè lettere

---

title: Es.: Scitala spartana
figure: images/hist/scytale.png

- Leggere un intero file di testo
- Inserire in una matrice i primi W×H caratteri
    - W colonne × H righe, valori prefissati
    - Riempire una riga della matrice dopo l'altra
    - Da destra a sinistra, una riga alla volta (→, ↓)
- Scrivere il contenuto della matrice su console
    - Scrivere una colonna della matrice dopo l'altra
    - Prima riga su console = prima colonna della matrice...
    - Dall'alto verso il basso, una colonna alla volta (↓, →)

>

Usare una lista di liste (con dimensioni predefinite)



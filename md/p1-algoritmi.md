title: Algoritmi in Python 3
subtitle: Introduzione alla programmazione
figure: images/algo/rubik-cube.png

---

title: Problem solving
figure: images/misc/problem-solving-cycle.svg
class: large-figure

- George Polya (1945). “_How to solve it_”
    - Soluzione di problemi matematici: processo raramente lineare <br>&nbsp;
- **(1) See.** Capire il problema
    - Quali sono i dati, quali le incognite?
    - Quali sono le condizioni? Sono soddisfacibili, ridondanti, contraddittorie?
    - Figure, notazione

> Make things as simple as possible, but not simpler. *(A. Einstein)*

> For every complex problem there is an answer that is clear, simple, and wrong. *(H.L. Mencken)*

---

title: Dal problema alla soluzione, e ritorno

- **(2) Plan.** Elaborare un piano
    - Mettere in relazione dati e incognite
    - Riduzione, analogia, divide et impera, composizione, astrazione...
    - *Computational thinking*
    - Cominciare a risolvere un problema *più semplice* (vincoli rilassati)
- **(3) Do.** Eseguire il piano
    - Controllare ogni passo. È corretto?
- **(4) Check.** Controllare la soluzione
    - Corretta? Ottenibile in altro modo?
    - Risultato, o metodo, utilizzabile per altri problemi?

> If you can't solve a problem... <br> then there is an easier problem you can solve: find it. *(G. Polya)*

---

title: Elementi di un algoritmo
figure: images/algo/recipe.png
figcaption: Una ricetta di cucina è un esempio di algoritmo

- *Algoritmo*: procedimento che risolve un determinato problema attraverso un numero finito di passi elementari (al-Khwarizmi, ~800)
- **Dati**: iniziali (istanza problema), intermedi, finali (soluzione)
- **Passi** elementari: azioni atomiche non scomponibili in azioni più semplici
- **Processo**, o anche esecuzione: sequenza ordinata di passi
- *Proprietà*: finitezza, non ambiguità, realizzabilità, efficienza...

> Computer science is no more about computers than astronomy is about telescopes. *(E. Dijkstra...)*

---

title: Ricerca in uno schedario
figure: images/algo/catalogue.png

- Es. in biblioteca: cercare la scheda di un certo libro
    - **(1)** *Finchè* restano delle schede da esaminare: si prende la prima scheda non ancora controllata
    - **(2)** *Se* autore e titolo sono quelli cercati: scheda trovata, ricerca conclusa!
    - **(3)** (Altrimenti...) <br> *Si ripete* il controllo (1), passando alla scheda successiva
    - **(4)** Esaurite le schede, il libro non è nella biblioteca!

---

title: Cercare più velocemente

- Su schedario *ordinato* si può fare più in fretta
    - **(1)** *Finchè* restano delle schede da esaminare: si prende tra loro la scheda centrale
    - **(2)** *Se* autore e titolo sono quelli cercati: scheda trovata, ricerca conclusa!
    - **(3)** *Altrimenti, se* autore e titolo vengono dopo quelli cercati: si scartano subito tutte le schede successive
    - **(4)** *Altrimenti, infine*: si scartano le schede precedenti
    - **(5)** *Si ripete* la ricerca sull'insieme dimezzato (1)
    - **(6)** Esaurite le schede, il libro non è nella biblioteca!

---

title: Complessità e calcolabilità

- **Complessità**: classificare algoritmi (e problemi)
    - **Trattabili**: costo accettabile, “polinomiale”
    - **Non trattabili**: costo “esponenziale”
- **Calcolabilità**: distinguere i problemi **non risolvibili**
    - Es. Valore di verità di `P`: *Questa frase è falsa*
    - Incompletezza Gödel; indecidibilità *terminazione*
    - ∀ formalizzazione della matematica che assiomatizza ℕ <br> → ∃ proposizione né dimostrabile né confutabile

---

title: Diagramma di flusso
figure: images/algo/origami.png
figcaption:Anche un origami è un esempio di algoritmo

- *Flow-chart*: Rappresentazione grafica di algoritmi
    - Più efficace e meno ambigua di una descrizione a parole
- Due tipi di entità:
    - Nodi
    - Archi
- È un *grafo orientato*
    - Passi di un algoritmo e loro sequenza


---

title: Tipi di nodi
figure: images/algo/spaghetti-flowchart.png

![](images/algo/nodes.svg)

- Istruzioni di I/O: es. leggere dati da tastiera o mostrarli a schermo
- Operazioni aritmetico-logiche
- Controllo del flusso di esecuzione

---

title: Programmazione strutturata
figure: images/algo/spaghetti-code.png

- Strutture di controllo:
    - **Sequenza**
    - **Selezione**
    - **Iterazione**

> Qualunque algoritmo può essere implementato utilizzando queste tre sole strutture *(Teorema di Böhm-Jacopini, 1966)*

> Goto statement considered harmful *(Dijkstra, 1968)*

---

title: Strutture di controllo

![](images/algo/structures.svg)

- Esempi quotidiani di `if` e `while`:
    - “*Se non c'è il lievito, usare due cucchiaini di bicarbonato*”
    - “*Battere gli albumi finché non montano*”

---

title: Blockly
class: large-image

![](images/algo/blockly.png)

>

<http://blockly-games.appspot.com/maze>

---

title: Linguaggio Python
class: segue dark

---

title: Python!

![](images/algo/antigravity.png)

---

title: Applicazioni in Python

![](images/algo/python-cases.jpg)

- Web, analisi di dati, scripting, insegnamento, giochi, hardware, multipiattaforma...

---

title: Tipi di dati

- Un **tipo di dato** specifica un insieme di *valori* e le *operazioni* ammesse
    - `int, float, bool, str`
    - Operazioni aritmetiche e logiche, confronti
- Una **variabile** serve per conservare un risultato

code: python

    3 + 4   # 7 - The result has to be handled...
    4 == 5  # False - Do not confuse with assignment!
    2 < 3 or not True  # True

code: python

    a = 5  # Assignment
    b = 2
    a = a + b

---

title: Valori numerici e booleani

- **`int`** o **`float`**, per numeri interi o reali
    - Operazioni di base: `+, -, *, /`
    - Divisione intera, resto, potenza: `//, %, **`
    - Assegnamento: `=, +=, -=, ...`
    - Confronti: `<, <=, >, >=, ==, !=`
-  **`bool`**, per valori booleani: `True, False`
    - Operazioni consentite: `and, or, not`
    - I confronti danno un risultato booleano

code: python

    -2 // 3    # -1 (floored integer division)
    -2 % 3     # 1 (reminder is always positive)
    2 ** 1000  # no limits (but memory)

---

title: Stringhe di testo

- **`str`** per sequenze di caratteri *Unicode*
- Primi 128 codici *Unicode* == *ASCII*
    - A capo: `'\n'` (10, o 13-10... ma conversione automatica)
    - Tabulazione: `'\t'` (9)
- Confronto tra stringhe, in ordine *lessicografico*
    - `<, <=, >, >=, ==, !=`

code: python

    str1 = "Monty Python's "
    str2 = 'Flying Circus'
    result = str1 + str2
    
    'first' < 'second'  # True (but... 'Second' <  'first')
    chr(90)             # 'Z'
    ord('Z')            # 90

---

title: Tabella ASCII
class: large-image

![](images/repr/ascii.png)

---

title: Leggere e scrivere
figure: images/algo/hello-user.svg

- **`input`** legge una riga di testo, inserita dall'utente, in una *variabile*
    - Prima mostra un messaggio
- **`print`** scrive una serie di valori su una riga
    - Tra i valori (parametri) viene inserito uno spazio

code: python

    user = input("What's your name? ")

    print("Hello,", user)

---

title: Somma di tre numeri
figure: images/algo/sum3.svg

code: python

    # File sum3.py - to run: python3 sum3.py

    a = int(input("Insert 1st val: "))
    b = int(input("Insert 2nd val: "))
    c = int(input("Insert 3rd val: "))

    total = a + b + c

    print("The sum is", total)

---

title: Variabile
figure: images/algo/var-label.svg

- **Nome** (etichetta) associato ad un certo **valore** (oggetto)
    - Oggetto assegnato a più variabili: non viene copiato, ma riceve più etichette
    - Il **tipo** dipende dal valore attualmente assegnato
    - Una var. non dev'essere *dichiarata*, ma dev'essere *inizializzata*

code: python

    x = 100
    DELTA = 5          # Constants: UPPER_CASE
    x = x + DELTA      # Variables: lower_case
    next_position = x  # Use explicative names!

---

title: Strutture di controllo
class: segue dark

---

title: Selezione: if

- **Indentazione** del corpo di `if` o `else`
    - Richiesta per sintassi, non opzionale!

> Readability counts *(The Zen of Python)*

code: python

    # File tooyoung.py - to run: python3 tooyoung.py

    age = int(input("Age? "))

    if age < 14:
        print("You're too young for driving a scooter...")
        print("But not for learning Python!")

- Clausola `else`: opzionale
    - Eseguita sse la condizione non è verificata

---

title: Valore assoluto
figure: images/algo/abs.svg

code: python

    x = int(input("insert a value: "))

    if x >= 0:
        y = x
        print(x, "is positive")
    else:
        y = -x
        print(x, "is negative")

    print("abs =", y)

- Corpo di `if` o `else`: qualsiasi istruzione
- Anche altri blocchi `if` o `while` annidati!

---

title: Calcolo dell'età

code: python

    birth_year = int(input("Birth year? "))
    birth_month = int(input("Birth month? "))
    birth_day = int(input("Birth day? "))
    current_year = int(input("Current year? "))
    current_month = int(input("Current month? "))
    current_day = int(input("Current day? "))

    if (current_month > birth_month
        or (current_month == birth_month and current_day >= birth_day)):
        age = current_year - birth_year
    else:
        age = current_year - birth_year - 1

    print("Your age is", age)

>

Espressione booleana composta con **`and`** e **`or`**

---

title: Confronto tra parole
figure: images/algo/words.svg

code: python

    a = input("First word? ")
    b = input("Second word? ")

    if a < b:
        print("The words are ordered")
    elif a > b:
        print("The words are inverted")
    else:
        print("The words are equal")

- **`elif`**: clausola `else` che contiene un altro `if`
- No `switch`, no `do-while`

> There should be one -- and preferably only one -- obvious way to do it *(ZoP)*


---

title: Operazioni aritmetiche
figure: images/algo/calc.svg

code: python

    a = float(input())
    b = float(input())
    op = input()

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/' and b != 0:
        print(a / b)
    else:
        print("Operation not allowed")

---

title: Iterazione: while
figure: images/algo/sum1n.svg

- Condizione booleana di *permanenza* nel ciclo
- Controllo *preliminare*, possibile che il corpo non sia mai eseguito

code: python

    # Sum of the numbers from 1 to n
    total = 0
    count = 1
    n = int(input("n? "))

    while count <= n:
        total = total + count
        count = count + 1

    print("The sum is", total)

<http://it.wikipedia.org/wiki/Gauss#Biografia>

---

title: Somma di N valori dell'utente
figure: images/algo/sumn.svg

code: python

    n = int(input("How many values? "))
    total = 0
    i = 0

    while i < n:
        val = int(input("Val? "))
        
        total += val  # total = total + val
        i += 1        # i = i + 1

    print("The sum is", total)

---

title: Ciclo con sentinella
figure: images/algo/average.svg

code: python

    total = 0
    count = 0

    val = int(input("Val? (0 to finish) "))
    
    while val != 0:
        total += val
        count += 1
        val = int(input("Val? (0 to finish) "))

    if count != 0:
        print("The average is", total / count)

---

title: Quadrato perfetto
figure: images/algo/perfect-square.svg

code: python

    n = 0
    while n <= 0:
        n = int(input("Positive val? "))

    ans = 1
    while ans * ans < n:
        ans += 1

    if ans * ans == n:
        print("Square root:", ans)
    else:
        print("Not a perfect square")

---

title: Moduli

- *Python Standard Library*: <http://docs.python.org/3/library/>

code: python

    import math
    y = math.sin(math.pi / 4)
    print(y)

code: python

    from math import sin, pi
    print(sin(pi / 4))

code: python

    from random import randrange
    n1 = randrange(90)  # something between 0 and 89
    n2 = randrange(90)  # possibly, a different number
    print(n1, n2)

>

Tutti gli `import` all'inizio dello script, per evidenziare le dipendenze

---

title: Esercizi
class: segue dark

---

title: Cerchio
figure: images/misc/greek-pi.png

- Chiedere all'utente il valore del raggio `r` di un cerchio
- Mostrare il valore dell'area e della circonferenza
- Se `r` è negativo, però, mostrare un messaggio d'errore

code: python

    from math import pi
    # `pi` is a constant defined in the `math` module

---

title: Minore e maggiore
figure: images/misc/three-brothers.png

- Chiedere all'utente tre numeri interi: `a`, `b`, `c`
- Determinare qual è il minore dei tre
- Determinare qual è il maggiore dei tre

>

Controllare prima di tutto se `a` è minore degli altri due <br>
Altrimenti controllare se `b` è minore di `c` <br>
Altrimenti ...

---

title: Cubi in ciclo
figure: images/misc/rock-cubes.png

- In un ciclo, ripetere le seguenti operazioni
    - Chiedere all'utente un numero
    - Mostrare il suo valore al cubo
    - Il valore 0 indica il termine della sequenza

---

title: Numero segreto
figure: images/misc/bingo-balls.png

- Generare un intero “segreto” a caso tra 1 e 90
- Chiedere ripetutamente all'utente di immettere un numero, finché non indovina quello generato
- Ad ogni tentativo, dire se il numero immesso è maggiore o minore del numero segreto

code: python

    from random import randint
    secret = randint(1, 90)
    # `randint` is a function defined in the `random` module

---

title: Lunghezza righe
figure: images/misc/measure-tape.png

- Leggere una sequenza di righe di testo, in un ciclo
- La sequenza termina con una riga vuota
- Visualizzare la lunghezza media delle righe

>

Lunghezza di una variabile `line` di tipo stringa: `len(line)`

---

title: Interesse composto
figure: images/misc/uncle-scrooge.png

- Dati dall'utente: capitale iniziale, tasso d'interesse, durata investimento
- Calcolare il capitale dopo ogni anno
- Es. 100€ al 4.5%: <br><br>

code: output

	Anno 0: 100.00€
	Anno 1: 104.50€
	Anno 2: 109.20€
	Anno 3: 114.12€ ...

>

Incolonnamento: `txt = '{:6.2f}'.format(val)` <br>
`txt` ha lunghezza ≥ 6, con 2 cifre decimali

---

title: Conteggio cifre
figure: images/misc/finger-counting.png

- Leggere un numero intero positivo
- Determinare di quante cifre è composto

>

Quante volte riusciamo a dividerlo per 10, prima che si annulli?

---

title: Resistenze, ciclo
figure: images/misc/resistors.png

- Leggere, attraverso un ciclo, una sequenza di valori di resistenze elettriche
- La sequenza termina quando l'utente immette il valore 0
- Alla fine, visualizzare la resistenza equivalente, sia nel caso di resistenze disposte in serie, che in parallelo

>

Formule utili:

R~~s~~ = ∑ R~~i~~

1/R~~p~~ = ∑ (1/R~~i~~)

---

title: La stanza del mostro
figure: images/misc/monster.png

- Il giocatore si muove su una scacchiera di 5x5 celle, partendo da un angolo
    - Le righe e le colonne sono numerate da 0 a 4
- Un tesoro ed un mostro sono nascosti due posizioni casuali, all'inizio del gioco
- Ad ogni turno, il giocatore:
    - Sceglie una direzione verso cui spostarsi (alto, basso, sinistra, destra)
    - Se capita sulla cella del tesoro, ha vinto
    - Se capita sulla cella del mostro, ha perso

code: python

    from random import randrange
    # ...
    monster_x = randrange(5)  # something between 0 and 4
    monster_y = randrange(5)  # something between 0 and 4



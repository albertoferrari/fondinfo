title: Liste e funzioni
subtitle: Introduzione alla programmazione
figure: images/fun/shopping-list.jpg

---

title: Lista
figure: images/fun/month-list.svg

- Sequenza di elementi, *di solito* dello stesso **tipo**
    - L'intera lista può essere assegnata ad una variabile, così diamo un **nome** alla lista
- I singoli elementi sono **numerati**
    - Gli indici partono da 0!
      
code: python

    to_buy = ["spam", "eggs", "beans"]
    
code: python

    rainfall_data = [13, 24, 18, 15]
    
code: python

    months = ["Jan", "Feb", "Mar",
              "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", 
              "Oct", "Nov", "Dec"]
    
---

title: Accesso agli elementi
figure: images/fun/wile-coyote.png

- **Attenzione ad usare indici validi!**
    - *Lunghezza* attuale di una lista `x`: `len(x)`
    - Elementi *numerati* da `0` a `len(x)-1`
    - Indici *negativi* contano dalla fine

code: python

    n = len(months)            # 12
    months[3]                  # "Apr"
    months[-2]                 # "Nov", same as n - 2

code: python

    to_buy = ["spam", "eggs", "beans"]
    
    to_buy[1] = "ketchup"      # replace an element

---

title: Appartenenza, inserimento, rimozione

code: python

    to_buy = ["spam", "eggs", "beans"]
    
    "eggs" in to_buy           # True, to_buy contains "eggs"

code: python

    to_buy.append("bacon")     # add an element to the end
    to_buy.pop()               # remove (and return) last element
    
    to_buy.insert(1, "bacon")  # other elements shift
    removed = to_buy.pop(1)    # remove (and return) element at index
    
    to_buy.remove("eggs")      # remove an element by value

---

title: Slice: porzioni di lista

code: python

    spring = months[2:5]       # ["Mar", "Apr", "May"]
    quart1 = months[:3]        # ["Jan", "Feb", "Mar"]
    quart4 = months[-3:]       # ["Oct", "Nov", "Dec"]
    whole_year = months[:]     # Copy the whole list

code: python

    list1 = ["spam", "eggs", "beans"]
    list2 = ["sausage", "mushrooms"]
    to_buy = list1 + list2     # List concatenation

code: python

    so_boring = [1, 2] * 3     # List repetition:
                               # [1, 2, 1, 2, 1, 2]
    results_by_month = [0] * 12

---

title: Uguaglianza e identità

code: python

    a = [3, 4, 5]
    b = a[:]       # b = [3, 4, 5] -- a new list!
    b == a         # True, they contain the same values
    b is a         # False, they are two objects in memory
                   # (try and modify one of them...) 
    c = a
    c is a         # True, same object in memory 
                   # (try and modify one of them...) 

---

title: Stringhe e liste

- **Stringa**: sequenza *immutabile* di caratteri
- **`join`** e **`split`**: da lista a stringa e viceversa

code: python

    txt = "Monty Python's Flying Circus"
    txt[0]    # 'M'
    txt[1]    # 'o'
    txt[-1]   # 's'
    txt[6:12] # "Python"
    txt[-6:]  # "Circus"

    days = ["tue", "thu", "sat"]
    txt = "|".join(days)  # "tue|thu|sat"

    days = "mon|wed|fri".split("|")
    # ["mon", "wed", "fri"]
    
---

title: Cicli su liste: for

code: python

    shopping_list = ["spam", "eggs", "bacon", "ketchup"]
        
    print("Your shopping list contains:")

    for product in shopping_list:
        print(product)
    
- Ad ogni iterazione, a `product` è assegnato un diverso elemento della lista `shopping_list`
- Si può usare un ciclo `for` su qualsiasi sequenza, anche su una *stringa*

---

title: Intervalli di valori: range
figure: images/algo/sum10.svg

- **`range`**: intervallo di valori aperto a destra
    - Estremo inferiore *incluso*
    - Estremo superiore *escluso*
    - Iterabile con un ciclo `for`

code: python

    # Add up numbers from 1 to 10
       
    total = 0
    for i in range(1, 11):
        total += i

    # total = 0;  i = 1
    # while i < 11:
    #     total += i;  i += 1
    
---

title: Cicli e annidamento
figure: images/misc/tables.png

code: python

    MAX = 12
    y = int(input("Insert a value: "))
    for x in range(1, MAX + 1):
        print(x * y, end = " ")
        # inserts a space, instead of a newline
    
code: python

    MAX = 12
    for y in range(1, MAX + 1):
        for x in range(1, MAX + 1):
            val = x * y
            print(val, end = " ")
        print()
    
Per fare in modo che ciascun valore richieda almeno 3 caratteri:
<br>
`val = "{:3}".format(x * y)`

---

title: Tupla

- Sequenza **immutabile** di valori, anche di *tipo diverso*

code: python

    # Tuple packing
    pt = 5, 6, "red"
    pt[0]  # 5
    pt[1]  # 6
    pt[2]  # "red"

    # multiple assignments, from a tuple
    x, y, colour = pt  # sequence unpacking
    a, b = 3, 4
    a, b = b, a
    
---

title: Brython
figure: images/misc/brython.png
figcaption: → brython.info

- *Transpiler*: converte codice Python in JavaScript
    - Sia traduttore che codice generato girano nel *browser*
- Useremo un modulo *ad-hoc*: `game2d`
    - Genera html e lancia web-server locale
    - Definisce funzioni di disegno
- Spesso i parametri sono tuple
    - *Color*: `(red, green, blue)` <br> Ogni componente nel range `0..255`<br>
    - *Point*: `(x, y)`<br>
    - *Size*: `(width, height)`<br>
    - *Rect*: `(left, top, width, height)`

---

title: Disegno nel browser
figure: images/oop/raster-coord.png

code: python

    from game2d import *

    # New canvas, width=600, height=400
    canvas = canvas_init((600, 400))

    # Yellow rectangle, left=100, top=150, w=250, h=200
    # red=255 (max), green=255 (max), blue=0 (min)
    draw_rect(canvas, (255, 255, 0), (100, 150, 250, 200))
    
    # Blue circle, center=(100, 150), radius=20
    draw_circle(canvas, (0, 0, 255), (100, 150), 20)

Servono i file `brython_dist.js` e `game2d.py`, in `examples`: <br>
<https://github.com/tomamic/fondinfo/archive/master.zip>

---

title: Sequenza di quadrati
figure: images/misc/red-squares.png

code: python

    from game2d import *

    canvas = canvas_init((300, 300))

    for i in range(5):
        x = i * 40
        y = x
        red = i * 60
        draw_rect(canvas, (red, 0, 0), (x, y, 140, 140))

Servono i file `brython_dist.js` e `game2d.py`, in `examples`: <br>
<https://github.com/tomamic/fondinfo/archive/master.zip>

---

title: Animazione

code: python

    from game2d import *

    def update():
        global x
        canvas_fill(canvas, (255, 255, 255))  # Draw background        
        image_blit(canvas, image, (x, 50))    # Draw foreground
        x = (x + 5) % 320                     # Update ball's position

    canvas = canvas_init((320, 240))
    image = image_load("ball.png")
    x = 50

    set_interval(update, 1000 // 30)    # Call update 30 times/second

---

title: Eventi della tastiera

code: python

    from game2d import *

    def keydown(event: DOMEvent):
        print("Key down: ", event.key, event.code)

    def keyup(event: DOMEvent):
        print("Key up: ", event.key, event.code)

    doc.onkeydown = keydown
    doc.onkeyup = keyup

<https://developer.mozilla.org/es/docs/Web/API/KeyboardEvent>

---

title: Es.: Conteggio cifre
figure: images/misc/numbers.jpg

- Chiedere una riga di testo all'utente
- Contare il numero complessivo di cifre presenti (da `'0'` a `'9'`)
- Valutare anche la somma di tutte le singole cifre trovate

>

Usare un ciclo `for` sulla stringa (sequenza di caratteri)

---

title: Es.: Conteggio di diversi caratteri
figure: images/misc/characters.png

- Chiedere una riga di testo all'utente
- Contare separatamente le occorrenze di ciascuna lettera maiuscola (da `'A'` a `'Z'`)

>

Creare una lista (array) di 26 elementi, inizialmente tutti posti a `0`

Ciascun elemento è il contatore per una certa lettera

L'indice del contatore corrispondente ad una lettera `val` può essere ottenuto come `ord(val) - ord('A')`

---

title: Es.: Array, precalcolo
figure: images/misc/sin-cos.png

- Riempire una lista con i valori di `sin(x)`
    - 360 elementi, indice `x` tra 0 e 359
- Chiedere ripetutamente un angolo all'utente, visualizzare il corrispondente valore precalcolato

>

`sin`, `pi` in modulo `math`
<br>
`sin` opera su radianti: `rad = x * pi / 180`

Estensione opzionale: salvare la lista di valori in un file e ricaricarla all'avvio, se già disponibile

---

title: Es.: Cerchi concentrici
figure: images/misc/red-circles.png

- Chiedere all'utente il numero di cerchi da disegnare
- Disegnare i cerchi con raggio decrescente, ma tutti con lo stesso centro
- Far variare il colore dei cerchi
	- Dal rosso del livello più esterno
	- Fino al nero del livello più interno

>

Cominciare a disegnare un grosso cerchio rosso

Poi, inserire l'operazione di disegno un ciclo, togliendo ad ogni passo `10` (p.es.) al raggio e al livello di rosso

Infine, determinare automaticamente, prima del ciclo, le variazioni migliori per raggio e colore

---

title: Es.: Griglia di colori
figure: images/misc/color-grid.png images/oop/raster-tile.png

- Chidere all'utente dei valori per `rows` e `cols`
- Mostrare una griglia di rettangoli di dimensione `rows×cols`
- Partire da un rettangolo nero in alto a sinistra
- In orizzontale, aumentare gradatamente la componente di blu
- In verticale, aumentare gradatamente la componente di verde

>

Cominciare a creare una griglia di riquadri tutti neri, con due cicli `for` annidati

Lasciare tra i riquadri un piccolo margine

---

title: Funzioni
class: segue dark

---

title: Definizione di funzioni
figure: images/fun/function.png

- Operatore, applicato a operandi, per ottenere un risultato

    - **`def`** per definire una funzione
    - **`return`** per terminare e restituire un risultato

code: python

    def hypotenuse(a, b):
        c = (a ** 2 + b ** 2) ** 0.5
        return c

    def limit_values(values, max_val):
        # procedure: process data, no direct result
        for i in range(len(values)):
            if values[i] > max_val:
                values[i] = max_val

        # the pythonic way: for i, val in enumerate(values): ...

---

title: Chiamata di funzioni

- **`def`** definisce una funzione, ma non la esegue!
- Bisogna *chiamarla*
- Ogni funzione, quando eseguita, crea un nuovo *spazio di nomi*
    - Parametri e variabili hanno **ambito locale**
    - Non visibili nel resto del programma
    - Anche nomi uguali, definiti in ambiti diversi, restano distinti
    
code: python

    side1 = float(input('1st side? '))
    side2 = float(input('2nd side? '))
    side3 = hypotenuse(side1, side2)
    print('3rd side:', side3)

    data = [5, 4, 2]
    limit_values(data, 4)
    print(data)

---

title: Parametri di funzioni

- **Parametri formali**: nomi usati nella *definizione*
- **Parametri effettivi**: oggetti passati alla funz.
- Parametri passati &ldquo;*per oggetto*&rdquo;
    - Variabili all'esterno: non vengono modificate
    - Liste e oggetti passati ad una funz.: modifiche *permanenti*
- Si possono restituire più valori, come *tupla*
    - `return 7, 5, 'black'`

code: python

    def inc(a):
        a += 1
        print(a)  # just for debug
    x = 10
    inc(x)
    print(x)      # just for debug

---

title: Funzione main

- A volte si preferisce creare una funzione principale
    - In questo modo si limitano le variabili globali

code: python
  
    # def hypotenuse ...

    def main():
        side1 = float(input("1st side? "))
        side2 = float(input("2nd side? "))
        side3 = hypotenuse(side1, side2)
        print("3rd side:", side3)

    main()
    
---

title: Modulo main

- Nome del modulo in esecuzione: `__name__`
    - É il nome del file, senza estensione
    - Modulo che avvia l'app ha nome speciale `"__main__"`

code: python
  
    # def hypotenuse ...

    def main():
        side1 = float(input("1st side? "))
        side2 = float(input("2nd side? "))
        side3 = hypotenuse(side1, side2)
        print("3rd side:", side3)

    if __name__ == "__main__":
        main()
    
---

title: Documentazione di funzioni

- **Annotazioni**: utili per documentare il tipo di param. e valore di ritorno (ma non c'è verifica!)
- **Docstring**: descrizione testuale di una funzione
- **`help`**: funzione per visualizzare la documentazione

code: python

    def hypotenuse(cathetus1: float, cathetus2: float) -> float:
        '''
        Return the hypotenuse of a right triangle,
        given both its legs (catheti).
        '''
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5

---

title: Effetti collaterali

- Modifica di oggetti passati come parametri o variabili globali, operazioni di lettura/scrittura...
- Annullano la **trasparenza referenziale**
    - Impossibile semplificare, sostituendo una chiamata a funzione col suo valore di ritorno (es. presenti operazioni di I/O)
- Rendono la funzione **non idempotente**
    - Chiamata più volte, con gli stessi parametri, restituisce risultati diversi
- → Difficile fare verifiche matematiche
    - `z = f(sqrt(2), sqrt(2))`
    - `s = sqrt(2)` <br> `z = f(s, s)`

---

title: Funzioni non idempotenti

- Esempio di semplificazione
    - `p = rq(x) + rq(y) * (rq(x) – rq(x))`
    - `p = rq(x) + rq(y) * (0)`
    - `p = rq(x) + 0`
    - `p = rq(x)`
- Ma se `rq` ha effetti collaterali, non si può!

code: python

    base_value = 0  # global variable

    def rq(x: int) -> int:
        global base_value
        base_value += 1
        return x + base_value

---

title: Esercizio - Area di un'ellisse
figure: images/misc/ellipse.svg

- Definire una funzione che:
    - Riceve come parametri i semiassi di una ellisse: `a`, `b`
    - Restituisce l'area dell'ellisse: `A = π*a*b`
- Nel `main`
    - Chiedere ripetutamente all'utente una coppia di valori
    - Invocare ogni volta la funzione con i valori inseriti dall'utente
    - Visualizzare il risultato



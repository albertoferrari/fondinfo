title: Sistema binario
subtitle: Introduzione all'informatica
figure: images/repr/binary-fingers.svg

---

title: Analogico e digitale
figure: images/repr/analog-clock.png images/repr/digital-clock.png

- Una grandezza (fisica o astratta) può essere rappresentata in due forme
    - **Analogica**: insieme di valori **continuo** (*denso e “senza buchi”*)
    - **Digitale** (o numerica): insieme di valori **discreto** (*tutti i punti sono isolati*)

---

title: Approssimazione discreta

- Alcune informazioni sono intrinsecamente discrete
    - Informazioni “artificiali”, es. un testo scritto
    - Scala atomica o subatomica …
- Molte grandezze fisiche hanno forma continua
    - Per loro elaborazione al calcolatore: rappresentazione digitale
    - *Approssimazione* del valore analogico
    - Errore dipende dalla precisione della rappresentazione digitale scelta

---

title: Codice

- Sistema basato su simboli, che permette la rappresentazione dell’informazione
- *Simbolo*: elemento atomico
- *Alfabeto*: insieme dei simboli possibili (`A`)
- *Cardinalità* del codice: numero di simboli dell’alfabeto
- *Stringa*: sequenza di simboli (`s ∈ A*`)
- *Linguaggio*: insieme stringhe ben formate (`L ⊆ A*`)

---

title: Codice posizionale
figure: images/repr/child-fingers.png

- Un numero naturale può essere rappresentato con una notazione posizionale
- `N = c~~0~~ · base^^0^^ + c~~1~~ · base^^1^^ + … + c~~n~~ · base^^n^^`
    - Es. `587~~10~~ = 7·10^^0^^ + 8·10^^1^^ + 5·10^^2^^`
- Sistemi di numerazione posizionali di uso comune
    - Decimale (base 10; c: `0-9`)
    - Binario (base 2; c: `0-1`)
    - Esadecimale (base 16; c: `0-9, A-F`)

---

title: Codifica dell’informazione

- Codifica: regole di corrispondenza per passare da un certo codice ad un altro
- Corrispondenza biunivoca
    - Tra una stringa di un codice
    - E una stringa di un altro codice
- Ad una certa stringa in un alfabeto ricco di simboli, corrisponde una stringa più lunga in un alfabeto più ridotto

---

title: Numeri binari
class: segue dark

---

title: Codice binario
figure: images/repr/sum-binary.jpg

- Base 2; c: `0-1`
- Informazione digitale nei calcolatori rappresentata con una sequenza di 0 e 1
    - Leibniz, ~1700
    - Konrad Zuse, ~1940
- Ogni elemento di una sequenza binaria viene detto *bit*
- Una sequenza di 8 bit viene detta *byte*

---

title: Codifica decimale → binaria
class: large-table

- (1) Dividere il numero decimale per 2
- (2) Assegnare il resto come valore del bit *(loop)*
- Ossia continuare a dividere per 2 il quoziente, finché non si annulla
- Es.: `35~~10~~ = 00100011~~2~~`

n  | n // B | n % B | peso
---|-----|-----|-------
35 |  17 |   1 | 1 = 2^^0^^
17 |   8 |   1 | 2 = 2^^1^^
 8 |   4 |   0 | 4 = 2^^2^^
 4 |   2 |   0 | 8 = 2^^3^^
 2 |   1 |   0 | 16 = 2^^4^^
 1 |   0 |   1 | 32 = 2^^5^^

---

title: Numeri naturali
figure: images/repr/binary-fingers.svg
figcaption: ... 819

- Rappresentare un numero naturale `N` in forma binaria
- Occorrono `K` bit, t.c. `2^^K^^ > N`
- Es. 4 bit per numeri naturali da 0 a 15
- Un calcolatore assegna un numero fisso di bit per diversi tipi di informazione
    - Casi di valori non rappresentabili
    - **Overflow**, **underflow**

---

title: Esadecimale (Hex)
class: large-table

  Dec  | Bin       | Hex |   Dec  | Bin       | Hex |   Dec  | Bin       | Hex
-------|-----------|-----|--------|-----------|-----|--------|-----------|----
**00** | 0000 0000 |  00 | **16** | 0001 0000 |  10 | **32** | 0010 0000 |  20 
**01** | 0000 0001 |  01 | **17** | 0001 0001 |  11 | **33** | 0010 0001 |  21
**02** | 0000 0010 |  02 | **18** | 0001 0010 |  12 | **34** | 0010 0010 |  22
**03** | 0000 0011 |  03 | **19** | 0001 0011 |  13 | **35** | 0010 0011 |  23
**04** | 0000 0100 |  04 | **20** | 0001 0100 |  14 | **36** | 0010 0100 |  24
**05** | 0000 0101 |  05 | **21** | 0001 0101 |  15 | **37** | 0010 0101 |  25
**06** | 0000 0110 |  06 | **22** | 0001 0110 |  16 | **38** | 0010 0110 |  26
**07** | 0000 0111 |  07 | **23** | 0001 0111 |  17 | **39** | 0010 0111 |  27
**08** | 0000 1000 |  08 | **24** | 0001 1000 |  18 | **40** | 0010 1000 |  28
**09** | 0000 1001 |  09 | **25** | 0001 1001 |  19 | **41** | 0010 1001 |  29
**10** | 0000 1010 |  0A | **26** | 0001 1010 |  1A | **42** | 0010 1010 |  2A
**11** | 0000 1011 |  0B | **27** | 0001 1011 |  1B | **43** | 0010 1011 |  2B
**12** | 0000 1100 |  0C | **28** | 0001 1100 |  1C | **44** | 0010 1100 |  2C
**13** | 0000 1101 |  0D | **29** | 0001 1101 |  1D | **45** | 0010 1101 |  2D
**14** | 0000 1110 |  0E | **30** | 0001 1110 |  1E | **46** | 0010 1110 |  2E
**15** | 0000 1111 |  0F | **31** | 0001 1111 |  1F | **47** | 0010 1111 |  2F

---

title: Bin ↔ Hex
figure: images/repr/4bits.png

![](images/repr/bin-hex.png)

- Ogni gruppo di 4 bit: 16 configurazioni diverse (2^^4^^ = 16)
- Ciascuna combinazione corrisponde ad uno dei 16 simboli esadecimali

---

title: Somma e sottrazione

code: Binary

        1   1
    0 0 0 1 0 1 1 0 +
    0 0 0 1 0 1 0 1 =
    -----------------
    0 0 1 0 1 0 1 1

code: Binary

                0 10
    0 0 0 0 1 1 1 0 -
    0 0 0 0 0 1 0 1 =
    -----------------
    0 0 0 0 1 0 0 1
    
Attenzione a riporto e prestito (in alto)

---

title: Moltiplicazione

code: Binary

            1 0 1 1 x
            1 1 0 1 =
            ---------
            1 0 1 1 +
          0 0 0 0
        -------------
          0 1 0 1 1 +
        1 0 1 1
      ---------------
        1 1 0 1 1 1 +
      1 0 1 1
    -----------------
    1 0 0 0 1 1 1 1

---

title: Divisione

code: Binary

    1 0 1 1 0 1 : 1 1
    0 0          ---------
    -----         0 1 1 1 1
    1 0 1 -
      1 1
    -------
      1 0 1 -
        1 1
      -------
        1 0 0 -
          1 1
        -------
            1 1 -
            1 1
            -----
            0 0

---

title: Numeri interi

- Occorre rappresentare anche i numeri negativi
    - Necessario riservare un bit per il segno
    - Ovvero, si dimezza il massimo modulo ammesso
- **Modulo e segno**
    - Il primo bit indica il segno
    - 0 positivo, 1 negativo

---

title: Complemento a due
figure: images/repr/4bits-sign.png

- Rappresentazione alternativa, *diversa da modulo e segno!*
- Numero negativo, ottenuto dal suo opposto positivo
    - Complemento il numero <br> (cambio gli 1 con 0 e viceversa)
    - Sommo 1
- Anche così, il primo bit indica il segno
    - 0 positivo, 1 negativo 
- *Attenzione*: bisogna conoscere codifica e num bit
    - Esempi seguenti: ogni intero con segno memorizzato in un singolo byte

---

title: Es. numero intero

- Avendo *un byte*, +35 è in binario: **`0`**`0100011`
- Numero –35, in modulo e segno: **`1`**`0100011`
- Numero –35, in complemento a due: **`1`**`1011101`

code: Binary

    0 0 1 0 0 0 1 1 ¬
    -----------------
    1 1 0 1 1 1 0 0 +
                  1 =
    -----------------
    1 1 0 1 1 1 0 1

`¬`: complemento semplice, bit a bit

---

title: Somma con segno

- Sommare 12 e -35 su 8 bit, modulo e segno
    - Sottrazione tra 35 e 12
    - Cambio di segno
- Stessa operazione, complemento a due
    - Semplice somma: `12 + -35 = -23`

code: Binary

    0 0 0 0 1 1 0 0 +
    1 1 0 1 1 1 0 1 =
    -----------------
    1 1 1 0 1 0 0 1

---

title: Numeri reali

- Insieme continuo, per grandezze analogiche
    - Rappresentabili solo in modo approssimato
- Parte frazionaria:
    - `F = c~~-1~~ · base^^-1^^ + … + c~~-n~~ · base^^-n^^`
- Due rappresentazioni *alternative*
    - **Virgola fissa**: segno, parte intera, parte decimale
    - **Virgola mobile**: segno, mantissa, esponente

---

title: Parte frazionaria in binario
class: large-table

- Moltiplicare la parte frazionaria per 2
- Assegnare la parte intera del risultato come valore del bit *(loop)*
- Ossia: continuare a moltiplicare per 2 la parte frazionaria del risultato... <br> finché non si annulla

fract | fract*B | int | peso
------|---------|-----|--------
0,375 | 0,750   | 0   | 2^^-1^^
0,750 | 1,500   | 1   | 2^^-2^^
0,500 | 1,000   | 1   | 2^^-3^^

---

title: Virgola fissa

- Numero espresso come: `r = (i, f)`
    - **`i`** è la parte intera, `n~~1~~` bit
    - **`f`** è la parte frazionaria, `n~~2~~` bit
- Precisione costante lungo l’asse reale
    - P.es. `f` di 3 bit, valori consecutivi sempre distanziati di 1/8
    - Tra ciascun intero e il successivo, possiamo rappresentare 8 valori

![](images/repr/fixed-point.png)

---

title: Virgola mobile
class: large-image

- Numero espresso come: `r = ±(1+f)·2^^e^^`
    - **`e`** è l'esponente intero (o caratteristica), `n~~1~~` bit
    - **`f`** è la parte frazionaria *(0 ≤ f < 1)*, `n~~2~~` bit
    - `2` è la base, `1+f` è anche detto *mantissa*
- Precisione variabile lungo l’asse reale; p.es.:
    - `f ∈ {0, 1/4, 2/4, 3/4}`, 2 bit <br> `e ∈ {-2, -1, 0, 1}`, 2 bit

![](images/repr/float4.png)

>

<http://www.mathworks.com/company/newsletters/news_notes/pdf/Fall96Cleve.pdf>

---

title: IEEE 754

- `-118.625 = -1110110.101~~2~~ = -1.110110101~~2~~ × 2^^6^^`
- All’esponente, su 8 bit, bisogna sommare `127` (`=2^^8 − 1^^ − 1`)

![](images/repr/ieee754-32-ex.svg)
![](images/repr/ieee754-32.svg)
![](images/repr/ieee754-64.svg)

---

title: Algebra di Boole
class: segue dark

---

title: Algebra di Boole

- L’algebra di Boole è un formalismo che opera su variabili (dette *variabili booleane*)
- Le variabili booleane possono assumere due soli valori: `vero`, `falso`
- Sulle variabili booleane è possibile definire delle funzioni (dette *funzioni booleane*)
- Anche le funzioni booleane possono assumere solo i due valori `vero` e `falso`

---

title: Funzione e tabella di verità
class: large-table

- Una *tabella di verità* permette di definire una *funzione booleana*
- Valore risultante per ciascuna combinazione dei valori in ingresso
- A volte, *specifica incompleta* (certe combinazioni di ingressi non possono verificarsi) → Non è specificato alcun valore

 A | B | C | F~~1~~
---|---|---|---
 0 | 0 | 0 | 1
 0 | 0 | 1 | 0
 0 | 1 | 0 | 0
 0 | 1 | 1 | 1
 1 | 0 | 0 | 0
 1 | 0 | 1 | 1
 1 | 1 | 0 | 1
 1 | 1 | 1 | 1

---

title: Espressione booleana
figure: images/repr/hair-logic.svg

- Algebra di Boole: basata su un insieme di operatori
- Possono essere combinati in espressioni
- Altra forma di definizione di funzioni booleane
- Es. `F~~2~~(A, B, C) = A·B + C`

Operatore | Simbolo
----------|--------
And       | · (∧)
Or        | + (∨)
Not       | ¬
Xor       | ⊕
Nand      | ↑
Nor       | ↓
---

title: Operatori principali
class: large-table

A | B | A·B | A+B | A⊕B | A↑B | A↓B
--|---|-----|-----|-----|-----|----
0 | 0 | 0   | 0   | 0   | 1   | 1
0 | 1 | 0   | 1   | 1   | 1   | 0
1 | 0 | 0   | 1   | 1   | 1   | 0
1 | 1 | 1   | 1   | 0   | 0   | 0

A | ¬A
--|---
0 | 1
1 | 0

---

title: Proprietà degli operatori 
class: large-table

Proprietà    | Not
-------------|--------
Complemento  | ¬¬A = A

Proprietà    | And                       | Or
-------------|---------------------------|--------------------------
Commutativa  | A · B = B · A             | A + B = B + A
Associativa  | (A·B) · C = A · (B·C)     | (A+B) + C = A + (B+C)
Distributiva | A + (B·C) = (A+B) · (A+C) | A · (B+C) = (A·B) + (A·C)
Idempotenza  | A · A = A                 | A + A = A
Identità     | A · 1 = A                 | A + 0 = A
Del limite   | A · 0 = 0                 | A + 1 = 1
Assorbimento | A · (A + B) = A           | A + (A · B) = A
Inverso      | A · ¬ A = 0               | A + ¬A = 1
De Morgan    | ¬(A·B·C…) = ¬A + ¬B + ¬C… | ¬(A+B+C…) = ¬A · ¬B · ¬C…

>

Attenzione a De Morgan: errore comune!

---

title: Forme canoniche
class: large-table

- **Somma di Prodotti (SP)**: si considerano le righe a 1
    - `F~~1~~(A, B, C) = (¬A·¬B·¬C) + (¬A·B·C) + (A·¬B·C) + (A·B·¬C) + (A·B·C)`
- **Prodotto di Somme (PS)**: si considerano le righe a 0
    - `F~~1~~(A, B, C) = (A + B + ¬C) · (A + ¬B + C) · (¬A + B + C)`

 A | B | C | F~~1~~ | → Forma canonica...
---|---|---|---|-----
 0 | 0 | 0 | 1 | → SP
 0 | 0 | 1 | 0 | → PS
 0 | 1 | 0 | 0 | → PS
 0 | 1 | 1 | 1 | → SP
 1 | 0 | 0 | 0 | → PS
 1 | 0 | 1 | 1 | → SP
 1 | 1 | 0 | 1 | → SP
 1 | 1 | 1 | 1 | → SP

---

title: Operazioni bit a bit in Python

code: Python

    x, y, z, shift = 0, 0, 0, 0  # some int values
    x << shift  # x = x * (2^shift)
    x >> shift  # x = x / (2^shift), con segno
    x & y       # AND applicato bit a bit
    x | y       # OR applicato bit a bit
    x ^ y       # XOR bit a bit
    ~x          # complemento di ogni bit

    z = 0x0B    # hex value (11 dec)
    z = 0b1011  # bin value (11 dec)
    
    hex(11)     # '0x0b' (text)
    bin(0x0B)   # '0b1011' (text)

Da non confondere con operatori logici (and, or, not)



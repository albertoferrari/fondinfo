title: Complessità computazionale
subtitle: Introduzione all'informatica
figure: images/comp/chess.jpg

---

title: Problemi e complessità

- Problemi *non risolvibili*
    - Es. Questa frase è falsa
    - Incompletezza Gödel; indecidibilità terminazione
- Risolvibili
    - *Non trattabili* (costo “esponenziale”)
    - Trattabili (costo accettabile, “polinomiale”) <br> &nbsp;
- **Calcolabilità**: classificare risolvibili e non risolvibili
- **Complessità**: “facili” e “difficili”

---

title: Ricerca lineare

code: Python

    def linear_search(v: list, value) -> int:
        '''v: not necessarily sorted'''

        for i in range(len(v)):
            if v[i] == value:
                return i

        return -1

---

title: Ricerca binaria

code: Python

    def binary_search(v: list, value) -> int:
        '''v: sorted list'''

        begin, end = 0, len(v)
        while begin < end:
            middle = (begin + end) // 2
            if v[middle] > value:
                end = middle
            elif v[middle] < value:
                begin = middle
            else:
                return middle

        return -1

---

title: Costo di un algoritmo

- **Spazio**, memoria richiesta
- **Tempo**, necessario all'esecuzione <br> &nbsp;
- Di solito si contano i cicli, in funzione di `n`
- O i confronti/scambi tra elementi dell'array
    - Array in memoria centrale, accesso lento
    - Altre variabili nei registri del processore
- Test e misure empiriche

>

<http://www.stroustrup.com/Software-for-infrastructure.pdf#5>

<https://www.youtube.com/watch?v=YQs6IC-vgmo>

---

title: Confronto tra algoritmi

- Caso peggiore negli algoritmi di ricerca: elemento non presente
- Ricerca lineare: `n` confronti
- Ricerca binaria: `⌈log~~2~~(n)⌉` confronti
    - A ogni iterazione l'insieme è dimezzato
    - Quante volte `n` dev'essere diviso per `2`, per arrivare a `0`?
    - `2^^k^^ ≥ n → k ≥ log~~2~~(n)`

---

title: Def. di complessità

- Una funzione `f(n)` ha *ordine* `O(g(n))` sse:
    - Esistono due costanti positive `c` ed `m`, tali che
    - `|f(n)| ≤ c|g(n)| ∀ n > m`
- Un algoritmo ha una *complessità* `O(g(n))` sse:
    - Il tempo di calcolo `t(n)`, sufficiente per eseguire l'algoritmo con ogni istanza(*) di dimensione `n`, ha ordine `O(g(n))`

>

(*) Istanza: insieme di dati su cui è definito il problema; quindi per la complessità conta il caso peggiore

---

title: Analisi asintotica
figure: images/comp/orders.svg

- Per `n` abbastanza grande, a meno di una costante moltiplicativa, `f(n)` non supera in modulo `g(n)`
- Comportamento dell'algoritmo al limite, per dimensione delle istanze tendente all'infinito
- Es. n = 1 000 000
    - Ricerca lineare: 1'000'000 cicli
    - Ricerca binaria: 20 cicli

---

title: Complessità intrinseca

- Limite inferiore di complessità di un problema
- Una funzione `f(n)` è `Ω(g(n))` sse
    - Esistono due costanti positive `c` e `m` tali che
    - `|f(n)| ≥ c|g(n)| ∀ n > m`
- Un problema ha una *delimitazione inferiore* alla complessità `Ω(g(n))` sse
    - Per ogni algoritmo risolutore…
    - ∃ una istanza (caso peggiore)…
    - per cui il tempo di calcolo `t(n)` è `Ω(g(n))`

---

title: Algoritmo ottimale

- Algoritmo che risolve un problema P, con le due seguenti condizioni:
    - Costo di esecuzione `O(g(n))`
    - P ha una delimitazione inferiore `Ω(g(n))`
- Es. L'algoritmo della ricerca binaria è ottimale
    - È dimostrato che `log~~2~~(n)` è la complessità intrinseca della ricerca
    - Ma ricerca lineare funziona anche per liste non ordinate!

---

title: Algoritmi di ordinamento
class: segue dark

---

title: Algoritmi di ordinamento

- Ricerca binaria: importante avere dati ordinati
    - Ordinateur, ordenador
- Algoritmi di ordinamento più semplici hanno complessità `n^^2^^`
    - Confronto tra ciascun elemento e gli altri
- Algoritmi di ordinamento *divide et impera*
    - Complessità `n·log~~2~~(n)`
    - Complessità instrinseca

---

title: Bubble sort
figure: images/comp/bubble-sort.png
class: large-figure

code: Python

    def swap(v: list, i: int, j: int):
        v[i], v[j] = v[j], v[i]

    def bubble_sort(v: list):
        end = len(v) – 1
        while end > 0:
            for i in range(end):
                if v[i] > v[i + 1]:
                    swap(v, i, i + 1)
            end -= 1

---

title: Analisi Bubble Sort

- Gli elementi maggiori salgono rapidamente, *“come bollicine di champagne”*
- Caso peggiore: lista rovesciata
    - Numero di confronti e scambi: `n^^2^^/2`
    - `(n-1)+(n-2)+...+2+1 = n(n-1)/2 = n^^2^^/2 - n/2 ≈ n^^2^^/2`
    - (Applicata la formula di Gauss per la somma dei primi numeri)
    - Complessità `n^^2^^`
- Anche in media, circa stessi valori

---

title: Selection Sort
figure: images/comp/selection-sort.png
class: large-figure

code: Python

    def selection_sort(v: list):
        for i in range(len(v) – 1):
            min_pos = i

            for j in range(i + 1, len(v)):
                if v[j] < v[min_pos]:
                    min_pos = j

            swap(v, pos_min, i)

---

title: Analisi Selection Sort

- Ad ogni ciclo principale, si seleziona il valore minore
- Caso peggiore: lista rovesciata
    - Numero di confronti `n·(n-1)/2`; complessità `n^^2^^`
    - Numero di scambi: `n-1` scambi
- Anche in media, circa stessi valori

>

Numero di confronti: (n - 1) + (n - 2) + (n - 3) + ... + 0 <br> Si applica Gauss

---

title: Insertion sort
figure: images/comp/insertion-sort.png
class: large-figure

code: Python

    def insertion_sort(v: list):
        for i in range(1, n):
            value = v[i]

            for j in range(i – 1, -1, -1):
                if v[j] <= value: break
                v[j + 1] = v[j]

            v[j + 1] = value

---

title: Analisi Insertion Sort

- La prima parte è ordinata, vi si inserisce un elemento alla volta, più facile trovare il posto
- Caso peggiore: lista rovesciata
    - Cicli: `1+2+...+(n-1) = n·(n-1)/2`; compl: `O(n^^2^^)`
- In media si scorre solo 1/2 della prima parte
    - In media `n^^2^^/4` confronti e `n^^2^^/4` scambi
- Ottimizzazioni
    - Ricerca binaria in parte ordinata, ma scambi
    - Inserimento a coppie, o gruppi

---

title: Quick Sort
figure: images/comp/quick-sort.png
class: large-figure

code: Python

    def quick_sort(v: list, begin=0, end=len(v)):
        if end - begin > 1:
            pivot = v[end – 1]
            j = begin
            for i in range(begin, end – 1):
                if v[i] < pivot:
                    swap(v, i, j)
                    j += 1
        swap(v, end – 1, j)
        quick_sort(v, begin, j)
        quick_sort(v, j + 1, end)

---

title: Analisi Quick Sort

- Dato un insieme, sceglie un valore `pivot`
- Crea due sottoinsiemi: `x ≤ pivot`, `x > pivot`
- Stesso algoritmo sui 2 insiemi (ricorsione)
- Caso peggiore: lista rovesciata, `n^^2^^`
    - Dipende da scelta pivot, ma esiste sempre
- Caso medio: `n·log~~2~~(n)`
    - `t(n) = α·n + 2·t(n/2)`
    - Sostituzione `k` volte: `t(n) = α·k·n + 2^^k^^t(n/2^^k^^)` …

---

title: Merge Sort

code: Python

    def merge_sort(v, begin=0, end=len(v)):
        '''In v, sort elements in range(begin, end)'''
        if end - begin > 1:
            middle = (begin + end) / 2
            merge_sort(v, begin, middle)
            merge_sort(v, middle, end)
            merge(v, begin, middle, end)

![](images/comp/merge-sort.png)

---

title: Merge, con appoggio

code: Python

    def merge(v, begin, middle, end):
        '''Merge two sorted portions of a single list'''
        i1, i2, n = begin, middle, end - begin
        result = []

        for k in range(n):
            if i1 < middle and (i2 >= end or v[i1] <= v[i2]):
                result.append(v[i1])
                i1 += 1
            else:
                result.append(v[i2])
                i2 += 1

        for k in range(n):
            cards[begin + k] = result[k]

---

title: Analisi Merge Sort

- Simile a Quick Sort, ma non si sceglie pivot
- La fusione ha complessità lineare
- Caso peggiore, caso medio: `n·log~~2~~(n)`
- **Spazio**: la fusione richiede altra memoria: `n`
    - Ma si può evitare il costo con spostamenti *in place*
- Accessi sequenziali, buon uso *cache*
- Integraz. con Insertion Sort (Python, Java7)

---

title: Classi di complessità
class: segue dark

---

title: Classi di complessità
figure: images/comp/orders.svg

- Costante: numero op. non dipende da `n`, dim. istanza
- Sotto-lineare: `n^^k^^`, `k<1`; `log(n)`, ricerca binaria
- Lineare: numero op. `∝ n`, ricerca lineare
- Sovra-lineare: `n·log(n)`, merge sort
- Polinomiale: `n^^k^^, k≥2`, insertion sort <br> &nbsp;
- **Algoritmo efficiente**: fino a classe polinomiale
- **Problema trattabile**: ∃ algoritmo efficiente

---

title: Complessità esponenziale
figure: images/comp/orders.svg

- Complessità esponenziale: `k^^n^^`
    - Es. elenco sottinsiemi, strategia perfetta per scacchi
- Complessità super-esponenziale: `n!`, `n^^n^^`, …
    - Es. elenco permutazioni
- **Problemi intrattabili**
    - ∄ algoritmo efficiente
    - Soluzioni non esatte/ottime, euristiche
    - Ma minimi locali...

---

title: Problemi P ed NP

- Problemi **P**: ∃ algoritmo *deterministico polinomiale*
- **NP**: ∃ algoritmo *non-deterministico polinomiale*
    - Su macchine deterministiche: non noto algoritmo polinomiale per la **ricerca** di una soluzione...
    - Ma algoritmo polinomiale per la **verifica** di una soluzione
- Esempio: fattorizzazione di grandi numeri
    - Ricerca: quali sono i fattori primi di un numero di `n` cifre?
    - Verifica: è vero che `x` è divisore di `y`?
- **Non è dimostrato che P≠NP, né che P=NP**
    - Millenium Prize Problems: 1M$
    - Se *P=NP*, trovare i fattori primi di un numero o verificarli: stessa classe di complessità

---

title: Complessità dei linguaggi

- *Linguaggi di classe P / NP*: stringa `x` riconosciuta in tempo polinomiale rispetto a `|x|`...
    - *P*: da una macchina di Turing deterministica (*DTM*)
    - *NP*: da una macchina di Turing non-deterministica (*NTM*)
    - Sappiamo che *P ⊆ NP* (DTM: caso particolare di NTM)
- *Linguaggi di classe EXP*: stringa `x` riconosciuta in tempo esponenziale rispetto a `|x|` da una DTM
    - NTM: simulata da DTM in tempo esponenziale
    - Quindi *NP ⊆ EXP*
- **P ⊆ NP ⊆ EXP**

---

title: Problemi NP-completi
figure: images/comp/classes.svg images/comp/knapsack.svg

- Ogni problema NP può essere ricondotto ad un problema **NP-completo** con algoritmo deterministico *polinomiale*
    - *Lower-bound* deterministico esponenziale per uno dei problemi NP-completi? ⇒ *P≠NP*
    - Oppure, *soluzione* con algoritmo deterministico polinomiale? ⇒ *P=NP*
- Esempio: *SAT*
    - Data una formula booleana *PdS*, è soddisfacibile?
    - ∃ combinazione di input che dà risultato vero?
- Esempio: *Knapsack*
    - ∃ combinazione di elementi che realizza utilità `≥V`, con peso `≤W`?

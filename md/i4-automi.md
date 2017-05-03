title: Automi e calcolo
subtitle: Introduzione all'informatica
figure: images/comp/hugo.jpg

---

title: Automi e calcolo
figure: images/comp/executor.svg
class: large-figure

- **Automa**: *macchina astratta*
- Riceve dall'esterno i dati ed una descrizione dell'algoritmo richiesto
- Interpreta un linguaggio, detto linguaggio macchina dell'automa
- Vincolo su numero di componenti, finito
- Vincolo su alfabeti di ingresso e di uscita, composti da un numero finito di simboli

---

title: Riconoscimento di linguaggi

- Data una stringa `x`, stabilire se essa appartiene ad `L` (problema dell'*appartenenza*, o *membership*)
- L. tipo 3: riconosciuti da *macchine a stati finiti (FSM)*
    - Es.: `{a^^n^^b : n≥0}`, gen. da `S → aS | b`
- L. tipo 2: *automi a pila non deterministici (NPDA)*
    - Es.: `{a^^n^^b^^n^^ : n≥1}` gen. da `S → aSb | ab`
- L. tipo 1: *automi limitati linearmente (LBA)*
    - Es.: `{a^^n^^b^^n^^c^^n^^ : n≥1}`
- L. tipo 0:  riconosciuti da *macchine di Turing (TM)*
    - Però semi-decidibili: se `x ∉ L`, il processo può non terminare!

---

title: Macchina a stati finiti (FSM)
class: segue dark

---

title: Macchina a stati finiti (FSM)

- `M = <Σ, Q, δ, q~~0~~, F>`
- `Σ = {σ~~1~~,...,σ~~n~~}`: alfabeto di input
- `Q = {q~~0~~,...,q~~n~~}`: insieme finito non vuoto di stati
- `F ⊆ Q`: insieme di stati finali
- `q~~0~~ ∈ Q`: stato iniziale
- `δ: Q x Σ → Q`: funzione di transizione
    - In base allo stato e al simbolo di input attuali … <br> determina lo stato successivo

---

title: Linguaggio riconosciuto da FSM

- Funzione di transiz. estesa a stringhe: `δ: Q x Σ* → Q`
    - `δ(q, ε) = q`
    - `δ(q, ax) = δ(δ(q, a), x)`,  con `a ∈ Σ, x ∈ Σ*`
- Linguaggio riconosciuto da una macchina `M`:
    - `L(M) = {x ∈ Σ* : δ(q0, x) ∈ F}`
- FSM riconoscono tutti e soli i *linguaggi regolari*
- Rappresentazione della funzione di transizione
    - *Tabella di transizione*
    - *Diagramma degli stati*

---

title: Esempio di FSM
figure: images/comp/fsm4.svg
figcaption: Stringhe con a in numero pari e b in numero pari

- `M = <{a, b}, {q~~S~~, q~~A~~, q~~B~~, q~~C~~}, δ, q~~S~~, {q~~S~~}>`

δ      | a      | b
-------|--------|---
q~~S~~ | q~~A~~ | q~~B~~
q~~A~~ | q~~S~~ | q~~C~~
q~~B~~ | q~~C~~ | q~~S~~
q~~C~~ | q~~B~~ | q~~A~~

- Grammatica equivalente (con *ε-prod* per `q~~S~~`):
    - `S → aA | bB | ε` <br> `A → aS | bC` <br> `B → aC | bS` <br> `C → aB | bA`

---

title: FSM non deterministica

- `M = <Σ, Q, δ~~N~~, q~~0~~, F>`
- `Σ = {σ~~1~~, ..., σ~~n~~}`: alfabeto di input
- `Q = {q~~0~~, ..., q~~m~~}`: insieme finito non vuoto di stati
- `F ⊆ Q`: insieme di stati finali
- `q~~0~~ ∈ Q`: stato iniziale
- `δ~~N~~: Q x Σ → P(Q)`: funzione di transizione, determina insieme di stati successivi
    - `P(Q)` è l'insieme delle parti di `Q`, ossia l'insieme di tutti i possibili sottoinsiemi di `Q`

---

title: Esempio di NFSM
figure: images/comp/nfsm.svg
figcaption: Accetta qualsiasi stringa terminante con b

- `M = <{a, b}, {q~~0~~, q~~1~~}, δ, q~~0~~, {q~~1~~}>`

δ      | a        | b
-------|----------|----
q~~0~~ | {q~~0~~} | {q~~0~~, q~~1~~}
q~~1~~ | {}       | {}

- `{q~~0~~} ↔ q'~~0~~`, `{q~~0~~, q~~1~~} ↔ q'~~1~~`


δ'               | a        | b
-----------------|----------|----
{q~~0~~}         | {q~~0~~} | {q~~0~~, q~~1~~}
{q~~0~~, q~~1~~} | {q~~0~~} | {q~~0~~, q~~1~~}

- `M' = <{a, b}, {q'~~0~~, q'~~1~~}, δ', q'~~0~~, {q'~~1~~}>`

---

title: Equivalenza FSM / NFSM

- Per ogni stato / ingresso, definiti più stati successivi
- Non-determinismo: calcolo = albero di computazioni autonome, anziché traiettoria in uno spazio di stati
- Nel casi di FSM, non-determinismo non aggiunge potere computazionale
    - FSM / NFSM: formalismi equivalenti
    - FSM è un caso particolare di NFSM
    - Viceversa, ogni elemento di `P(Q)` di NFSM diventa uno stato di FSM
    - `P(Q)` contiene `2^^|Q|^^` elementi

---

title: Automa a pila (PDA)
class: segue dark

---

title: Automa a pila (PDA)
figure: images/comp/pda.svg

- Simile a FSM, ma dotato di memoria infinita, organizzata a pila
    - Si può accedere solo alla cima della pila
    - Lettura del simbolo in cima
    - Sostituzione simbolo in cima con nuova stringa (anche ε)
- In forma non-deterministica, permette di riconoscere i linguaggi non contestuali
- In forma deterministica, riconosce solo i linguaggi non contestuali deterministici (sottoclasse)
    - Base dei comuni linguaggi di programmazione

---

title: Definizione di PDA

- `M = <Σ, Γ, z~~0~~, Q, q~~0~~, F, δ>`
- `Σ = {σ~~1~~, ..., σ~~n~~}`: alfabeto di input
- `Γ = {z~~0~~, ..., z~~m~~}`: simboli della pila
- `z~~0~~ ∈ Γ`: simbolo di pila iniziale
- `Q = {q~~0~~, ..., q~~k~~}`: insieme finito non vuoto di stati
- `q~~0~~ ∈ Q`: stato iniziale; `F ⊆ Q`: insieme di stati finali
- `δ: Q x Σ x Γ → Q x Γ*`: funzione di transizione
    - In base a stato, simbolo di input, simbolo in cima a pila …
    - Determina stato successivo e simboli inseriti nella pila
    - Per rimuovere il simbolo in cima alla pila, si scrive ε

---

title: Esempio di PDA

- Automa a pila M che riconosce `L = {a^^n^^b^^n^^, n ≥ 1}`
- `M = <{a, b}, {Z~~0~~, A~~0~~, A}, Z~~0~~, {q~~0~~, q~~1~~, q~~2~~}, q~~0~~, {q~~2~~}, δ>`
    - `A`: si impilano sopra `A~~0~~` per contare le `a`
    - `q~~0~~`: si memorizzano le `a`
    - `q~~1~~`: si confrontano le `b` con quanto memorizzato
    - `q~~2~~`:  stato finale

δ      | Z~~0~~, a      | Z~~0~~, b | A~~0~~, a       | A~~0~~, b | A, a       | A, b
-------|----------------|-----------|-----------------|-----------|------------|----------
q~~0~~ | A~~0~~, q~~0~~ |           | AA~~0~~, q~~0~~ | ε, q~~2~~ | AA, q~~0~~ | ε, q~~1~~
q~~1~~ |                |           |                 | ε, q~~2~~ |            | ε, q~~1~~
q~~2~~ |                |           |                 |           |            |


---

title: PDA non deterministico (NPDA)

- `A = <Σ, Γ, z~~0~~, Q, q~~0~~, F, δ~~N~~>`
- `δ~~N~~: Q x Σ~~ε~~ x Γ → P(Q x Γ*)`: funzione di transizione, determina gli stati e i simboli di pila successivi
    - Es. `δ(p, a, A) = {(q, BA), (r, ε)}`   (due transizioni)
    - Simbolo `A` in cima alla pila sostituito dalla stringa di caratteri `BA`, nuovo stato interno `q`
    - Simbolo `A` in cima alla rimosso (sostituito da `ε`), nuovo stato interno `r`
- NPDA: maggiore potere computazionale di PDA
    - `L = {a^^n^^b^^n^^} ∪ {a^^n^^b^^2n^^},  n ≥ 0`
    - `S → A|B, A → aAb|ε, B → aBbb|ε`

---

title: Macchina di Turing (TM)
class: segue dark

---

title: Macchina di Turing (TM)
figure: images/comp/tm.png

- Automa con testina di scrittura/lettura su nastro bidirezionale “illimitato”
- Ad ogni passo:
    - Si trova in un certo stato
    - Legge un simbolo dal nastro
- In base alla funzione di transizione (deterministica):
    - Scrive un simbolo sul nastro
    - Sposta la testina di una posizione
    - Cambia lo stato
- Può simulare ogni altro modello di calcolo noto!

---

title: TM deterministica

- `M = <Σ, Q, q~~0~~, F, δ>`
- `Σ = {σ~~1~~, ..., σ~~n~~, ␢}`: alfabeto di input (+ *blank*)
- `Q = {q~~0~~, ..., q~~m~~}`: insieme finito non vuoto di stati
- `q0 ∈ Q`: stato iniziale
- `F ⊆ Q`: insieme di stati finali
- `δ: Q x Σ → Q x Σ x {d, s, i}`: funzione di transizione
    - Determina lo stato successivo, il simbolo successivo, lo spostamento della testina

---

title: TM non deterministica (NTM)

- `M = <Σ, Q, q~~0~~, F, δ~~N~~>`
- `δ~~N~~: Q x Σ → P(Q x Σ x {d, s, i})`: funzione di transizione
    - Determina le configurazioni successive (nuovo stato, simbolo scritto, spostamento della testina)
- Grado di non-determinismo: massimo numero di figli di un nodo dell'albero di computazione
- NTM: **stessa potenza computazionale di TM**
    - Data NTM, `M`, con grado di non-determinismo `n`...
    - `∃ M'`, una equivalente MT, in grado di simulare `M`
- Ma (finora…) NTM **più efficiente**
    - `k` passi di `M` richiedono `k'` (`∝ kn^^k^^` , asintot.) passi di `M'`

---

title: Macchina di Turing universale (UTM)

- UTM realizza la computazione:
    - `(q~~0U~~, D~~M~~#x) →* (α, q~~fU~~, β)` …
    - `q~~0U~~`, stato iniziale; `q~~fU~~`, stato finale
    - `D~~M~~#x`: input; `D~~M~~`: descrizione di `M` (funz. di transizione)
- ⇔ `M` realizza la computazione: `(q~~0~~, x) →* (α, q~~f~~, β)`
    - `q~~0~~`, stato iniziale; `q~~f~~`, stato finale; `x`, input
- Regole di transizione di `M` → Sequenza di quintuple
    - `D~~M~~ = d~~1~~##d~~2~~## ... ##d~~n~~` 
    - `q~~i~~#σ~~j~~#q~~h~~#σ~~k~~#t~~l~~ ⇔ δ(q~~i~~, σ~~j~~) = (q~~h~~, σ~~k~~, t~~l~~)`

---

title: Funzionamento della UTM

- UTM **interpreta** un arbitrario programma su nastro
    - Dato lo stesso input, UTM produce lo stesso output di `M`
    - Per ogni simbolo letto in `x` (input di `M`), scorre la lista di regole, per scegliere la giusta transizione

![](images/comp/utm.svg)

---

title: Calcolabilità
class: segue dark

---

title: Calcolabilità

- **Tesi di Church-Turing**: problema intuitivamente calcolabile → esiste TM in grado di calcolarlo
    - TM: formalismo non meno potente di ogni altro modello di calcolo proposto finora
    - Funzioni ricorsive, lambda-calcolo, macchine a registri…
- Ma esistono **problemi irrisolvibili** (nel caso generale)
    - Attenzione: non si dice niente sulla singola istanza!
- *Teorema di incompletezza di Gödel*
    - ∀ formalizzazione della matematica che assiomatizza ℕ
    - → ∃ proposizione né dimostrabile né confutabile

---

title: Paradossi classici

- Paradosso del mentitore
    - Questa frase è falsa
    - Epimenide di Creta afferma: *“I cretesi sono bugiardi”*
- Paradosso del barbiere
    - Se un barbiere fa la barba a tutti e soli coloro che non si fanno la barba da soli, chi sbarba il barbiere?
- Paradosso di Russell
    - Consideriamo insiemi di insiemi e supponiamo che un insieme possa contenere se stesso
    - Sia T l'insieme di tutti gli insiemi che non contengono se stessi; possiamo stabilire se T contiene T?

---

title: Problema della terminazione

- Predicato della terminazione, **non calcolabile**
    - `h(D~~M~~, x) = 1`, se `M` con input `x` termina
    - `h(D~~M~~, x) = 0`, se `M` con input `x` non termina
- Costruiamo per assurdo `H`, TM che calcola `h`
- Costruiamo quindi `G`
    - `g(D~~M~~) = 0`, se `h(D~~M~~, D~~M~~) = 0`
    - Indefinito, altrimenti (ossia `G` cicla all'infinito, se `h = 1`)
- Ma è assurdo:
    - `g(D~~G~~)` è indefinita, se `g(D~~G~~) = 0` (definita)
    - `g(D~~G~~) = 0` (definita) se `g(D~~G~~)` è indefinita

>

`M`: macchina di Turing; `D~~M~~`: rappresentazione di `M` come stringa

---

title: Più informalmente...

- Funz. `g` definita in `paradox.py` (Python è *Turing completo*)

code: Python

    from absurd import h
    def g(file):
        if h(file, file):
            while True: pass
        else:
            return False
    g('paradox.py')

- Altri problemi indecidibili (corollari)
    - Correttezza: il programma calcola la funzione desiderata?
    - Chiamata: una procedura (o istruzione) sarà eseguita?
    - Equivalenza, ambiguità di grammatiche CF …
    
---

title: Macchine a registri
class: segue dark

---

title: Calcolatore
figure: images/sys/hal-9000.jpg

- Macchina programmabile
    - Memorizza ed elabora automaticamente...
    - Attraverso istruzioni di un programma...
    - Informazioni in formato digitale (I/O)
- Diversi modello di calcolo
    - Definizione di operazioni elementari e concetto stesso di algoritmo
    - Definizione di problema risolvibile / irrisolvibile (calcolabilità): dipende dal modello di calcolo
- Macchina di Turing
    - Modello teorico (A. Turing, 1936)
    - Tesi di Church-Turing: problema intuitivamente calcolabile → esiste TM in grado di calcolarlo

---

title: Macchina di von Neumann
figure: images/sys/bus.svg images/hist/eniac.jpg

- 1941, Z3 (Berlino)
    - A relais, programma su nastro esterno
- 1946, ENIAC (Philadelphia)
    - Balistica, meteorologia, reazioni nucleari
    - Programmazione con cavi
- 1948, Manchester "baby"
    - Programma in memoria
- 1951, sistema IAS (Princeton)
    - Dati e programmi in memoria centrale

---

title: Northbridge e southbridge
class: large-image

![](images/sys/north-south-bridge.png)

---

title: Central Processing Unit

- CPU: “cervello” del calcolatore
    - Esegue i programmi
    - Comanda le altre parti del calcolatore
- Composta da due parti:
    - **Control Unit (CU)**: interpreta le istruzioni, comanda le altre parti della CPU, controlla il flusso tra CPU e memoria
    - **Arithmetic Logical Unit (ALU)**: esegue le operazioni aritmetiche e logiche, esegue i confronti tra dati

---

title: Architettura CPU
class: large-image

![](images/sys/cpu-architecture.png)

---

title: Ciclo principale della CPU

- **Caricamento**: CU preleva l’istruzione dalla locazione di memoria indicata dal registro PC (Program Counter) e la memorizza in IR (Instruction Register)
- **Decodifica**: CU interpreta l’istruzione, legge eventualmente dalla memoria i dati necessari
- **Esecuzione**: CU comanda le parti
- **Memorizzazione**: risultati memorizzati nella memoria centrale o in registri della CPU

---

title: Lettura dalla memoria
class: large-image

![](images/sys/cpu-memory.svg)

---

title: Sequenza di lettura
class: large-image

![](images/sys/cpu-read-1.svg)

---

title: Sequenza di lettura
class: large-image

![](images/sys/cpu-read-2.svg)

---

title: Sequenza di scrittura
class: large-image

![](images/sys/cpu-write-1.svg)

---

title: Sequenza di scrittura
class: large-image

![](images/sys/cpu-write-2.svg)

---

title: Fetch istruzioni
class: large-image

![](images/sys/cpu-fetch.svg)

---

title: Interpretazione istruzioni

- Al termine della fase di *fetch*, IR contiene l'istruzione da eseguire
    - **Codice operativo + operandi**
    - *Linguaggio macchina*: il significato dipende dalla CPU
- Nell'esempio: **`4`** `010 ~~(16)~~ = ` **` 0100 `** `0000 0001 0000 ~~(2)~~`
    - Codice operativo = **`0100`**
    - Es. Leggi una parola dal registro delle periferiche...
    - E memorizzala in un indirizzo di memoria (operando)
    
---

title: Esecuzione istruzioni
class: large-image

![](images/sys/cpu-exec.svg)

---

title: Classificazione di Flynn
figure: images/sys/flynn.svg
class: large-figure

- **Parallelismo**: migliori prestazioni, a parità di velocità sulla singola istruzione
- *SISD*: una operazione alla volta; macchine tradizionali a singolo processore e core
- *MISD*: insolite, per tolleranza ai guasti; sistemi eterogenei, sugli stessi dati, devono dare gli stessi risultati
- *SIMD*: operazioni naturalmente parallelizzabili; unità di calcolo vettoriale e GPU
- *MIMD*: istruzioni diverse su dati diversi; architetture con più core o processori autonomi, sistemi distribuiti

---

title: Assembler

- **Linguaggio macchina**: definisce il set di istruzioni comprensibile dalla CPU
    - *CISC*: Complex Instruction Set Computing
    - *RISC*: Reduced instruction set Computing
- Assembler: traduce da **linguaggio assembly** (mnemonico) a linguaggio macchina (mapping 1~1)
- Es. *Assembly x86* → macchina (istruzioni di varia lunghezza)

code: Assembly

    MOV AH, 11 → 1011 0 100 00001011

- 4 bit di op-code (`1011`), tipo di istruzione
- Bit `w` (`0`): operazione a 8 o 16 bit, (0 o 1 risp.)
- 3 bit per registro destinazione (`100`)
- 8 bit di dato per operando: `11~~(10)~~ = 00001011~~(2)~~`


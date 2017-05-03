title: Linguaggi formali
subtitle: Introduzione all'informatica
figure: images/comp/attack.jpg

---

title: Linguaggi formali

- Presenti in tutte le applicazioni
    - Linguaggi di programmazione
    - Linguaggi di marcatura (es. HTML, Latex)
    - Interazione uomo macchina (es. Google, Zork)
- Fondamentali nel software di sistema
    - Compilatori
    - Interpreti …
- Paradigmatici nella teoria
    - Molti problemi riconducibili a quello dell'*appartenenza*: una stringa appartiene ad un linguaggio?

---

title: Alfabeti e stringhe

- Alfabeto `Σ`: insieme di simboli
- Stringa `s`: sequenza di simboli di `Σ`
    - `s ∈ Σ*`, insieme di tutte le stringhe
    - `ε`: stringa vuota
    - `|s|`: lunghezza della stringa `s`
- Linguaggio `L ⊆ Σ*`
    - Sottoinsieme di tutte le stringhe possibili
    - Grammatica: regole formali per definire le “*stringhe ben formate*” di L
- Esempio: numeri romani da 1 a 1000
    - Alfabeto `{I, V, X, L, C, D, M}` + regole...

---

title: Concatenazione di stringhe

- Operazione di concatenazione `•`
    - Propr. associativa: `(x • y) • z = x • (y • z)`
    - Non commutativa: `x • y ≠ y • x`
    - `Σ*` chiuso rispetto a `•: Σ* x Σ* → Σ*`
- Potenza
    - `x^^n^^ = x • x • x • x … (n volte)`
- Elemento neutro `ε`
    - Stringa vuota, `∀ x ∈ Σ*, ε • x = x • ε = x`
    
>

`<Σ*, •, ε>`: monoide

---

title: Definizione di linguaggi

- Approccio **algebrico**: linguaggio costruito a partire da linguaggi più elementari, con operazioni su linguaggi
- Approccio **generativo**: grammatica, regole per la generazione di stringhe appartenenti al linguaggio
- Approccio **riconoscitivo**: macchina astratta o algoritmo di riconoscimento, per decidere se una stringa appartiene o no al linguaggio

---

title: Espressioni regolari
class: segue dark

---

title: Operazioni su linguaggi

- `L~~1~~` ed `L~~2~~` linguaggi su `Σ*` (due insiemi di stringhe)
- Unione: `L~~1~~ ∪ L~~2~~ = {x ∈ Σ* : x ∈ L~~1~~ ∨ x ∈ L~~2~~}`
- Intersezione: `L~~1~~ ∩ L~~2~~ = {x ∈ Σ* : x ∈ L~~1~~ ∧ x ∈ L~~2~~}`
- Complementazione: `̅L~~1~~ = {x ∈ Σ* : x ∉ L~~1~~}`
- Concatenazione o prodotto: `L~~1~~ • L~~2~~ = {x ∈ Σ* : x = x~~1~~ • x~~2~~, x~~1~~ ∈ L~~1~~, x~~2~~ ∈ L~~2~~}`
- Potenza: `L^^n^^ = L • L^^n-1^^, n≥1; L^^0^^ = {ε}` per convenzione
    - Concatenazione di‌ `n` stringhe qualsiasi di `L`
- Stella di Kleene: `L* = ∪ L^^n^^, n = 0..∞`
    - Concatenazione arbitraria di‌ stringhe di `L`

>

`L*`: chiusura riflessiva e transitiva di `L` rispetto a `•`

---

title: Espressioni regolari

- Dato un alfabeto `Σ`, chiamiamo *espressione regolare* una stringa `r` sull'alfabeto `Σ ∪ {+, *, (, ), •, Ø}` t.c.:
    - `r = Ø`: linguaggio vuoto; oppure
    - `r ∈ Σ`: linguaggio con un solo simbolo; oppure
    - `r = s + t`: unione dei linguaggi `L(s)`, `L(t)`; oppure
    - `r = s • t`: concatenazione dei linguaggi `L(s)`, `L(t)`; oppure
    - `r = s*`: chiusura del linguaggio `L(s)`
    - (con `s` e `t` espressioni regolari; simbolo `•` spesso implicito)
- *Linguaggi regolari*: rappresentabili con espressioni regolari (*“regex”*)

>

Esempio, con `Σ = {a, b}`: <br> `a • (a + b)* • b`

---

title: Regex nelle applicazioni

- Concatenazione di caratteri: `goal`
- Unione tra espressioni (opzione): `one|two|three`
- Un car. da un insieme (o no): `[a-z]`, `[^a-z0-9]`
- Un carattere qualsiasi: `defin.tely`
- Ripetizioni (0+, 1+, 0-1): `goo*al`, `go+al`, `goo?al`
- Sottoespressione: `(left right )*halt`

code: python

    >>> text = 'Though not quickly, he run the 5th lap steadily.'
    >>> re.findall(r'[a-z]+ly', text)
    ['quickly', 'steadily']
    >>> re.sub(r'([0-9])([a-z]+)', r'\1<sup>\2</sup>', text)
    Though not quickly, he run the 5<sup>th</sup> lap steadily.

<http://docs.python.org/3/library/re.html> - <http://www.zytrax.com/tech/web/regex.htm>

---

title: Grammatiche di Chomsky
class: segue dark

---

title: Grammatiche di Chomsky

- Grammatica `G = < V~~T~~, V~~N~~, P, S >`
    - `V~~T~~`: alfabeto finito di simboli **terminali**
    - `V~~N~~`: ... **non terminali** (variabili, categorie sintattiche)
    - `V = V~~T~~ ∪ V~~N~~`
    - `P`: insieme di **produzioni**, relaz. binarie `V* • V~~N~~ • V* x V*` <br> `<α, β> ∈ P` si indica con `α → β`
    - `S ∈ V~~N~~`: **assioma**
- `L(G)`: insieme delle stringhe di terminali ottenibili con finite operazioni di riscrittura
    - Applicazione delle regole di produzione, in vario modo

---

title: Linguaggio generato da G

- *Derivazione diretta* `⇒`: riscrittura di una stringa tramite applicazione di una regola di produzione
- *Derivazione* `⇒*`: chiusura riflessiva e transitiva della derivazione diretta
- *Forma di frase*: stringa `x t.c. x ∈ V*, S ⇒* x`
- *Linguaggio generato* da `G`: forme di frase con soli simboli terminali
    - `L(G) = {x : x ∈ V~~T~~*, S ⇒* x}`
- *Equivalenza* tra `G~~1~~` e `G~~2~~`: `L(G~~1~~) = L(G~~2~~)`

---

title: Grammatiche equivalenti

- `G~~1~~ = <{a,b}, {S, A}, P, S>`, con produzioni:
    - `S → b` <br> `S → aA` <br> `A → aS`
    - … genera il linguaggio `{a^^n^^b : n pari}`
- Anche `G~~2~~`, con produzioni:
    - `S → Ab | b` <br> `A → aAa | aa`
- Ed anche `G3`:
    - `S → Ab` <br> `A → Aaa | ε`

>

`|` per raggruppare diverse produzioni di uno stesso non-terminale

---

title: Esempio di generazione

- `G = <{a, b, c}, {S, B, C}, P, S>`
    - (1) `S → aSBC`
    - (2) `S → aBC`
    - (3) `CB → BC`
    - (4) `aB → ab`
    - (5) `bB → bb`
    - (6) `bC → bc`
    - (7) `cC → cc`
    - … genera il linguaggio `{a^^n^^b^^n^^c^^n^^ : n≥1}`
- Esercizio: provare a generare `aaabbbccc`
    - Soluzione: applicare 1-1-2-3-3-3-4-5-5-6-7-7

---

title: Alberi di derivazione (sintattici)

- Esempio di grammatica **ambigua**: due interpretazioni valide per `a + a * a`
    - `V~~T~~ = {a, +, *, (, )};  V~~N~~ = {E};`
    - `E → E+E | E*E | (E) | a`

![](images/comp/ambiguity.svg)

- Grammatica non ambigua (con precedenza tra operatori)
    - `E → E+T | T` <br> `T → T∗F | F` <br> `F → (E) | a`

---

title: Classificazione di Chomsky
figure: images/comp/hierarchy.svg

- *Tipo 0*: grammatiche **ricorsivam. enumerabili** (RE)
    - `αAβ → γ` (*non limitate*)
- *Tipo 1*: grammatiche **contestuali** (CS)
    - `αAβ → αγβ`
- *Tipo 2*: grammatiche **non contestuali** (CF)
    - `A → γ`
- *Tipo 3*: grammatiche **regolari** (REG)
    - `A → aB` oppure `A → b`
    - Coincide con classe dei linguaggi definiti da *regex*

>

`A, B ∈ V~~N~~; a, b ∈ V~~T~~; α, β, γ ∈ V*`

---

title: Linguaggi non contestuali
class: segue dark

---

title: Linguaggi non contestuali

- Controllo di *palindromi*, *bilanciamento di parentesi* e varie *simmetrie*
    - Es.: `{a^^n^^b^^n^^ : n≥1}` gen. da `S → aSb | ab` (CF)
    - Ma non: `{a^^n^^b^^n^^c^^n^^ : n≥1}` (CS) (*)
- **Linguaggi di programmazione** comuni: grammatiche CF
- Definizione con notazione Extended **Backus-Naur Form** (EBNF)
    - `{...}`: parte ripetibile (0+), `[...]`: parte opzionale, 
    - `(...)`: raggruppamento, `|`: scelta
    - Terminali tra virgolette

>

(*) Nell'es. visto, sostituire (3) con: (3a) `CB → HB`; (3b) `HB → HC`; (3c) `HC → BC`


---

title: Linguaggi LL(1)

- Sottoclasse dei linguaggi CF
- Ogni produzione relativa a stesso non-terminale (a sx)... <br> genera come primo simbolo un terminale diverso
    - No prefissi comuni, no ricorsione sinistra
- **Recursive descent parser**: analisi sintattica molto semplice ed efficiente
    - Basta “spiare” il simbolo di input successivo, per capire con certezza quale produzione applicare
- *Polish prefix notation*
    - Es.: `* + 1 2 - 3 2` ⇒ (in forma infissa) `(1 + 2) * (3 - 2)`

code: ebnf

    expr = number | "+" expr expr | "-" expr expr | "*" expr expr | "/" expr expr
    number = digit {digit}
    digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

---

title: Espressioni infisse

- Grammatica equiv. LL(1), ma senza precedenza tra operatori
- Provare a generare `2 + 3 * 3`

code: ebnf

    expr = term {( "+" | "-" | "*" | "/" ) term}
    term = number | "(" expr ")" | "-" term

- Grammatica equiv. LL(1), con precedenza tra operatori

code: ebnf

    expr = term {( "+" | "-" ) term}
    term = factor {( "*" | "/" ) factor}
    factor = number | "(" expr ")" | "-" term

---

title: Pumping lemma REG
figure: images/comp/pumping-lemma-3.svg

- Formalmente, `∀ L` regolare...
    * `∃ k t.c. ∀ z ∈ L, |z| ≥ k`
    * `∃ u, v, w, |uv| ≤ k, |v| ≥ 1 t.c.`
    * `z = uvw, uv^^i^^w ∈ L, ∀ i ≥ 0`
- In ogni stringa abbastanza lunga,
    * c'è una parte che si può ripetere,
    * generando un'altra stringa di `L`
- Uno stesso non-terminale, per un input abbastanza lungo, deve comparire più volte nell'albero sintattico …
    * Un Automa a Stati Finiti (*), per un input abbastanza lungo, torna in uno stato già visitato …

>

Esempio con `G~~1~~`: <br> `S → b | aA; A → aS`

---

title: Pumping lemma CF
figure: images/comp/pumping-lemma-2.svg

- Formalmente, `∀ L` non contestuale...
    * `∃ k t.c. ∀ z ∈ L, |z| ≥ k`
    * `∃ u, v, w, x, y, |vwx| ≤ k, |vx| ≥ 1 t.c.`
    * `z = uvwxy, uv^^i^^wx^^i^^y ∈ L, ∀ i ≥ 0`
- In ogni stringa abbastanza lunga,
    * ci sono due parti che si possono
    * ripetere assieme, restando in `L`
- Uno stesso non-terminale, per un input abbastanza lungo, deve comparire più volte nell'albero sintattico …

---

title: Corollari dei due pumping lemma

- ⇒ `L = {a^^n^^b^^n^^ : n ≥ 0}` non è REG
    * Si prende `a^^m^^b^^m^^, con m > k ⇒ |uv| < m`, sono tutte `a`…
- ⇒ `L = {a^^n^^b^^n^^c^^n^^ : n ≥ 0}` non è CF
    * Si prende `a^^m^^b^^m^^c^^m^^, con m > k ⇒ |vwx| < m`
    * Se `v` ed `x` con più simboli diversi, `uv^^2^^wx^^2^^y` con simboli mescolati
    * Se `v` ed `x` con un solo simbolo, `uv^^2^^wx^^2^^y` con numero diverso di `a`, `b`, `c`
    * In entrambi i casi la nuova stringa `z' ∉ L`

---

title: Linguaggi di programmazione
class: segue dark

---

title: Linguaggi di programmazione

- Notazione formale per definire algoritmi
    - *Algoritmo*: sequenza di istruzioni per risolvere un dato problema in un tempo finito
- Ogni linguaggio è caratterizzato da:
    - **Sintassi**
    - **Semantica**

---

title: Sintassi
figure: images/dev/syntax-diagrams.png
class: large-figure

- Insieme di regole formali per scrivere *frasi* ben formate (programmi) in un certo linguaggio
    - *Lessico*: parole riservate, operatori, variabili, costanti ecc. (*token*)
- Grammatiche non contestuali (...) espresse con notazioni formali:
    - Backus-Naur Form
    - Extended BNF
    - Diagrammi sintattici

---

title: Semantica

- Attribuisce un **significato** alle frasi (sintatticamente corrette) costruite nel linguaggio
- Una frase può essere sintatticamente corretta e tuttavia non aver alcun significato
    - Soggetto – predicato – complemento
    - *“La mela mangia il bambino”*
    - *“Il bambino mangia la mela”*
- Oppure avere un significato diverso da quello previsto...
    - *GREEK_PI = 345*

---

title: Semantica

- **Correttezza sui tipi**
    - Quali tipi di dato possono essere elaborati?
    - Quali operatori applicabili ad ogni dato?
    - Quali regole per definire nuovi tipi e operatori?
- **Semantica operazionale**
    - Qual è l'effetto di ogni azione elementare?
    - Qual è l’effetto dell’aggregazione delle azioni?
    - Cioè, qual è l’effetto dell’esecuzione di un certo programma?

---

title: Linguaggi di basso livello
figure: images/dev/assembly.png
class: large-figure

- Più orientati alla macchina che ai problemi da trattare
- **Linguaggi macchina**: solo operazioni eseguibili direttamente dall'elaboratore
    - Op. molto elementari, diverse per ogni processore, in formato binario
- **Linguaggi assembly**: prima evoluzione, codici binari → mnemonici

---

title: Linguaggi di alto livello

- Introdotti per facilitare la scrittura dei programmi
- Definizione della soluzione in modo intuitivo
- Con una certa **astrazione** rispetto al calcolatore su cui verranno eseguiti
- Devono essere tradotti in linguaggio macchina

---

title: Storia dei linguaggi
class: large-image

![](images/dev/languages-timeline.svg)

>

<http://www.oreilly.com/news/graphics/prog_lang_poster.pdf> <br>
<http://www.levenez.com/lang/history.html> <br>
<http://www.cs.brown.edu/~adf/programming_languages.html>

---

title: The Top 20 (IEEE Spectrum, 2015)

![](images/dev/languages-spectrum-2015.png)

>

<http://spectrum.ieee.org/static/interactive-the-top-programming-languages-2015>

---

title: Paradigmi di sviluppo

- Forniscono la filosofia e la metodologia con cui si scrivono i programmi
- Definiscono il concetto (astratto) di computazione
- Ogni linguaggio consente (o spinge verso) l'adozione di un particolare paradigma
    - Imperativo / procedurale
    - Orientato agli oggetti
    - Scripting (tipizzazione dinamica, principio DRY - Don't Repeat Yourself)
    - Funzionale (funzioni come “cittadini di prima classe”)
    - Logico (base di conoscenza + regole di inferenza)

---

title: Linguaggi e paradigmi

- **Imperativi / procedurali**
    - Cobol, Fortran, Algol, C, Pascal 
- **Orientati agli oggetti**
    - Simula, Smalltalk, Eiffel, C++, Delphi, Java, C#, VB.NET
- **Scripting**
    - Basic, Perl, PHP, Javascript, Python, Shell
- **Funzionali**
    - Lisp, Scheme, ML, Haskell, Erlang
- **Logici**
    - Prolog...

---

title: Esecuzione dei programmi

- Linguaggio ad alto livello → passi necessari:
    - **Compilazione**, traduzione in linguaggio macchina
    - **Collegamento** con librerie di supporto
    - **Caricamento** in memoria
- Programmi **compilati**: applicati i 3 passi...
    - A tutto il codice; prima dell'esecuzione
- Programmi **interpretati**: applicati i 3 passi...
    - In sequenza, su ogni istruzione; a tempo di esecuzione

![](images/dev/build.svg)

---

title: Compilazione
figure: images/dev/compiler.svg
class: large-figure

- Traduzione da ling. alto livello a ling. macchina
    - Analisi: lessicale, grammaticale, contestuale
    - *Rappresentazione intermedia*: albero sintattico annotato (**AST**) 
    - Generazione codice oggetto
- Codice oggetto: non ancora eseguibile
    - Linker, loader

---

title: Albero sintattico
figure: images/dev/ast-euclid.svg
class: large-figure

code: Python

    while b != 0:
        if a > b:
            a = a − b
        else:
            b = b − a
    return a 

Algoritmo di Euclide per MCD

---

title: Collegamento

- Il **linker** collega diversi moduli oggetto
    - Simboli irrisolti → riferimenti esterni
    - Il collegamento può essere statico o dinamico
- **Collegamento statico**
    - Libreria inclusa nel file oggetto, eseguibile stand-alone
    - Dimensioni maggiori, ma possibile includere solo funzionalità utilizzate
- **Collegamento dinamico**
    - Librerie condivise da diverse applicazioni
    - Installazione ed aggiornamento unici
    - Caricate in memoria una sola volta

---

title: Caricamento

- Il **loader** carica in memoria un programma rilocabile
    - Risolti tutti gli indirizzi relativi (variabili, salti ecc.)
    - Caricati eventuali programmi di supporto
- **Rilocazione statica**: indirizzi logici trasformati in  indirizzi assoluti
- **Rilocazione  dinamica**: indirizzi logici mantenuti nel programma in esecuzione
    - Programma compilato: indirizzamento relativo
    - Tramite *registro base*: locazione in memoria del codice, dei dati e dello stack (reg. CS, DS e SS su x86)
    - *Memory Management Unit* in S.O.

---

title: Codice gestito

- Compilazione in **codice intermedio**
    - Bytecode (Java), Common Intermediate Lang. (.NET), …
    - Python: compilato per una macchina virtuale (file .pyc), ma in modo trasparente
- Esecuzione su una **macchina virtuale**, che gestisce la memoria (garbage collection)
    - Java Virtual Machine, Common Language Runtime, …
    - Spesso compilazione “al volo” (*Just In Time*) in codice nativo
- **Garbage collection**
    - Restituzione automatica della memoria
    - Per oggetti/dati che non servono più
    - Possibile anche per codice nativo: linguaggio *Go*, *“smart pointers”* in C++, estensioni…

---

title: Garbage collection
figure: images/dev/garbage-truck.jpg

- Vantaggi
    - Non è possibile dimenticare di liberare la memoria (*memory leak*)
    - Non è possibile liberare della memoria che dovrà essere utilizzata in seguito (*dangling pointer*)
- Svantaggi
    - Decide autonomamente quando liberare la memoria
    - Liberare e compattare mem. richiede del calcolo
- Diversi algoritmi
    - *Reference counting*: idea di base, ma cicli…
    - *Mark & sweep*: parte da riferimenti locali/globali, marca oggetti raggiungibili
    - *Generational garbage collection*: controlla spesso oggetti recenti

title: Qualità del software
subtitle: Introduzione all'informatica
figure: images/dev/bug-feature.jpg

---

title: Ciclo di vita del software
figure: images/dev/waterfall-model.svg
class: large-figure

- **Analisi**
    - Modello, requisiti, fattibilità
- **Progetto e implementazione**
    - Componenti architetturali... dettaglio classi
- **Collaudo**
    - Rispetto requisiti, qualità sw
- **Rilascio e manutenzione**
    - 40%-80% del costo totale (DoD, HP)
    - Non noti o non colti correttamente i requisiti
    - Cambiano le condizioni operative …

>

[Winston W. Royce, 1970](http://www.cs.umd.edu/class/spring2003/cmsc838p/Process/waterfall.pdf) - [Robert L. Glass, 2001](http://www.eng.auburn.edu/~hendrix/comp6710/readings/Forgotten_Fundamentals_IEEE_Software_May_2001.pdf)

---

title: Evoluzione di un sistema sw
figure: images/dev/rup-cycle.png
class: large-figure

- Evoluzione ineliminabile per molti sistemi
    - Prestazioni, qualità, funzionalità (manutenzione *perfettiva*, ~60%)
    - Anomalie ed errori (manutenzione *correttiva*, ~20%)
    - Mutamenti dell’ambiente (manutenzione *adattativa*, ~20%)
- Sviluppo iterativo e metodologie agili
    - Rilascio frequente ed incrementale
    - <http://agilemanifesto.org/>

---

title: Qualità del software
figure: images/dev/programmer.jpg
class: large-figure

- Le qualità su cui si basa la valutazione di un sistema software possono essere:
    - **Interne**, riguardano le caratteristiche legate al **processo** di sviluppo e non sono direttamente visibili agli utenti
    - **Esterne**, riguardano le funzionalità fornite dal **prodotto** sw e sono direttamente visibili agli utenti
- Le categorie sono legate:
    - *Product quality is process quality*

---

title: Qualità esterne

- **Correttezza e affidabilità**: il sistema rispetta le specifiche, l'utente può affidarsi al programma
- **Robustezza**: il sistema si comporta in modo ragionevole anche fuori dalle specifiche
- **Efficienza**: usa bene le risorse di calcolo
- **Scalabilità**: migliori prestazioni con più risorse
- **Sicurezza**: riservatezza, autenticazione, autorizzazione, accounting
- **Facilità d’uso**: interfaccia utente permette di interagire in modo naturale

---

title: Qualità interne

- **Verificabilità**: sistema basato su modello formale
- **Riusabilità**: parti per costruire nuovi sistemi
- **Manutenibilità**: riparabilità, evolvibilità (nuove specifiche), adattabilità (cambiamenti ambiente)
- **Interoperabilità**: capacità di co-operare con altri sistemi, anche di altri produttori
- **Portabilità**: adatto a più piattaforme hw/sw
- **Comprensibilità**: codice leggibile, documentato
- **Modularità**: interazione tra componenti coesi

---

title: Specifiche
figure: images/dev/gearwheel.png

- Rispetto a cosa valutiamo **correttezza** o **affidabilità** di un programma?
- Idea del programmatore
    - Non formulata, non documentata
    - Incompleta, mutevole, facilmente dimenticata
- Specifiche (formali o informali)
    - Formulate, scritte, studiate e condivise <br> → Parte del progetto e del programma
    - Spec. assiomatiche: espressioni logiche o asserzioni <br> → **Precondizioni, postcondizioni e invarianti**

---

title: Pre- e post-condizioni 

- **Precondizioni**
    - Stabiliscono se è possibile chiamare un metodo
    - Prerequisiti per l’attivazione
- **Postcondizioni**
    - Stabiliscono se il metodo restituisce il valore atteso, cioè se produce l’effetto desiderato
    - … In relazione ai parametri (che soddisfano le precondizioni)
    - Definiscono il significato del metodo
- **Divisione delle responsabilità** tra moduli
    - Errore del codice *chiamante* (*client*) se precondizioni non soddisfatte
    - Errore del codice *chiamato* (*server*), se postcondizioni non soddisfatte

---

title: Responsabilità e contratti

- **Precondizioni + postcondizioni = contratto**
    - … tra modulo chiamante e modulo chiamato
- Infrazione di un contratto: problema serio
    - Errore rispetto alle specifiche
    - Eccezione e/o terminazione
- No **divisione responsabilità** → sovrapposizioni
    - Tutti i moduli assumono molte responsabilità
    - Programmazione difensiva: tutte le parti del programma controllano tutte le condizioni
    - Grosso programma → ancora più grosso

---

title: Esempio di contratto

code: Python

    def sqrt(x: float) -> float

- Precondizioni: `x >= 0`
- Postcondizioni: `abs(result * result - x) <= 0.00001`
- Codice chiamante
    - Obblighi: deve passare un numero non negativo
    - Benefici: riceve la radice del numero
- Codice chiamato
    - Obblighi: restituisce un numero `r` tale che `r * r ≃ x`
    - Benefici: può assumere che `x` non è negativo

---

title: Invariante di classe

- Vincolo che deve valere per ogni stato stabile di un oggetto, durante tutto il suo ciclo di vita
- Rafforzamento generale di pre- e post-condizioni
- “Criterio di sanità” dell’oggetto
- Deve essere soddisfatto dal costruttore
- Deve essere mantenuto dai metodi pubblici
- Ma non necessariamente da metodi privati o protetti

---

title: Ereditarietà e contratti

![](images/dev/contract-inherit.svg)

- *Che relazione c’è tra le asserzioni di una classe e quelle dei suoi discendenti?*

---

title: Principio di sostituibilità

- Polimorfismo: possibile esecuzione metodo di una sottoclasse, anziché della classe base
    - I metodi delle sottoclassi possono ridefinire i metodi delle classi base... ma non arbitrariamente
- I contratti della sottoclasse devono *rispettare i contratti della classe base* (“sottocontratti”)
    - Precondizioni: non devono essere più forti
    - Postcondizioni: non devono essere più deboli
    - Invarianti di classe: non devono essere più deboli

> Require no more, promise no less

---

title: Design by contract

- Paradigma proposto nel linguaggio *Eiffel* (Betrand *Meyer*, 1986)
- Uso di asserzioni in varie fasi di sviluppo
    - Progetto: approccio pragmatico alle specifiche
    - Implementazione: guida per la programmazione
    - Documentazione: interfacce con info aggiuntive
    - Collaudo: DbC delimita i casi da testare (per affidabilità)
    - Manutenzione: DbC fa emergere prima gli errori
    - Uso finale: sollevate eccezioni se violazioni

---

title: Asserzioni Python

- Espressioni booleane, simili a predicati matematici
- Esprimono proprietà semantiche di classi e metodi
- Utili per collaudo e debugging, ma anche documentazione
- Violazione → **AssertionError** (e normalmente *abort*, terminazione programma)

code: Python

    assert age > 0

---

title: Asserzioni e contratti

- Asserzioni in genere utili per:
    - Precondizioni, postcondizioni, invarianti di classe
    - Invarianti interne e di controllo del flusso
- Argomenti di metodi pubblici sbagliati → eccezione
    - `ValueError` o `TypeError`
    - Di solito, asserzioni usate per debug...

---

title: Pre- e post-condizioni

code: Python

    def sqrt(x: float) -> float:
        '''
        Precondition: x >= 0
        Postcondition: abs(result * result - x) <= 0.00001
        '''
        if x < 0 raise ValueError("sqrt: arg < 0")

        # ...
        
        assert abs(result * result - x) <= 0.00001
        return result

---

title: Verifica e validazione
class: segue dark

---

title: Verifica e validazione
figure: images/dev/v-model.png
class: large-figure

- Mostrare che il sistema...
    - È conforme alle specifiche
    - Soddisfa i bisogni dell’utente
- Comprende revisione e collaudo del sistema
- **Test case**, derivati dalle specifiche

---

title: Costo dei bug
figure: images/dev/first-bug.jpg
class: large-figure

- Scovare bug non è un compito facile, e nemmeno una esperienza eccitante…
    - Costoso: non è insolito dedicare al testing il 40% del tempo e delle risorse di un progetto
- **Far emergere** bug in prime fasi dello sviluppo!
    - B. Boehm: se trovare e correggere un problema in fase di specifica dei requisiti costa 1$...
    - 5$ in progetto, $10 in programmazione,
    - $20 in unit testing, fino a $200 dopo consegna
    - Alcuni bug possono capitare già a causa di specifiche non ben chiare e capite

---

title: Prove formali

- Dimostrazione matematica di un programma: alternativa (~ accademica) al testing
    - Annotazione del programma con asserzioni matematiche: comportamento atteso
    - Proprietà valide per i vari costrutti del programma
- Prova che post-condizioni verificate, se:
    - Precondizioni verificate
    - Programma termina
- Dimostrazioni automatiche
    - Se a mano → errori (più che nel programma?)

---

title: Revisione del software

- Analisi del codice (o pseudocodice) per capirne le caratteristiche e le funzionalità
- **Code walk-through**
    - Selezione porzioni di codice e valori di input
    - Simulazione su carta comportamento del sistema
- **Code inspection**, più formale e focalizzato
    - Uso di variabili non inizializzate
    - Loop infiniti
    - Letture di porzioni di memoria non allocata
    - Rilascio improprio della memoria

---

title: Testing

> Le operazioni di testing possono individuare la presenza di errori nel software ma non ne possono dimostrare la correttezza. *(E. Dijkstra)*

> Eseguire un programma con l'intento di trovare errori. *(Glen Myers, “The art of Software Testing”)*

- Verificare sistema in un insieme abbastanza ampio di casi... → plausibile comportamento analogo anche nelle restanti situazioni

---

title: Classificazione dei test
figure: images/dev/v-model.png
class: large-figure

- Tipi di test
    - **White box** (*in the small*)
    - **Black box** (*in the large*)
- Livelli di test
    - *Unit test*
    - *Integration test*
    - *System test*
- Ripetizione di test
    - *Regression test*

---

title: Testabilità

- Qualità software che facilitano rilevazione errori
    - **Osservabilità** – Disponibili i risultati dei test
    - **Controllabilità** – Possibilità di impostare ingressi e stato del programma prima di eseguire un test
    - **Decomponibilità** – Programma diviso in parti che possono essere testate individualmente
    - **Comprensibilità** – Si capisce il comportamento corretto (desiderato) del programma
- → Sviluppo per testabilità

---

title: White-box testing
class: segue dark

---

title: White-box testing

- Test basati sulla conoscenza della struttura interna del codice
- Un errore non può essere scoperto se la parte di codice che lo contiene non viene mai eseguita
- **Statement test**
    - Insieme di test T tali che, eseguendo su tutti i casi di T il programma P, ogni istruzione di P venga eseguita almeno una volta (test utopia?)
    - **Branch test** (copertura delle decisioni)
    - **Branch & condition test** (… condizioni)

---

title: Basic path testing

- Scelto insieme minimo di percorsi per coprire tutte le istruzioni e condizioni (*white box*)
    - Tracciare diagramma di flusso
    - Astrarre il diagramma in un grafo di flusso
    - Complessità ciclomatica `n` = metrica di test
    - Trovare `n` casi di test che seguono ciascun cammino indipendente
- Cammino: sequenza di comandi, da inizio a fine
- Cammino indipendente: aggiunge almeno una nuova istruzione rispetto ai cammini già identificati

---

title: Diagramma di flusso
figure: images/dev/flow-chart.png
class: large-figure

code: Python

    def f():
        // entry 
        while a:
            x()
            if b:
                if c: y()
                else z()
                # p
            else:
                 v()
                 w()
            # q
        # exit: r

---

title: Grafo di flusso
figure: images/dev/flow-graph.png
class: large-figure

- Piccola astrazione rispetto a diagramma di flusso
- **Complessità ciclomatica**, dalla teoria dei grafi:
    - Numero di possibili cammini indipendenti, o...
    - Numero di regioni del grafo di flusso, o...
    - Numero di nodi predicato + 1 <br> &nbsp;
- `A, r`
- `A, X, B, C, Y, p, q, A, r`
- `A, X, B, C, Z, p, q, A, r`
- `A, X, B, V, W, q, A, r`

---

title: Black box testing
class: segue dark

---

title: Black box testing

- Sistema = scatola nera; si verificano le corrispondenze di input e output
    - White-box testing: impossibile per grandi sistemi
    - Test case scelti in base alle specifiche dei requisiti
- Desiderata: trovare errori...
    - Funzionali: otteniamo i risultati attesi per dati input di un metodo?
    - Interfaccia: dati passati correttamente tra i metodi?
    - Efficienza: il metodo è abbastanza veloce?

---

title: Partizioni d’equivalenza

- Partizionamento ingressi in **classi di equivalenza**
    - Irrealistico testare tutti i possibili ingressi (es. `sqrt`)
    - Ipotesi: sufficiente testare un solo caso per classe
    - Si includono casi limite e valori non validi
    - Precondizioni: riducono il numero di casi di test

code: Python

    def swap_elements(v: list, i: int, j: int):
        '''
        Exchange element i and j in list v
        v: empty, one element, more elements
        i, j: one or both indexes out of range... or both in range: i < j, i > j, i = j
        '''
        # ...

---

title: Regression testing

- Scopo: trovare errori di regressione
    - Errori in un programma che prima era corretto, ed è stato modificato di recente
    - Un errore di regressione è un errore che prima non c’era
- Dopo la modifica di una parte `P` nel programma `Q`
    - Testare che la parte `P` funzioni correttamente
    - Testare che l’intero programma `Q` non sia stato danneggiato dalla modifica



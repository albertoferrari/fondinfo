title: Linguaggio C++11
subtitle: Ereditarietà
figure: images/misc/cpp-logo.jpg

---

title: title: Ereditarietà

- Una nuova classe (classe derivata) viene creata a partire da una classe esistente (classe base)
- La classe derivata eredita le variabili membro e le funzioni membro della classe base
- Eredita interfaccia e implementazione
- Può aggiungere variabili membro e funzioni membro

---

title: Relazione “is a”

- Un oggetto di una classe derivata può essere usato ovunque può essere usato uno della classe base
- Un oggetto di una classe derivata ha più di un tipo
    - class HourlyEmployee : public Employee {
    - public:
    - HourlyEmployee(string name, string code,
    - double wageRate, double hours);
    - // …
    - private:
    - // …
    - };

---

title: Ridefinizione dei metodi

- Una classe derivata può cambiare la definizione di una funzione membro ereditata (overriding)
- In questo caso la definizione della classe derivata deve contenere la dichiarazione della funzione membro ereditata

---

title: Accesso a un metodo della classe base

- Una classe derivata può ridefinire una funzione della classe base
    È comunque possibile invocare su un oggetto della classe derivata la versione della funzione data nella classe base
- Per fare ciò si utilizza l’operatore ::, che in questo caso è obbligatorio, altrimenti la funzione chiamante continuerebbe in realtà a chiamare se stessa generando un loop

---

title: Overriding / overloading

- Overriding
    - Una funzione ridefinita in una classe derivata ha lo stesso numero e tipo di parametri della funzione della classe base
    - Sostituisce la funzione della classe base
- Overloading
    - Una funzione sovraccaricata in una classe derivata ha un diverso numero e/o tipo di parametri rispetto alla funzione della classe base
    - La classe derivata ha entrambe le funzioni

---

title: Uso dei membri privati della classe base

- I membri privati della classe base non sono referenziabili nelle definizioni delle funzioni membro della classe derivata
- Diversamente verrebbe violato il principio di incapsulamento
- Le funzioni membro della classe derivata possono accedere alle variabili membro private della classe base tramite le funzioni accessor e mutator
- Le funzioni membro private della classe base non sono accessibili (di fatto non sono ereditate)

---

title: Il qualificatore protected

- Una variabile o funzione membro qualificata come protected può essere referenziata nelle funzioni membro di una classe derivata
- Le variabili membro protected agiscono come se fossero protected in ogni classe derivata
- Molti ritengono che l’uso di variabili membro protected comprometta l’incapsulamento
    È quindi buona norma utilizzare protected solo quando assolutamente necessario

---

title: Cosa non viene ereditato

- Oltre alle funzioni membro private non vengono ereditati
    - Costruttori
    - Distruttori
    - Costruttori di copia
    - Operatori di assegnamento
- Se non vengono definiti vengono creati quelli di default

---

title: Costruttori nelle classi derivate

- I costruttori della classe base non sono ereditati
- Per inizializzare le variabili ereditate…
    - Un costruttore della classe derivata può invocare esplicitamente un costruttore della classe base
    - Altrimenti, viene invocato automaticamente il costruttore di default della classe base
    - HourlyEmployee::HourlyEmployee(string name, string number,
    - double wageRate, double hours)
    - : Employee(name, number), wageRate(wageRate), hours(hours) {
    - //deliberately empty
    - }

---

title: Ordine di chiamata dei costruttori

- La chiamata del costruttore della classe base è la prima azione del costruttore della classe derivata
- Se A ◅- B ◅- C, quando viene creato un oggetto di classe C…
    - prima viene chiamato un costruttore della classe A
    - poi un costruttore della classe B
    - poi vengono intraprese le rimanenti azioni del costruttore di classe C

---

title: Distruttori in classi derivate

- Quando il distruttore di una classe derivata è invocato, viene invocato automaticamente il distruttore della classe base
- I distruttori sono chiamati in ordine inverso rispetto ai costruttori
- Se A ◅- B ◅- C, quando termina lo scope di un oggetto di classe C…
    - viene chiamato prima il distruttore della classe C
    - poi quello della classe B
    - infine quello della classe A

---

title: Relazioni tra oggetti

- Relazione “is a”
    - Esempio: a HourlyEmployee is an Employee
    - Utile soprattutto per polimorfismo
    - Sempre possibile usare un oggetto di una sotto-classe al posto di un oggetto di una classe base
- Relazione “has a”
    - Esempio: *an Employee has a Date (of employment)*
    - Serve per riutilizzo di funzionalità
    - Grado elevato di flessibilità: ...
    - Gli oggetti membri sono di solito nascosti
    - Inaccessibili ai programmatori che usano l’oggetto esterno
    - Possono essere cambiati senza disturbare il codice esterno

---

title: Ereditarietà e riuso

- La classe base contiene il codice comune alle classi derivate
    - L’ereditarietà è una forma di riuso del codice
    - Si eredita il codice della classe base
- Ma la classe derivata è strettamente dipendente dalla classe base, ne eredita anche l’interfaccia!
    - Per il semplice riuso è meglio far ricorso al contenimento
    - Oggetti incapsulati forniscono funzionalità di base
    - Vedi Eckel, Thinking in C++: http://www.mindview.net/Books

---

title: Ereditarietà protetta e privata

- Ereditarietà protetta: i membri pubblici della classe base sono protetti nella classe derivata quando sono ereditati
- Ereditarietà privata: nessun membro della classe base può essere referenziato nella classe derivata
- La relazione “is a” non è valida
- Sono raramente usate

---

title: Ereditarietà multipla

- Una classe derivata può avere più di una classe base
- Possono esserci situazioni ambigue
- Richiede una conoscenza approfondita del linguaggio

---

title: Operatori di assegnamento in classi derivate

- Una classe derivata quando sovraccarica l’operatore di assegnamento può fare uso dell’operatore di assegnamento della classe base

code: c++

    Derived& Derived::operator=(const Derived& rtside)
    {
        Base::operator=(rtSide);
        //…
    }

---

title: Costruttori di copia in classi derivate

- Una classe derivata quando sovraccarica il costruttore di copia può fare uso del costruttore di copia della classe base

code: c++

    Derived::Derived(const Derived& obj) : Base(obj), …
    {
        // …
    }

---

title: Polimorfismo e funzioni virtuali

- Polimorfismo e funzioni virtuali sono un meccanismo fondamentale per realizzare sistemi estensibili
- Consentono di trattare gli oggetti di tutte le classi di una gerarchia come se fossero oggetti della classe base
- Risultato: scrittura di programmi più semplici (meno branching logic), in cui viene favorito il testing ed il mantenimento del codice

---

title: Metodi virtuali

- Quando un metodo di una classe base è dichiarato virtuale…
- Se invocato tramite un puntatore o un riferimento…
    - Il programma sceglie a tempo di esecuzione la funzione della classe appropriata (late binding o dynamic binding)
- Se invocato su un oggetto…
    - La risoluzione del riferimento avviene a tempo di compilazione (static binding) e la funzione chiamata è quella della classe dell’oggetto (ottimizzazione)

---

title: Metodi virtuali

- Per specificare che una funzione è virtuale si include il modificatore virtual nella dichiarazione (non nella definizione)
- Quando la definizione di una funzione virtuale viene cambiata in una classe derivata si parla di overriding
- La proprietà di essere una funzione virtuale viene ereditata lungo tutta la gerarchia

---

title: Polimorfismo

- Capacità di oggetti appartenenti a classi che derivano da una classe base comune di rispondere in modi diversi alla chiamata di una certa funzione
- Si implementa tramite le funzioni virtuali
    - Alla chiamata di una funzione virtuale tramite un puntatore o un riferimento alla classe base, il programma sceglie la ridefinizione corretta della funzione nella classe derivata appropriata

---

title: Polimorfismo

- Se una funzione non virtuale è ridefinita in una classe derivata non si ha polimorfismo
    - Se viene chiamata tramite un puntatore alla classe base, è utilizzata la versione della classe base
    - Se viene chiamata tramite un puntatore alla classe derivata, è utilizzata la versione della classe derivata

---

title: The slicing problem

- Assegnando un oggetto di una classe derivata a una variabile della sua classe base, le variabili e funzioni membro aggiunte dalla classe derivata vengono perse
- Il problema può essere risolto usando funzioni virtuali e puntatori

---

title: Overriding e overloading

- Il meccanismo di overriding è concettualmente molto diverso da quello di overloading, e non deve essere confuso con esso
- L'overloading consente di definire in una stessa classe più metodi aventi lo stesso nome, ma che differiscano nella signature
- L'overriding, invece, consente di ridefinire un metodo in una sottoclasse: il metodo originale e quello che lo ridefinisce hanno necessariamente la stessa firma, e solo a tempo di esecuzione si determina quale dei due deve essere eseguito

---

title: Implementazione delle funzioni virtuali

- Se una classe ha una o più funzioni membro virtuali il compilatore crea una tabella che per ogni funzione virtuale contiene l’indirizzo in memoria del codice della funzione
- Quando viene creato un oggetto della classe, la sua descrizione contiene un puntatore alla tabella delle funzioni virtuali
- Quando una funzione virtuale viene chiamata usando un puntatore all’oggetto, il sistema runtime usa la tabella invece del tipo del puntatore per decidere quale definizione della funzione usare
- Le funzioni virtuali introducono overhead

---

title: Classi astratte e funzioni virtuali pure

- Se una funzione è virtuale pura la sua definizione non è necessaria
- Una classe con una o più funzioni virtuali pure è detta astratta
- Una classe astratta può essere usata solo come classe base per derivare altre classi, non si possono creare oggetti
    - Ex: class Abs { public: virtual void f() = 0; };

---

title: Ereditarietà di interfaccia e di implementazione

- Con l’ereditarietà pubblica si può ereditare:
    - La sola interfaccia (funzioni virtuali pure), oppure...
    - L’interfaccia più...
    - Un’implementazione di default (funzioni virtuali)
    - Un’implementazione obbligatoria (funzioni non virtuali)
- È bene non ridefinire le funzioni ereditate non virtuali

---

title: Distruttori delle classi base

- Se si dealloca un oggetto di una classe derivata attraverso un puntatore alla classe base e la classe base ha un distruttore non virtuale, il risultato è indefinito
- È bene dichiarare virtuali i distruttori delle classi base

---

title: Polimorfismo

- Aumento di generalità: è il runtime a doversi occupare delle specificità, non il programmatore
- Estendibilità: il codice è scritto indipendentemente dai tipi derivati, nuovi tipi possono essere aggiunti senza dover apportare modifiche a quanto già sviluppato

---

title: Funzioni virtuali e parametri di default

- Quando si eredita una funzione virtuale con un parametro di default, è bene non cambiarne il valore
- Motivazione
    - Le funzioni virtuali usano dynamic binding
    - I parametri di default usano static binding

---

title: Upcasting e downcasting

- Il casting da un tipo discendente a un tipo antenato è detto upcasting ed è sicuro
- Il casting da un tipo antenato a un tipo discendente è detto downcasting ed è pericoloso

---

title: Dynamic cast

- Consente di fare un downcasting sicuro
- Va usato su puntatori
- Se il cast riesce (cioè se il tipo dinamico corrisponde al tipo che si vuole ottenere), restituisce un puntatore al nuovo tipo, altrimenti restituisce NULL

---

title: Template

- I template consentono di definire funzioni e classi molto generali che hanno parametri al posto dei tipi
- Tecnica particolarmente apprezzata perché consente una notevole riusabilità del software

---

title: Template di Funzioni

- I template di funzioni supportano l’astrazione algoritmica: esprimere algoritmi in modo molto generale trascurando dettagli implementativi
    - Esempio: scambio dei valori di due variabili

---

title: Funzioni Template: Sintassi

- La dichiarazione e la definizione di una funzione template devono essere precedute dal prefisso di template
    - template<class T>
- Una funzione template corrisponde a un insieme di definizioni di funzione, il compilatore ne produce una per ogni tipo per cui si usa il template

---

title: Funzioni Template: Sintassi (2)

- È possibile avere template di funzioni con più di un parametro di tipo
    - template<class T1, class T2>
- Generalmente si usano template di funzioni con un solo parametro di tipo

---

title: Funzioni Template e Compilatori

- Molti compilatori non supportano la compilazione separata e richiedono che la definizione della funzione template sia nello stesso file in cui viene usata, prima della prima invocazione
    È possibile mettere la definizione della funzione template in un file separato ed includere questo file

---

title: Definzione e Uso di Funzioni Template

    È buona norma scrivere prima una funzione ordinaria e, solo dopo che la si è verificata, convertirla in un template
- Una funzione template può essere usata per ogni tipo per cui il codice della funzione ha senso

---

title: Template di Classi

- La definizione di una classe template deve essere preceduta da
    - template<class T>
- Le funzioni membro sono template
- Specificando il tipo è possibile dichiarare oggetti della classe template, usare il nome della classe come tipo di un parametro di una funzione, …

---

title: Template di Classi (2)

- Spesso le definizioni di classi template hanno restrizioni implicite sui tipi che possono essere sostituti al parametro
- Molti compilatori non supportano la compilazione separata, occorre includere anche il file di implementazione nel file di applicazione

---

title: Template ed Ereditarietà

    È possibile definire una classe template derivata a partire da una classe base (anche non template)

---

title: Gestione delle Eccezioni

- C++ fornisce strumenti per gestire situazioni eccezionali
- Terminologia
    - Sollevare un’eccezione (to throw an exception) = segnalare una situazione eccezionale
    - Intercettare l’eccezione (to catch or handle the exception) = gestire la situazione eccezionale

---

title: Costrutto try-throw-catch

code: c++

    try
    {
        /* Some statements */
        if (Exceptional_Case) throw exception;
        /* Some more statements */
    }
    catch(Type e)
    {
        /* Code to be performed if a value of type `Type` */
        /* is thrown in the try block */
    }

---

title: Blocco try

- Contiene il codice per gestire le situazioni normali
- Può riconoscere e segnalare situazioni speciali sollevando eccezioni
- Se non si verificano eccezioni, l’esecuzione del blocco try è quella standard
- E’ buona norma inserire in un blocco try il solo codice che potenzialmente può sollevare un’eccezione

---

title: Istruzione throw

- Usata per “lanciare” un valore detto eccezione
- Il valore lanciato può essere di qualsiasi tipo
- L’esecuzione del blocco try termina e il controllo passa a un blocco catch

---

title: Blocco catch

- Contiene il codice per gestire la situazione eccezionale
- Ha un parametro che
    - Specifica quale tipo di valore può essere intercettato dal blocco
    - Consente di utilizzare il valore intercettato all’interno del blocco
- Se non viene sollevata nessuna eccezione l’esecuzione del blocco try viene completata e il blocco catch viene ignorato
- Una volta completato il blocco catch, viene eseguito il codice che segue
- Un blocco catch risponde solo a un blocco try immediatamente precedente
- Se non c’è un blocco catch del tipo opportuno il programma termina

---

title: Classi di Eccezioni

- Sono classi i cui oggetti contengono l’informazione che si vuole lanciare al blocco catch
- In questo modo si ottiene un diverso tipo per ogni possibile situazione eccezionale
- Può essere utile definire una gerarchia di classi di eccezioni

---

title: Eccezioni Multiple

- Un blocco try può potenzialmente sollevare più eccezioni di tipi diversi
- In ogni esecuzione verrà sollevata al massimo una eccezione
- Ogni blocco catch può intercettare valori di un solo tipo
- Si possono avere più blocchi catch dopo un blocco try per gestire eccezioni di tipo diverso

---

title: Blocco catch di Default

- Quando in un blocco try viene sollevata un’eccezione, i blocchi catch che seguono sono considerati in ordine, viene eseguito il primo che intercetta quel tipo di eccezione
- Blocco catch speciale che intercetta ogni tipo di eccezione, da usare come default
    - catch(…) { cout << “Unexplained exception”;}

---

title: Sollevare un’Eccezione in una Funzione

- Spesso è utile ritardare la gestione di un’eccezione
- Una funzione può sollevare un’eccezione e non intercettarla
- Sarà il programma che usa la funzione a gestire l’eccezione
- Il programma metterà la chiamata della funzione in un blocco try seguito da un blocco catch che intercetta l’eccezione

---

title: Specifica delle Eccezioni

- Elenca le eccezioni che possono essere sollevate da una funzione e non vengono da essa intercettate
- Deve apparire sia nella dichiarazione che nella definizione della funzione
- Se viene sollevata un’eccezione che non viene intercettata e non compare nella specifica, viene chiamata la funzione unexpected che per default termina il programma, ma può essere ridefinita

---

title: Specifica delle Eccezioni ed Ereditarietà

- Se B->D, un’eccezione di tipo D viene gestita come se fosse di tipo B, anche rispetto alla specifica
- Quando si dà una nuova definizione o si fa overriding di una funzione ereditata, non si possono aggiungere eccezioni alla specifica, ma se ne possono eliminare

---

title: Quando Sollevare un’Eccezione

- Se la funzione è in grado di gestire in modo semplice il caso speciale, non deve sollevare l’eccezione
- Se invece il modo in cui il caso speciale va gestito dipende da dove la funzione è usata, si delega la gestione al livello superiore (le eccezioni non intercettate risalgono di scope)
- Non usare le eccezioni nei distruttori

---

title: Esempio: Allocazione Dinamica

code: c++

    #include <new>
    using std::bad_alloc;
    //…
    try
    {
        int *p = new int[100];
    }
    catch(bad_alloc)
    {
        cout << “Cannot alloc p”;
        //…
    }

---

title: Abuso delle Eccezioni

- La gestione delle eccezioni genera overhead sia temporale che spaziale
- Le istruzioni throw rendono contorto il flusso di controllo (come le istruzioni di salto)
- La gestione delle eccezioni va usata con moderazione

---

title: Vantaggi della Gestione delle Eccezioni

- In un linguaggio che non la supporta si può restituire un codice di errore
    - Occorre controllarlo ogni volta
    - Il programma può ignorarlo
    - Alcune funzioni non possono restituire un codice di errore
- In C++
    - Gestione uniforme delle eccezioni per tutte le funzioni
    - L’eccezione non può essere ignorata
    - Non si mescola la gestione del caso speciale e dei casi normali
    - Migliora la gestione delle variabili locali

---

title: Strutture Dati Collegate

- Sono composte da variabili dinamiche di tipo struct o classe dette nodi
- I nodi contengono puntatori che puntano ad altri nodi
- La Standard Template Library (STL) contiene versioni predefinite di queste strutture dati

---

title: Liste Concatenate

- Sono liste di nodi in cui ogni nodo contiene un puntatore che punta al nodo successivo
- Il primo nodo è detto testa, la lista è referenziata tramite un puntatore alla testa
- L’ultimo nodo contiene un puntatore NULL

---

title: Pile o Stack

- Una pila (o stack) è una struttura dati che gestisce i dati in modo LIFO
- Ha due operazioni base:
    - Aggiungere un elemento in cima alla pila (push)
    - Prelevare un elemento dalla cima della pila (pop)
- Può essere implementata tramite una lista concatenata

---

title: Code

- Una coda (o queue) è una struttura dati che gestisce i dati in modo FIFO
- Può essere implementata tramite una lista concatenata
- Occorrono due puntatori: uno alla testa e un uno alla fine della lista

---

title: Classi friend

- Se una classe F è friend di una classe C, tutte le funzioni membro di F sono friend della classe C

code: c++

    class F; // forward declaration
    class C
    {
    public:
        /*…*/
        friend class F;
        /*…*/
    };
    class F
    { /*…*/ };

---

title: Iteratori

- Un iteratore è un costrutto usato per indicare un elemento all’interno di una struttura dati
- Una classe iteratore estende il concetto di puntatore definendo operatori che consentono di usare la sintassi dei puntatori con gli oggetti della classe (++, --, ==, !=, *)
- Un iteratore è usato insieme a una classe struttuta dati che ha le funzioni membro begin() e end()

---

title: Standard Template Library

- Progettata per gestire insiemi di dati in modo comodo ed efficiente senza conoscere dettagli implementativi
- Fa parte dello standard C++
- È basata sulla programmazione generica
- Containers
    - Sono classi template usate per contenere insiemi di dati
- Iterators
    - Servono per muoversi nell’insieme di dati
- Algorithms
    - Implementazioni di molti algoritmi per operare sull’insieme di dati

---

title: Iteratori

- È un’astrazione progettata per nascondere i dettagli implementativi e fornire un modo uniforme per esplorare le strutture dati
- Ogni classe container ha il suo tipo di iteratori ma la terminologia, la sintassi e la semantica sono le stesse

---

title: Operatori che Operano sugli Iteratori

- Operatore di incremento ++ (in forma prefissa e postfissa)
    - Fa avanzare l’iteratore all’elemento successivo
- Operatore di decremento -- (in forma prefissa e postfissa)
    - Fa retrocedere l’iteratore all’elemento precedente
- Operatori di confronto == e !=
    - Per verificare se due iteratori puntano allo stesso elemento
- Operatore di dereferenziazione *
    - Per accedere all’elemento puntato dall’iteratore (l’accesso può essere di sola lettura)

---

title: Iteratori e Containers

- Le classi container hanno due funzioni membro che restituiscono iteratori collocati in posizioni speciali
    - begin() restituisce un iteratore che punta al primo elemento
    - end() restituisce un valore speciale che può essere usato per verificare se un iteratore punta oltre l’ultimo elemento

---

title: Tipi di Iteratori

- Gli iteratori sono classificati secondo il tipo di operazioni ad essi applicabili
    - Forward iterators: si può applicare l’operazione ++
    - Bidirectional iterators: si possono applicare le operazioni ++ e --
    - Random access iterators: si possono applicare le operazioni ++ e -- e si può accedere a qualsiasi elemento in un solo passo
- Ogni categoria include le precedenti

---

title: Iteratori constant e mutable

- Un iteratore di qualsiasi tipo è
    - Constant se l’operatore * restituisce l’elemento puntato come r-value
    - Mutable se l’operatore * restituisce l’elemento puntato come l-value
- Se una classe container ha iteratori mutable, ha anche iteratori const

---

title: Reverse Iterators

- Se una classe container ha iteratori bidirezionali, per passare gli elementi in ordine inverso si possono usare i reverse iterators
- La funzione membro rbegin() restituisce un iteratore che punta all’ultimo elemento
- La funzione membro rend() restituisce un valore speciale che può essere usato per verificare se un reverse iterator punta oltre il primo elemento
- L’operatore ++ fa avanzare un reverse iterator in senso inverso

---

title: Sequential Containers

- Gli elementi sono ordinati in base al modo in cui sono inseriti
    - slist (lista concatenata semplice, non standard)
    - list (lista concatenata doppia)
    - vector
    - deque (coda in cui si inseriscono e rimuovono elementi a entrambe le estremità)

---

title: Lists (vs vectors)

- Gli elementi non sono contigui in memoria
- Non forniscono accesso casuale agli elementi
- L’inserimento e la rimozione degli elementi impiegano lo stesso tempo in tutte le posizioni
- L’inserimento o la rimozione di un elemento non invalidano puntatori, iteratori e reference

---

title: Container Adapters

- Sono classi template implementate a partire da altre classi
    - stack, queue basate su deque
    - priority_queue basata su vector
- È possibile specificare un container sottostante differente da quello di default
    - Es: stack<int, vector<int> >

---

title: Associative Containers

- Ogni elemento ha associato un valore detto chiave
- Gli elementi sono individuati per mezzo della chiave
- set, multiset, map, multimap

---

title: Set

- Ogni elemento coincide con la sua chiave
- Ogni elemento può comparire al più una volta
- Per motivi di efficienza memorizza gli elementi in ordine rispetto al loro valore (i set sono implementati come alberi binari)
- Per default l’ordinamento usa l’operatore <
    È possibile specificare un diverso criterio di ordinamento purché sia
    - Antisimmetrico: op(x,y)=TRUE -> op(y,x)=FALSE
    - Transitivo: op(x,y)=TRUE && op(y,z)=TRUE -> op(x,z) = TRUE
    - Irriflessivo: op(x,x) = FALSE
- multiset è come set ma consente la ripetizione degli elementi

---

title: Map

    È un insieme di coppie ordinate di elementi (corrisponde a una funzione)
    - Es: map<string, int> numberMap;
- Per motivi di efficienza memorizza gli elementi in ordine rispetto al valore della chiave
- Se non si specifica un ordinamento, viene usato quello di default
- multimap è come map ma consente che più valori siano associati alla stessa chiave

---

title: Generic Algorithms

- STL contiene algoritmi generici
- STL specifica non solo
    - sintassi (interfaccia)
    - semantica (relazioni di I/O)
- ma anche
    - tempo di calcolo

---

title: Miscellanea

- Regole di buona programmazione
    - Pre-condizioni e post-condizioni
    - Programmazione difensiva
    - La macro assert
- Checklist for class authors
- Cosa fare ora

---

title: Pre-condizioni e Post-condizioni

    È buona norma includere nella dichiarazione di una funzione un commento che indichi
    - Pre-condizioni: condizioni che devono esistere quando la funzione è chiamata
    - Post-condizioni: condizioni che si verificano dopo che la funzione è eseguita
    -     Descrizione del valore ritornato o delle modifiche al valore degli argomenti

---

title: Pre-condizioni e Post-condizioni

- Esempio
    - void showInterest(double balance, double rate);
    - //Precondition: balance is a non-negative savings
    - //account balance, rate is the interest rate expressed
    - //as a percentage, such as 5 for 5%.
    - //Postcondition: the amount of interest on the given
    - //balance at the given rate is shown on the screen.

---

title: Programmazione Difensiva

- Metodologia che punta alla prevenzione dell’errore piuttosto che alla sua correzione
- Si introducono controlli (detti invarianti) in punti del programma in cui certe condizioni devono sicuramente essere verificate

---

title: La Macro assert

- Un altro modo per introdurre controlli di errore al fine di documentare e verificare la correttezza dei programmi
- Valuta un’espressione booleana:
    - se è vera non accade nulla
    - se è falsa il programma termina e invia un messaggio di errore

---

title: La Macro assert (2)

- Può essere usata per verificare le pre-condizioni
    È definita nella libreria cassert
- Utile nella fase di debug, dopo il test introduco #define NDEBUG e gli assert vengono ignorati
    - assert infatti è definita come una macro: definendo NDEBUG prima di includere assert.h, si disattiva la macro

---

title: Deallocazione autom.

- Reference counting vs. garbage collection
    - Quando ci sono 0 riferimenti, oggetto rimosso
    - Risolve maggior parte di memory leak
    - Non funziona con riferim. ciclici! (Cfr. weak_ptr)
- TR1 (2005) di C++ introduce shared_ptr
    - // vector<Polygon*> elements; vector<shared_ptr<Polygon> > elements;
    - Oggetti rimossi quando si distrugge il vector
    - O cmq quando si annulla l'ultimo shared_ptr
- *Last one out, turn off the lights*

---

title: Lista con smart ptr

code: c++

    #include <tr1/memory>
    typedef std::tr1::shared_ptr<Polygon> PolyPtr;

    class ListOfPolygons {
      public:
        void addElement(Polygon* p); // Same signature, or...
        Polygon* getElement(int i);  // PolyPtr everywhere
        int getSize();
        void sort();
      private:
        vector<PolyPtr> elements;
    }
    typedef std::tr1::shared_ptr<ListOfPolygons> ListPtr;

    void ListOfPolygons::addElement(Polygon* p) {
      elements.push_back(PolyPtr(p));
    }
    Polygon* ListOfPolygons::getElement(int i) {
      return elements[i].get();
    }
    int ListOfPolygons::getSize() { return elements.size(); }

---

title: Smart ptr all'opera

code: c++

    // Create a list and fill it with polygons
    ListPtr list(new ListOfPolygons());
    list->addElement(new Rectangle(5, 7));
    list->addElement(new Square(6));
    list->addElement(new Triangle(3, 4, 5));
    list->addElement(new RegularPolygon(5, 7));

    // Print areas
    list->sort();
    for (int i = 0; i < list->getSize(); ++i) {
      PolyPtr p(list->getElement(i));
      cout << p->getName() << ": " << p->area();
    }

    // Delete polygons and list
    list = NULL; // No need to do anything else!



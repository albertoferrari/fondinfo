title: Linguaggio C++11
subtitle: Classi e oggetti
figure: images/misc/cpp-logo.jpg

---

title: Classi e Oggetti

- Una classe è un tipo che ha variabili membro e funzioni membro
- Il valore di una variabile di un tipo classe è detto oggetto
- Un programma è un insieme di oggetti che interagiscono

---

title: Incapsulamento

- Una classe è un tipo completo
- Un tipo di dato consiste di
    - Un insieme di valori
    - Un insieme di operazioni
- È un tipo di dato astratto (ADT) se l’utilizzo è indipendente dall’implementazione dei valori e delle operazioni
- I tipi di dati predefiniti sono ADT
- Le classi devono essere ADT

---

title: Membri Privati e Pubblici

- I membri privati possono essere referenziati solo all’interno delle definizioni delle funzioni membro
- I membri pubblici possono essere referenziati ovunque
- È buona norma rendere private tutte le variabili membro e pubbliche le sole funzioni membro necessarie (quelle che espongono le funzionalità della classe)

---

title: Sezioni Pubblica e Privata

- Generalmente si definisce una sola sezione pubblica e una sola sezione privata
- Generalmente la sezione pubblica compare prima (per maggior chiarezza verso chi legge il codice)
- In assenza di specificazione C++ considera i membri privati (il che è di nuovo indicativo della necessità di nascondere il maggior numero possibile di dettagli)

---

title: Classi: Utilizzo Pratico

- Una volta definita, la classe può essere usata per dichiarare oggetti, array, puntatori e riferimenti

code: c++

    Time sunset;
    Time arrayOfTimes[5];
    Time *pointerToTime;
    Time &dinnerTime = sunset;

---

title: Funzioni accessor e mutator

- Le funzioni accessor consentono di leggere i dati dell’oggetto
- Le funzioni mutator consentono di modificare i dati dell’oggetto
- Queste funzioni forniscono un accesso controllato ai dati
- Generalmente si definiscono setter/getter functions
- E’ buona norma mantenere private le variabili membro e dotarle di funzioni accessor e mutator solo se necessario
- Una funzione che setta il valore di un dato dovrebbe anche controllare la validità di tale valore (validation) e lasciare comunque il dato in uno stato consistente (oppure lanciare un’eccezione...)

---

title: Interfaccia ed Implementazione

- L’interfaccia di una classe consiste di
    - Dichiarazioni delle funzioni membro pubbliche
    - Commenti
- L’implementazione di una classe consiste di
    - Variabili membro e dichiarazioni delle funzioni membro private
    - Definizioni delle funzioni membro
- Generalmente stanno in file diversi, ma è importante la separazione concettuale
- L’interfaccia viene generalmente definita in un file header
- Il file header sarà incluso da tutti i file che vogliono fare uso della classe (direttiva `#include`)
- Chi vende librerie software, fornisce ai clienti i soli file header e il codice oggetto

---

title: Programmazione Orientata agli Oggetti

- Un programmatore deve poter usare la classe conoscendo solo l’interfaccia
- Vantaggio: è possibile cambiare l’implementazione senza dover cambiare qualsiasi altro codice che usi la classe
- Filosofia: descrivere il problema in termini di oggetti che interagiscono, piuttosto che algoritmi che operano su dati (anche algoritmi e dati possono cambiare...)

---

title: Classe di Esempio: Interfaccia

code: c++

    // prevent multiple inclusions of header file
    #ifndef TIME1_H
    #define TIME1_H
    // Time abstract data type definition
    class Time {
    public:
        Time(); // constructor
        void setTime( int, int, int ); // set hour, minute, second
        void printMilitary(); // print military time format
        void printStandard(); // print standard time format
    private:
        int hour; // 0 - 23
        int minute; // 0 - 59
        int second; // 0 - 59
    };
    #endif

---

title: Classe di Esempio: Implementazione

code: c++

    …
    #include "time1.h"
    Time::Time() { hour = minute = second = 0; }
    void Time::setTime( int h, int m, int s ) {
        hour = (h >= 0 && h < 24) ? h : 0;
        minute = (m >= 0 && m < 60) ? m : 0;
        second = (s >= 0 && s < 60) ? s : 0;
    }
    void Time::printMilitary() {
        cout << (hour < 10 ? "0" : "") << hour << ":“
             << (minute < 10 ? "0" : "") << minute;
    }
    void Time::printStandard() {
        cout << ((hour == 0 || hour == 12) ? 12 : hour % 12) << ":"
             << (minute < 10 ? "0" : "") << minute << ":"
             << (second < 10 ? "0" : "") << second
             << (hour < 12 ? " AM" : " PM");
    }

---

title: Classe di Esempio: Utilizzo

code: c++

    …
    #include "time1.h"
    int main() {
        Time t1;
        t1.setTime(17, 15, 0);
        t1.printStandard();
        Time *t2 = new Time();
        t2->setTime(17, 20, 0); // (*t2).setTime(17, 20, 0);
        t2->printStandard(); // (*t2).printStandard();
        delete t2;
    }

---


---

title: Costruttore

    È una funzione membro che viene chiamata automaticamente quando viene dichiarato un oggetto della classe
- Usata per operazioni di inizializzazione
- Deve avere lo stesso nome della classe
- Non può ritornare un valore
- Deve stare nella sezione pubblica della classe
- Non può essere invocato come le altre funzioni membro
- Definizione alternativa preferibile: sezione di inizializzazione (vedi)
- Spesso si ha overloading dei costruttori

---

title: Costruttore senza Argomenti

- Quando si dichiara una variabile di tipo classe e si vuole invocato il costruttore senza argomenti, non si usano le parentesi
    - Esempio: DayOfYear date;

---

title: Chiamata Esplicita del Costruttore

- Il costruttore può essere chiamato esplicitamente per modificare le variabili membro di un oggetto
- Crea un oggetto anonimo e lo inizializza con i valori degli argomenti
- L’oggetto anonimo può essere assegnato a una variabile del tipo classe
    - Esempio: DayOfYear date(4, 5);
    - date = DayOfYear(10, 14);
    È più efficiente usare le mutator functions
- Se sono disponibili sia costruttore/i che mutator functions, queste è consigliabile siano chiamate anche dal costruttore (per non ripetere codice)

---

title: Costruttore di Default

- Un costruttore senza argomenti è detto costruttore di default
- Se non definiamo nessun costruttore viene creato un costruttore di default
- Se definiamo almeno un costruttore il costruttore di default non viene creato
    È bene includere sempre il costruttore di default

---

title: Sezione di Inizializzazione

- Le variabili membro vengono create e inizializzate dal costruttore nell’ordine in cui sono definite nella classe
- La sezione di inizializzazione è più efficiente per variabili membro di tipo classe
- Le variabili membro possono essere inizializzate all’interno di una sezione di inizializzazione, mentre costanti, riferimenti e membri di tipo classe devono utilizzare tale costrutto

---

title: Sezione di Inizializzazione

code: c++

    class Increment {
    public:
        Increment(int c = 0, int d = 1);
        void addDelta() { count += delta; }
        void print() const;
    private:
        int count;
        const int delta; // const data member
    };
    // Constructor for class Increment
    Increment::Increment(int c, int d)
        : delta( d ) // initializer for const member
    {
        count = c;
    }

---

title: Variabili Membro di Tipo Classe

- Una classe può avere una variabile membro di tipo classe (ovvio: i programmi sono costruiti da classi!)
- Notazione speciale per invocare il costruttore della variabile membro nel costruttore della classe più esterna
- I parametri del costruttore della classe più esterna possono essere usati nella chiamata del costruttore della variabile membro

---

title: Distruttori

- Funzione membro chiamata automaticamente quando un oggetto viene distrutto
- Non riceve parametri e non restituisce valori
- Una classe deve avere un unico distruttore
- Naming: ~ + nomeClasse
- Il distruttore non distrugge materialmente l’oggetto, ma è delegato a compiere tutte quelle operazioni utili prima che l’oggetto venga distrutto (es.: rilascio della memoria allocata dinamicamente)
- Chiamati in ordine inverso rispetto ai costruttori

---

title: Il Modificatore const: 1° Uso

- Per un parametro di tipo classe il passaggio call-by-reference è più efficiente del passaggio call-by-value
- Per i parametri di tipo classe va sempre usato il passaggio call-by-reference
- Se la funzione non modifica il parametro si usa il modificatore const

---

title: Il Modificatore const: 2° Uso

- Altro uso di const: per segnalare che una funzione membro non modifica l’oggetto chiamante
- Va messo sia nella dichiarazione che nella definizione
- Attenzione: const richiede consistenza!

---

title: Reference come Valore di Ritorno

- E’ possibile per una funzione membro pubblica ritornare una reference a membri privati della classe
- Per quanto sintatticamente corretta, questa operazione può violare il principio di information hiding

---

title: Reference come Valore di Ritorno (2)

code: c++

    #ifndef TIME4_H
    #define TIME4_H
    class Time {
    public:
        Time( int = 0, int = 0, int = 0 );
        void setTime( int, int, int );
        int getHour();
        int &badSetHour( int ); // DANGEROUS reference return
    private:
        int hour;
        int minute;
        int second;
    };
    #endif

---

title: Funzioni inline

- La definizione di una funzione membro può essere posta all’interno della definizione della classe
- Il compilatore inserisce il codice della funzione in ogni punto di chiamata
- Svantaggio: mescoliamo interfaccia e implementazione
- Definire inline solo funzioni molto corte

---

title: Membri static: Variabili

- Una variabile membro static è condivisa da tutti gli oggetti di una classe
- Usata dagli oggetti della classe per comunicare e coordinarsi
- Solo gli oggetti della classe possono accedervi
- Se public, allora accessibile con scope resolution
- Va inizializzata al di fuori della definizione della classe, una sola volta

---

title: Membri static: Funzioni

- Una funzione membro static accede solo ai membri static
- Non può accedere ai dati dell’oggetto chiamante
- Viene invocata usando il nome della classe e lo scope resolution operator (::)
- La parola chiave static va messa solo nella dichiarazione

---

title: Overloading di operatori

- Gli operatori (+, -, ==, …) non sono altro che…
- Funzioni usate con una sintassi particolare
- C++ consente di sovraccaricare gli operatori così che accettino argomenti di tipo classe
    - Caratteristica tra le più apprezzate del linguaggio
    - Può rendere alcuni programmi più chiari rispetto a chiamate a funzione equivalenti
    - Non abusarne quando invece l’uso non è chiaro!
- Almeno uno degli operandi deve essere di tipo classe

---

title: Overloading di operatori

- Un operatore si scrive come una comune funzione
    - Nome dato dalla parola chiave operator seguita dal simbolo dell’operatore di cui fare l’overloading
- Unici operatori predefiniti su membri di tipo classe:
        = (assegnamento)
        & (indirizzo)
- L’overload deve essere sempre esplicito
    - Es. Overload di = non condiziona +=, -= o !=
    - Es. Se si implementa solo l’op. +, non si può usare +=

---

title: Overloading di operatori come funzioni membro

- Il primo operando è l’oggetto chiamante, quindi:
    - Gli operatori binari hanno un solo parametro
    - Gli operatori unari non hanno parametri
- Vantaggi
        È più nello spirito OOP
        È più efficiente
- C’è uno svantaggio
    - Il primo operando (l’oggetto più a sinistra) deve essere membro della classe
    - Non sempre conviene, non sempre è possibile
    - Es. operatori >> e <<

---

title: Costruttori e conversione di tipo automatica

- Conversioni automatiche di tipo
    - Se definizione di classe contiene i costruttori appropriati
    - Es.: myAmount + 25
    - Creato un oggetto di classe Amount
    - Al costruttore viene passato 25
- Operatore binario sovraccaricato come membro
    - Conversione automatica del 2° operando (argomento)
    - Non del 1° (oggetto chiamante)
    - Es.: 25 + myAmount
    - Non funziona, se operatore membro

---

title: Overloading di operatori come funzioni non membro

    È possibile effettuare l’overloading semplicemente dichiarando le funzioni, senza necessità che siano membro della classe
- Svantaggio: non potendo accedere ai campi privati, hanno necessità di utilizzare accessor
    - La classe è obbligata a fornire tali accessor
    - Overhead nella chiamata degli accessor
- Perciò, gli operatori non membro generalmente sono dichiarati come friend (…)

---

title: Funzioni friend

- Una funzione friend di una classe ha accesso ai membri privati della classe pur non essendone membro
- Dichiarata friend nella definizione della classe
    - Per chiarezza meglio se all’inizio
    - Viene definita e chiamata come una funzione ordinaria
- Le funzioni friend hanno migliori prestazioni
    - Non necessitano di accessor

---

title: Funzioni friend

- Le funzioni friend più comuni sono gli operatori sovraccaricati
- Una funzione può essere friend di più classi
- Offrono il vantaggio della conversione automatica di tutti gli operandi
- Ma per alcuni autori non sono nello spirito OOP
- Evitarle, se possibile: violano l’incapsulamento

---

title: Funzioni friend: esempio

code: c++

    #include <iostream>
    using std::cout;
    using std::endl;
    class Count {
        friend void setX( Count &, int ); // friend declaration
    public:
        Count() { x = 0; }
        void print() const { cout << x << endl; } // output
    private:
        int x; // data member
    };
    // Can modify private data of Count because
    // setX is declared as a friend function of Count
    void setX( Count &c, int val ) {
        c.x = val; // legal: setX is a friend of Count
    }

---

title: Returning by const value

- Se una funzione ritorna un oggetto, l’uso di const per il valore ritornato impedisce che l’oggetto possa essere modificato
    - Es: (m1+m2).input(); // compiler error
- Per le funzioni accessor che ritornano variabili membro di tipo classe è bene usare const per il valore ritornato
- Ritornare valori di tipi predefiniti come const non ha senso


---


---

title: Operatori << e >>

- Operatori << e >> sovraccaricati per I/O degli oggetti di una classe
- Notazione di immediata comprensione
- Non possono essere sovraccaricati come membri
- L’operatore più a sinistra è infatti rispettivamente ostream& oppure istream&
- Non è del tipo della classe per cui si vogliono sovraccaricare << e >>

---

title: Operatori << e >>

- Di fatto le chiamate effettuate sono nella forma:
    - cin >> object; // operator>>(cin, object);
- Gli operatori << e >> ritornano rispettivamente un oggetto ostream e istream
- In questo modo, si possono concatenare più chiamate all’operatore stesso
    - cout << object1 << object2;

---

title: Operatore =

- L’operatore = (assegnamento) deve essere sovraccaricato come membro
- Se non viene sovraccaricato, viene creato automaticamente
- L’operatore = di default copia i valori delle variabili membro di un oggetto nelle corrispondenti variabili membro di un altro oggetto
- Problemi nel caso ci siano puntatori: l’operatore = deve essere sovraccaricato!

---

title: Puntatore this

- Un oggetto ha accesso al proprio indirizzo mediante il puntatore this
- this non è parte dell’oggetto, piuttosto è passato come argomento implicito a tutte le funzioni membro dell’oggetto
- Tipo del puntatore this:
    - Funzione membro non costante: Employee* const
    - Funzione membro costante: const Employee* const

---

title: Auto-assegnamento

- Se si fornisce un operatore =…
    - Bisogna evitare auto-assegnamenti
    - Altrimenti c’è rischio di memory leak

        // Overloaded = operator; avoids self assignment
    - const String &String::operator=( const String &right )
        {
    - cout << "operator= called\n";
    - if ( &right != this ) { // avoid self assignment
    - delete [] sPtr; // prevents memory leak
    - length = right.length; // new String length
    - setString( right.sPtr ); // call utility function
        }
    - else
    - cout << "Attempted assignment of a String to itself\n";
    - return *this; // enables cascaded assignments
        }

---

title: Memory leak

- Un memory leak (falla nella memoria) è un particolare tipo di consumo non voluto di memoria
- Dovuto al mancato rilascio della memoria non più utilizzata da parte dei processi
    - Il termine non è etimologicamente corretto, visto che la memoria non viene persa fisicamente, piuttosto diventa inutilizzabile per un difetto del software

---

title: Operatori ++ e --

- Occorre un modo per distinguere la forma prefissa dalla forma postfissa
- La forma prefissa è sovraccaricata come qualsiasi altro operatore unario
- Nella forma postfissa si aggiunge un parametro fittizio di tipo int
    - Nella dichiarazione e nella definizione
    - Si tratta di un “dummy value” senza nessun altro scopo

---

title: Operatori ++ e --

- Operatori ++ e -- predefiniti ritornano…
    - Per riferimento nella forma prefissa
    - Per valore nella forma postfissa

        // Preincrement operator overloaded as a member function.
    - Date &Date::operator++()
        {
    - helpIncrement(); // The increment is in this utility function
    - return *this; // reference return to create an lvalue
        }
        // Postincrement operator overloaded as a member function. Note
        // that the dummy int parameter does not have a name.
    - Date Date::operator++( int )
        {
    - Date temp = *this;
    - helpIncrement(); // The increment is in this utility function
        // return non-incremented, saved, temporary object
    - return temp; // value return; not a reference return
        }

---

title: Operatore []

- L’operatore [] deve essere sovraccaricato come membro
- Se si vuole usare il valore ritornato come l-value deve ritornare una reference
- Il parametro indice può essere di qualsiasi tipo ed è l’argomento della chiamata alla funzione membro

---

title: Overloading: riassunto

- Almeno un operando deve essere di tipo classe
- Non si può:
    - Creare un nuovo operatore
    - Cambiare il numero di operandi di un operatore
    - Cambiare la precedenza di un operatore
    - Dare un argomento di default a un operatore sovraccaricato
- I seguenti operatori possono essere sovraccaricati solo come membri: =, [], ->, ()

---

title: Overloading: riassunto

- I seguenti operatori possono essere sovraccaricati solo come non membri o friend:
        <<, >>
- I seguenti operatori non possono essere sovraccaricati:
        . :: sizeof ?:
- Per alcuni operatori l’overloading è sconsigliato:
        && e || quando sovraccaricati effettuano la valutazione completa dell’espressione
        , quando sovraccaricato non garantisce l’ordine di valutazione da sinistra a destra


---


---

title: Suddivisione del Codice in File

- Separazione tra la classe e i programmi che la usano
    - Riuso: parti separate facilmente riusabili (libreria)
    - Compilazione selettiva
- Separazione tra interfaccia e implementazione
    - Incapsulamento: occultamento dei dettagli
    - Diverse implementazioni di una stessa libreria

---

title: Regole per Incapsulamento

- Rendere private tutte le variabili membro
- Raggruppare definizione della classe, dichiarazioni degli operatori e commenti nel file di interfaccia (header file)
- Raggruppare le definizioni delle funzioni membro, degli operatori e delle funzioni ausiliarie e l’inizializzazione delle variabili static nel file di implementazione

---

title: Compilazione Separata

- Il file che contiene il programma che usa la classe si chiama file di applicazione
- Sia l’implementazione che l’applicazione devono includere l’header file
- L’implementazione e l’applicazione vengono compilate separatamente
- Per ottenere l’eseguibile occorre linkare i due oggetti

---

title: Compilazione Separata (2)

- dtime.cpp

- dtime.o

- timedemo

- g++ -c dtime.cpp

- timedemo.cpp

- timedemo.o

- g++ -c timedemo.cpp

- g++ dtime.o timedemo.o –o timedemo

- sorgenti

- oggetti

- eseguibile

- dtime.h

---

title: Comando make

- Capisce quali moduli devono essere ricompilati e invia i comandi opportuni
- Utilizza un file chiamato makefile o Makefile che descrive le dipendenze e contiene i comandi per aggiornare i file
- Verifica il tempo di ultima modifica dei file per decidere quali richiedono aggiornamento

---

title: Makefile: Esempio

- timedemo: timedemo.o dtime.o
- g++ timedemo.o dtime.o -o timedemo
- timedemo.o: timedemo.cpp dtime.h
- g++ -c -W -Wall -pedantic timedemo.cpp
- dtime.o: dtime.cpp dtime.h
- g++ -c -W -Wall -pedantic dtime.cpp

---

title: Vantaggi della Compilazione Separata

- Separando l’interfaccia e l’implementazione della classe dall’applicazione
    - Posso riusare la classe in diversi programmi senza riscriverla
    - Posso compilare l’implementazione solo una volta
- Separando l’interfaccia dall’implementazione
    - Se cambio l’implementazione non devo cambiare i programmi che usano la classe
    - Devo solo ricompilare l’implementazione e rifare il link

---

title: Esempio: Inclusione Ripetuta

- classA.h
- class A
    {
- public:
    …
- private:
    …
    };

- implA.cpp

- implB.cpp

- classB.h
    #include “classA.h”
- class B
    {
- public:
    …
- private:
- A var;
    };

- Main.cpp
    #include “classA.h”
    #include “classB.h”
    …

---

title: Uso di #ifndef

- Un header file può includere altri header file
- Per evitare che il contenuto di un header file venga incluso più volte è necessario racchiudere il codice tra queste due sezioni:

code: c++

    #ifndef NOMEHEADER_H
    #define NOMEHEADER_H
code: c++

    #endif

- Come identificatore si usa il nome del file in maiuscolo e con l’underscore al posto del punto
- Convenzione usata in tutti gli header std (iostream, vector, string,…)

---

title: Esempio: Inclusione Ripetuta (2)

- classA.h

code: c++

    #ifndef CLASSA_H
    #define CLASSA_H

    class A
    {
        //…
    };
    #endif

- classB.h

code: c++

    #ifndef CLASSB_H
    #define CLASSB_H
    #include “classA.h”
    class B
    {
        //…
    };
    #endif

- implA.cpp
- implB.cpp

---

title: Namespace e Direttiva using

- Un namespace è un insieme di definizioni di nomi (classi, funzioni, …)
- Per creare un namespace

code: c++

    namespace Name_Space_Name
    { /* Some code */ }
- Per rendere disponibili tutti i nomi di un namespace si usa la direttiva using

code: c++

    using namespace Name_Space_Name;

- Lo scope della direttiva using va dal punto di occorrenza alla fine del file o del blocco
- Se il codice non è messo esplicitamente in un namespace è nel namespace globale (accessibile ovunque)

---

title: Dichiarazione using

- Per rendere disponibile un solo nome di un namespace uso la dichiarazione
    - using Name_Space_Name::One_Name;
- Utile con (molte) chiamate a pochi nomi Es: using std::cin; using std::cout; using std::string;

---

title: Differenze tra Direttiva e Dichiarazione

- La direttiva introduce tutti i nomi del namespace, la dichiarazione introduce un solo nome
- La direttiva introduce i nomi del namespace solo potenzialmente
    - Si possono avere sovrapposizioni potenziali
    - Non si possono avere sovrapposizioni esplicite

---

title: Qualificazione dei Nomi

- Se uso una definizione di un nome poche volte, posso qualificare il nome ogni volta che lo uso
    - esempio: std::cin
- Questa forma è usata spesso per specificare il tipo dei parametri
- Posso qualificare un nome rispetto a un namespace anche entro lo scope di una direttiva using per un altro namespace che definisce lo stesso nome
    - esempio: using namespace MySpace;
    - void someFunction(istream p1, std::istream p2);

---

title: Come Specificare il namespace?

- Evitare l’uso della direttiva using all’inizio del file perché vanifica il meccanismo dei namespace
- La maggior parte delle volte è preferibile l’uso della dichiarazione using
- Se il programma usa namespace diversi in punti diversi può essere opportuno inserire le direttive o dichiarazioni using in blocchi
- Negli header file usare la qualificazione dei nomi

---

title: Namespace senza Nome

- Una unità di compilazione è costituita da un file e dagli header file da esso inclusi
- Ogni unità di compilazione ha un namespace senza nome
    - namespace
        { … }
- I nomi definiti nel namespace senza nome sono locali all’unità di compilazione

---

title: Nascondere le Funzioni Ausiliarie

- Due modi:
    - Se la funzione accede ai dati dell’oggetto: funzione membro privata
    - Se la funzione non accede ai dati dell’oggetto: nel namespace senza nome del file di implementazione (oppure nel namespace della classe)


---


---

title: Variabili Dinamiche di Tipo Classe

- Quando si usa l’operatore new con un tipo classe viene chiamato il costruttore
    - Es: MyClass *classPtr;
    - classPtr = new MyClass;
    - classPtr = new MyClass(2, 45.3);
        …
    - delete classPtr;

---

title: Il Puntatore this

- this è un puntatore predefinito che punta all’oggetto chiamante
- Non si può cambiare il suo valore
- Non può essere usato nella definizione di una funzione membro static

---

title: Operatore = di Default

- Copia i valori dell’oggetto sorgente (r-value) nell’oggetto destinazione (l-value)
- Se la classe include una variabile membro di tipo puntatore, dopo l’assegnamento il puntatore dell’oggetto destinazione punta alla stessa area di memoria a cui punta il puntatore dell’oggetto sorgente
- L’area che era puntata dall’oggetto di destinazione non è probabilmente referenziata da nessun altro puntatore: memory leak
- Il primo dei due distruttori ad essere chiamato distrugge la memoria a cui puntano entrambi: dangling pointer

---

title: Shallow e Deep Copy

- La shallow copy (o “copia superficiale”) di A in B si realizza copiando byte a byte i valori presenti in A. In questo modo viene di fatto copiato il solo oggetto, ma non gli oggetti “figli” a cui il “padre” fa riferimento
- La deep copy si realizza invece copiando anche tutti gli oggetti “figli” facenti parte dell’oggetto “padre”

---

title: Overloading dell’Operatore =

- L’operatore = predefinito ritorna il suo operando sinistro per reference (permettendo così assegnamenti in cascata)
- Quando si ridefinisce l’operatore = per una classe si ritorna l’oggetto chiamante per reference (usando il puntatore this)
- Fare attenzione al caso dell’auto-assegnamento

---

title: Distruttore

- È una funzione membro che viene chiamata automaticamente quando termina lo scope di un oggetto
- Se una classe ha variabili membro dinamiche è bene che il distruttore le de-allochi
- Ha lo stesso nome della classe preceduto dal simbolo “~”, non ha parametri e non ha valore di ritorno
- Non ha argomenti e non può essere sovraccaricato
- Quando vengono chiamati più costruttori, i distruttori vengono chiamati in ordine inverso

---

title: Costruttore di Copia

- È un costruttore con un parametro dello stesso tipo della classe (const call-by-ref)
    - const: deve semplicemente essere costruita una copia)
    - by reference: altrimenti si creerebbe un ciclo ricorsivo di chiamate!
- Viene chiamato automaticamente quando
    - Un oggetto viene dichiarato e inizializzato con un altro oggetto dello stesso tipo
    - Una funzione ritorna un valore di tipo classe
    - Un oggetto viene passato per valore a una funzione

---

title: Costruttore di Copia di Default

- Se non viene definito viene creato automaticamente
- Il costruttore di copia di default fa una shallow copy
- Se la classe comprende puntatori e variabili dinamiche deve essere ri-definito

---

title: The Big Three

- Operatore =, distruttore e costruttore di copia vengono creati automaticamente dal compilatore
- Se la classe usa puntatori e variabili dinamiche devono essere ri-definiti: non farlo è un grave errore logico
- Di fatto sono legati dalle stesse problematiche relative all’uso di puntatori
    “If you need any of them, you need all three”

---


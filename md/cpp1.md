title: Linguaggio C++11
subtitle: Programmazione strutturata
figure: images/misc/cpp-logo.jpg

---

title: C++ Basics

- Elementi fondamentali
    - Variabili e costanti, espressioni, assegnamenti
- Istruzioni di controllo
    - Espressioni booleane, istruzioni di branching (if-else, switch), cicli (while, do-while, for)
- Funzioni e parametri
    - Call-by-value, call-by-reference
- Array e strutture
- Puntatori e allocazione dinamica

---

title: Funzione main()

- Punto di partenza del programma
- Lo standard ANSI/ISO C++
    - Impedisce la dichiarazione priva di tipo (int) della funzione main
    - Consente di omettere l’istruzione
    - return 0;
    - nella funzione main

---

title: Variabili

- Variabili
    - Convenzione sui nomi (camelCase)
    - Convenzione da usare per:
    -     variabili, parametri, funzioni, campi e metodi
    - Posizione della dichiarazione
- Costanti
    - Convenzione sui nomi (UPPER_CASE)
- Tipi e classi
    - Convenzione sui nomi (TitleCase)
- Suggerimento: mantenere nomi di variabili, costanti, ecc... in lingua inglese

- Variabili e Costanti

---

title: Namespace

- Insiemi di definizioni di nomi (classi, funzioni, …)
- Le librerie standard mettono i loro nomi nel namespace std
- Per usare queste definizioni occorre la direttiva
    - using namespace std;
- Per usare una specifica definizione
    - using std::cin;

---

title: Namespace (2)

code: c++

    #include <iostream>
    int main()
    {
        int integer1, integer2, sum; // declaration
        std::cout << "Enter first integer\n"; // prompt
        std::cin >> integer1; // read an integer
        std::cout << "Enter second integer\n"; // prompt
        std::cin >> integer2; // read an integer
        sum = integer1 + integer2; // assignment of sum
        std::cout << "Sum is " << sum << std::endl; // print sum
        return 0; // indicate that program ended successfully
    }

---

title: Namespace (3)

code: c++

    #include <iostream>
    using std::cout; // program uses cout
    using std::cin; // program uses cin
    using std::endl; // program uses endl

    int main()
    {
        int num1, num2;
        cout << "Enter two integers";
        cin >> num1 >> num2; // read two integers
        if (num1 == num2) }
            cout << num1 << " is equal to " << num2 << endl;
        }
        return 0; // indicate that program ended successfully
    }

---

title: Strutture di Controllo

- if/else
- while
- for
- do/while
- switch
- Programmazione ad oggetti: tende ad essere meno strutturata di quella procedurale

---

title: Funzioni

- Elementi costitutivi delle classi
    - Funzioni membro = metodi
- Caratterizzate da nome, parametri (numero, ordine e tipo) e tipo di ritorno
- Le funzioni hanno un prototipo
- Il prototipo non è necessario se la definizione della funzione appare prima del suo utilizzo
- Nel prototipo i parametri possono non avere nome, ma per chiarezza in genere lo si mette

---

title: Funzioni (2)

- La direttiva #include permette di importare i prototipi di funzioni delle librerie standard
- Ogni libreria standard ha un file header contenente la definizione di funzioni, tipi di dati e costanti
- Funzioni inline: viene generata una copia della funzione ogni volta che questa viene utilizzata
- Utile per funzioni brevi ed usate spesso (evita l’overhead del chiamare la funzione)

---

title: Funzioni (3)

code: c++

    #include <iostream>
    using std::cout;
    using std::endl;
    int cube(int y); // prototipo
    int main()
    {
        int x;
        for ( x = 1; x <= 10; x++ )
        cout << cube( x ) << endl;
        return 0;
    }
    int cube( int y )
    {
        return y * y * y;
    }

---

title: Parametri Call-by-value e Call-by-reference

- Call-by-value
    - L’argomento può essere una variabile o un’espressione
    - Il parametro formale viene inizializzato al valore dell’argomento
    - La funzione riceve una copia del valore dell’argomento
- Call-by-reference (“&” attaccato al tipo del parametro formale)
    - L’argomento deve essere una variabile
    - Il parametro formale viene sostituito con la variabile argomento
    - La funzione può cambiare la variabile argomento
    - Vantaggio: migliori prestazioni
    - Svantaggio: minore modularità, la funzione chiamata può corrompere i dati della chiamante

---

title: Parametri Call-by-value e Call-by-reference

- Oggetti di grandi dimensioni possono essere passati by reference, dichiarandoli però costanti
    - const int &x;
- Suggerimento
    - Parametri piccoli e non modificabili: call-by-value
    - Parametri modificabili: puntatori
    - Parametri grandi e non modificabili: reference a costante (oppure puntatore a costante)

---

title: Puntatori

- I puntatori contengono come valori indirizzi di memoria
- Quindi mentre una variabile contiene direttamente un valore, un puntatore lo contiene indirettamente: indirection
- L’operatore * (indirection operator) ritorna un sinonimo dell’oggetto a cui il suo operando (un puntatore) punta

---

title: Puntatori (2)

code: c++

    #include <iostream>
    using std::cout;
    using std::endl;

    int main()
    {
        int a; // a is an integer
        int *aPtr; // aPtr is a pointer to an integer
        a = 7;
        aPtr = &a; // aPtr set to address of a
        cout << "The address of a is " << &a << "\nThe value of aPtr is " << aPtr;
        cout << "\n\nThe value of a is " << a << "\nThe value of *aPtr is " << *aPtr;
        cout << "\n\nShowing that * and & are inverses of "<< "each other.\n&*aPtr = "
            << &*aPtr << "\n*&aPtr = " << *&aPtr << endl;
        return 0;
    }

---

title: Puntatori e Allocazione Dinamica

- L’operatore new crea una variabile dinamica e restituisce un puntatore ad essa
    - Esempio:
    - int *p;
    - p = new int;
- L’operatore delete distrugge la variabile e dealloca la memoria
    - Esempio:
    - delete p;

---

title: Arrays, Dynamic Arrays, Vectors

- Arrays: insiemi di dati dello stesso tipo, allocati staticamente
    - Esempio: `int a[10];`
- Dynamic arrays: la dimensione è determinata (e può variare) durante l’esecuzione
    - Esempio: `int *p = new int[10]; /*...*/ delete[] p;`
    - `delete[]` chiama prima il *distruttore* di ogni elemento
- Vector: una classe template della STL
    - Esempio: `vector<int> a;`

---

title: Parametri Array

- Se un parametro formale è di tipo array ([] dopo il nome del parametro) l’argomento passato è il nome di un array (senza [])
- La funzione può modificare gli elementi dell’array (di fatto viene passato un puntatore costante al primo elemento dell’array)
- Si deve passare alla funzione anche la dimensione dell’array

---

title: Il Modificatore di Parametro const

- Se inserito prima di un parametro il compilatore verifica che la funzione non lo modifichi
- Va usato sia nella definizione che nella dichiarazione (prototipo)
- Se un parametro const è passato a un’altra funzione, anche in essa deve essere const
- Il corretto utilizzo consente di assegnare ai metodi delle classi solo i privilegi effettivamente necessari, rispettando i concetti della programmazione object oriented e facilitando il debug

---

title: Il Modificatore di Parametro const

code: c++

    // Printing a string one character at a time using a non-constant pointer to constant data
    #include <iostream>
    using std::cout;
    using std::endl;
    void printCharacters( const char * );
    int main()
    {
        char string[] = "print characters of a string";
        cout << "The string is:\n";
        printCharacters( string );
        return 0;
    }
    // sPtr cannot modify the character to which it points. sPtr is a "read-only" pointer
    void printCharacters( const char *sPtr )
    {
        for ( ; *sPtr != '\0'; sPtr++ ) { // no initialization
            cout << *sPtr;
        }
    }

---

title: Casting

- In generale pericoloso, sorgente di errori a run time
- Quattro nuovi costrutti di casting: più specifici, meno potenti (è un bene!)
    - `static_cast<tipo>(expr)` : conversione tra tipi
    - `const_cast<tipo>(expr)` : attributo const (on/off)
    - `dynamic_cast<tipo>(espressione)` : gerarchie di classi
    - `reinterpret_cast<tipo>(expr)` : puntatori, int

---

title: Overloading

- C++ consente di avere più funzioni con definizioni diverse e lo stesso nome
- Devono differire per il numero di parametri e/o il tipo di almeno un parametro (signature)
- Non possono differire solo per
    - Valore ritornato
    - Modificatore const
    - Call-by-value vs. call-by-reference
- Funzionalità importante della programmazione ad oggetti: è corretto che se una stessa operazione può essere applicata a tipi di dati differenti, il nome dell’operazione non cambi

---

title: Overloading (3)

- Signature di una funzione
    - Nome più lista dei tipi dei parametri
    - Deve essere unica per ogni definizione di funzione
- Il compilatore risolve la chiamata di funzione in base alla signature
- E’ possibile effettuare l’overloading non solo delle funzioni, ma anche degli operatori

---

title: Regole per Risolvere l’Overloading

- Il compilatore cerca, nell’ordine:
    - Match esatto
    - Match con promozione tra tipi interi o tra tipi floating-point
    - Match con altra conversione tra tipi predefiniti
    - Match con conversione tra tipi definiti dall’utente
- Se in uno dei tentativi trova più match, dà errore

---

title: Esempio

code: c++

    #include <iostream>
    using std::cout;
    using std::endl;
    int square( int x ) { return x * x; }
    double square( double y ) { return y * y; }
    int main()
    {
        cout << "The square of integer 7 is " << square( 7 )
        << "\nThe square of double 7.5 is " << square( 7.5 )
        << endl;
        return 0;
    }

---

title: Argomenti di Default

- Per i parametri call-by-value si può specificare un valore di default
- Se il corrispondente argomento manca, il parametro assume il valore di default
- Il valore di default va inserito nella prima tra dichiarazione e definizione
- I parametri con valore di default devono stare nelle posizioni più a destra
- Nella chiamata gli argomenti vanno omessi a partire da destra

---

title: Overloading e Argomenti di Default

- Entrambi consentono di invocare un nome di funzione in più modi
- Gli argomenti di default vanno usati quando:
    - Esiste un valore di default sensato (es.: se il valore fosse nullo, meglio l’overloading)
    - La funzione usa lo stesso algoritmo indipendentemente dal numero di argomenti nella chiamata
- Attenzione: l’overload unito all’uso di argomenti di default può portare a codice di difficile comprensione

---

title: Rappresentazione delle Stringhe

- C++ offre due modi per rappresentare le stringhe di caratteri
    - Il modo ereditato dal linguaggio C (C-strings)
    - Oggetti della classe string (presente nella libreria standard)

---

title: C-strings

- Array di char terminati col carattere ‘\0’
    - Es: char message[10] = “Ciao”; char shortString[] = “abc”; char arrayOfChar[] = {‘a’,‘b’,‘c’}; char s[10];
- I valori di tipo stringa (es. “Hello”) sono implementati come C-string

---

title: Libreria cstring

- Le C-strings non consentono l’uso degli operatori = e ==
- La libreria cstring contiene funzioni per la manipolazione delle C-strings (definizioni nel namespace globale)
    - Es. strcpy, strcmp, strcat, strlen
- Lo standard C++ ha aggiunto versioni safe di queste funzioni
    - Es. strncpy, strncmp, strncat, strnlen

---

title: I/O di C-strings

- L’operatore << consente di inserire il valore di una C-string in un output stream
    - Es: char message[] = “Hello”; cout << message;
- L’operatore >> consente di estrarre una stringa da un input stream
    - Ignora eventuali caratteri di spaziatura iniziali, la lettura si ferma al primo carattere di spaziatura
    - Es: char a[80], b[80]; cin >> a >> b;
    - Lettura di un’intera linea di input con la funzione membro della classe istream: getline(cstringVar, maxCar+1)
    - Es: cin.getline(a, 80);

---

title: La Classe Standard string

- Con le C-strings ci si deve occupare dei dettagli di implementazione
- La classe string consente di trattare le stringhe di caratteri come un tipo base
    - Con l’operatore = si può assegnare un valore a una variabile string
    - Con l’operatore + si possono concatenare due stringhe
- Classe string: definita nella libreria string, definizioni nel namespace std

---

title: Conversione tra C-strings e Oggetti string

- Le C-strings sono convertite automaticamente in oggetti string
    - Inizializzazione di un oggetto string con una C-string
    - Assegnamento di una C-string ad un oggetto string
    - Concatenazione di oggetti string e C-strings
- Non c’è conversione automatica di oggetti string in C-strings
    - Funzione membro c_str()

---

title: I/O di Oggetti string

- L’operatore << (insertion) consente di inserire un oggetto string in un output stream
    - Es: string message(“Hello”); cout << message;
- L’operatore >> (extraction) consente di estrarre un oggetto string da un input stream
    - Ignora eventuali caratteri di spaziatura iniziali, la lettura si ferma al primo carattere di spaziatura
    - Es: string s1, s2; cin >> s1 >> s2;
    - Lettura di un’intera linea di input con la funzione getline(aStream, aString) definita nella libreria string

---

title: Altre Funzionalità

- Sono fornite funzioni di utilità per:
    - Comparazione
    - Manipolazione
    - Estrazione di sottostringhe
    - Rimpiazzo o inserimento di caratteri
    - Iterazione tra gli elementi
    - ...

---

title: La classe vector

- I vettori sono array la cui dimensione può cambiare durante l’esecuzione
- Sono oggetti della classe vector, una classe template della Standard Template Library (STL)
    - Ex: vector<int> v;
- La classe è definita nella libreria vector all’interno del namespace std
    - Ex: #include <vector> using namespace std;

---

title: La notazione []

- La notazione []
    - può essere usata per
        - leggere un elemento
        - cambiare un elemento che ha già un valore
    - non può essere usata per
        - inizializzare un elemento
    - non controlla se l’elemento esiste
- Per aggiungere elementi (in ordine di posizione) si usa il metodo push_back()
- Accesso agli elementi di un vector

---

title: Costruttore con un argomento intero

- Crea un numero di elementi pari all’argomento e li inizializza…
    - Con lo zero del tipo numerico se è un vettore di numeri
    - Con il costruttore di default se il tipo base è un tipo classe
    - Ex: `vector<int> v(10); vector<DayOfYear> days(3);`

---

title: Dimensioni e capacità

- La dimensione è il numero di elementi in un vector (restituita dal metodo `size()`)
- La capacità è il numero di elementi per i quali c’è memoria allocata
- Se aggiungo elementi a un vector che ha esaurito la capacità, questa viene automaticamente aumentata
- Posso ignorare la gestione della capacità se non serve efficienza
- Altrimenti posso usare il metodo `reserve()` per riservare una capacità minima
- Il metodo `resize()` modifica la dimensione del vector



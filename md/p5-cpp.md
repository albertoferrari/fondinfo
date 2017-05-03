title: Linguaggio C++11
subtitle: Introduzione alla programmazione
figure: images/misc/cpp-logo.jpg

---

title: Hello, C++

- `cout`: output su console, op. di inserimento `<<`
    - Possibile concatenare più operazioni di scrittura

code: c++

    #include <iostream>
    using namespace std;

    int main() {
        cout << "Hello, C++!" << endl;
    }

- Da *Qt Creator* (ambiente di sviluppo): *Create Project →  Non-Qt →  Plain C++*
- **C++11**: aggiungere al file `.pro` (di progetto): `CONFIG += c++11`

---

title: Leggere e scrivere

- `cin`: input da console, op. di estrazione `>>`
    - Possibile concatenare più operazioni di lettura
    - `getline(cin, line)`: lettura intera riga

code: c++

    #include <iostream>
    using namespace std;

    int main() {
        string name;
        int age;
        cout << "Name, age?" << endl;
        cin >> name >> age;
        cout << "Hello, " << name << "." << endl;
        cout << "You're " << age << " years old." << endl;
    }

---

title: Tipizzazione statica
figure: images/algo/my-shoes.png

- Una delle differenze principali: le comuni variabili non sono *riferimenti*, ma *contenitori* di dati
    - Occorrono **dichiarazioni** di tipo
    - Ma possibile *type inference* (`auto`)
- Tipi principali: `int`, `float` (e `double`), `bool`
- `string`: sequenza mutevole di byte (tipo `char`)

code: c++

    int x = 10;
    double h = 3.7;
    string s = "hello";
    
    auto y = 5;               // type inference: C++11
    auto k = 2.2;
    auto t = string{"hola"};  // C++14: auto t = "hola"s;

---

title: Operazioni di base

- Operazioni su numeri: `+, -, *, /, %`
    - Anche incremento e decremento unitario: `++, --`
    - *Attenzione*: la divisione tra interi dà risultato intero (`trunc`); il resto può essere negativo
    - Assegnamento: `=, +=, -=` ...
    - Confronti: `>, >=, <, <=, !=, ==`
    - *Attenzione*: i confronti **non** si possono concatenare
- Operazioni booleane (and, or, not): `&&, ||, !`

code: c++

    cout << (3 < 5) << endl;           // 1
    cout << (3 < 5 < 4) << endl;       // 1 (!)
    cout << (3 < 5 && 5 < 4) << endl;  // 0

---

title: Stringhe

- Operazioni di confronto; concatenazione: `+`
- *Attenzione*: apici doppi per valori `string`, singoli per `char`

code: c++

    string sentence = "Lorem ipsum";
    sentence[6] = 'I';
    cout << sentence[6];  // 'I'

    int n = 5;
    string txt = to_string(n);
    int val = stoi(txt);  // see also `stod`, `stof`...

---

title: Decisioni
figure: images/algo/words.svg

code: c++

    string a, b; cin >> a >> b;
    if (a < b) {
        cout << "The words are ordered";
    } else if (a > b) {
        cout << "The words are inverted";
    } else {
        cout << "The words are equal";
    }

code: c++

    int choice; cin >> choice;
    switch (choice) {
        case 1: cout << "First option"; break;
        case 2: cout << "Second option"; break;
        default: cout << "Error";
    }

---

title: Iterazioni
figure: images/algo/average.svg

code: c++

    int val, tot = 0, count = 0;
    cout << "Val (0 to end)? "; cin >> val;
    while (val != 0) {
        tot += val; ++count;
        cout << "Val (0 to end)? "; cin >> val;
    }
    if (count > 0) cout << "Avg: " << tot / float(count);

code: c++

    int val, tot = 0, count = 0;
    do {
        cout << "Val (0 to end)? "; cin >> val;
        if (val != 0) { tot += val; ++count; }
    } while (val != 0);  // the check is at the end
    if (count > 0) cout << "Avg: " << tot / float(count);

---

title: Vector, array dinamici
figure: images/fun/shopping-list.jpg

code: c++

    #include <vector>
    // ...

    vector<string> shopping_list = {"milk", "cocoa",
                                    "yogurt"};
    cout << shopping_list[1] << endl;  // cocoa
    shopping_list[1] = "coffee";
    shopping_list.push_back("corn flakes");
    cout << shopping_list.size() << endl;  // 4

    shopping_list.erase(begin(shopping_list) + 2);
    shopping_list.insert(begin(shopping_list) + 2, "biscuits");

    vector<string> another_list;
    another_list.assign(10, ""); // 10 strings

---

title: Cicli for

code: c++

    // for-each, C++11
    for (auto x : shopping_list) {
        cout << x << endl;
    }

    // range, C++98
    for (int i = 0; i < shopping_list.size(); ++i) {
        cout << shopping_list[i] << endl;
    }

    // equivalent while
    int i = 0;
    while (i < shopping_list.size()) {
        cout << shopping_list[i] << endl;
        ++i;
    }

---

title: Somma colonne: matrice

code: c++

    vector<vector<int>> matrix = {{2, 4, 3, 8},
                                  {9, 3, 2, 7},
                                  {5, 6, 9, 1}};
    auto rows = matrix.size();
    auto cols = matrix[0].size();
    for (auto x = 0; x < cols; ++x) {
        auto total = 0;
        for (auto y = 0; y < rows; ++y) {
            total += matrix[y][x];
        }
        cout << "Col #" << x << " sums to " << total << endl;
    }

code: c++

    vector<vector<char>> another_matrix;
    another_matrix.assign(rows, vector<char>(cols, '-'));

---

title: Funzioni

code: c++

    #include <cmath>
    #include <iostream>
    using namespace std;

    double hypotenuse(double a, double b) {
        auto c = sqrt(a * a + b * b);
        return c;
    }

    int main() {
        auto side1 = 3.0, side2 = 4.0;
        auto side3 = hypotenuse(side1, side2);
        cout << "3rd side: " << side3 << endl;
    }

---

title: Parametri per riferimento

- Parametri passati per riferimento sono *alias*
    - Le modifiche riguardano anche le variabili esterne
    - Limitarne l'uso!

code: c++

    // pass by reference: external vars can be modified
    void swap(int& m, int& n) {
        int tmp = m;
        m = n; n = tmp;
    }

    int main() {
        int a = 5, b = 7;
        swap(a, b);
        cout << a << " " << b << endl;
    }

---

title: Flussi e file

code: c++

    #include <fstream>
    // ...

    int n; float r; string w;
    ifstream file1{"input.txt"};   // file input stream
    if (file1.good()) {            // is stream available?
        file1 >> n >> r >> w;
    }
    file1.close();

    ofstream file2{"output.txt"};  // file output stream
    if (file2.good()) {            // is stream available?
        file2 << "Values: " << n << " " << r << " " << w << endl;
    }
    file2.close();

---

title: Lettura di righe

code: c++

    ifstream file1{"input.txt"};

code: c++

    string first_line, second_line;
    getline(file1, first_line);
    getline(file1, second_line);
    // first_line and second_line do not include newlines

code: c++

    string whole_text;
    getline(file1, whole_text, '\0');
    // read the whole file, including newlines

code: c++

    string line;
    while (getline(file1, line)) {  // for each line in file1...
        cout << line << endl;
    }


---

title: Lettura di dati

code: c++

    int val;  // or float, string ...
    while (file1 >> val) {
        cout << setw(4) << val << endl;  // val occupies 4 chars
    }                                    // setw in <iomanip>

code: c++

    char val;
    file1 >> noskipws;      // otherwise, whitespaces are skipped
    while (file1 >> val) {
        cout << val << endl;
    }

code: c++

    int n; float r; string w;
    istringstream sstr{"5 7.5 hello"};  // istringstream in <sstream>
    sstr >> n >> r >> w;                // a stream view on a string

---

title: Flussi e stringhe

- Si può gestire una stringa come uno stream
    - `istringstream`, `ostringstream` in libreria `<sstream>`
    - Per estrarre valori ed inserire valori, rispettivamente

code: c++

    /* Split a text into a vector of strings */
    string text = "one:two::three";
    vector<string> values;

    istringstream sstr{text};
    string item;
    while (getline(sstr, item, ':')) {
        values.push_back(item);
    }

---

title: Numeri casuali

code: C++

    #include <iostream>
    #include <cstdlib>
    #include <ctime>
    using namespace std;

    int main() {
        srand(time(nullptr));           // just once! (initial seed
                                        // for random numbers)

        for (int i = 0; i < 10; ++i) {  // generate 10 random numbers
            int r = rand() % 90;  // 0 <= r < 90
            cout << r << endl;
        }
    }

>

C++11 ha anche una libreria `random`, più avanzata <br>
<http://www.stroustrup.com/C++11FAQ.html#std-random>

---

title:  Rettangoli e cerchi con Qt
figure: images/qt/slogan.png images/oop/raster-coord.png

code: C++

    #include <QtWidgets>

code: C++

    QPixmap screen{600, 400}; QPainter painter{&screen};

    painter.setBrush(QColor{255, 255, 0});
    painter.drawRect(50, 75, 90, 50);

    painter.setBrush(QColor{0, 0, 255});
    painter.drawEllipse(QPoint{300, 50}, 20, 20);
    
    QLabel label; label.setPixmap(screen); label.show();

code: Project

    QT += widgets
    CONFIG += console c++11

>

Progetto: *Application* → *Qt Widgets Application*

---

title: Oggetti
class: segue dark

---

title: Oggetti

- C++: definizione della classe separata dalla implementazione dei metodi
    - Definizione fornita agli utenti
    - Implementazione compilata in libreria
- Sorgenti organizzati in 3 file:
    - `ball.h` – definizione della classe
    - `ball.cpp` – implementazione dei metodi
    - `main.cpp` – applicazione che usa la classe
    - Dall'ambiente di sviluppo: *Add new → C++ Class*

---

title: Definizione: ball.h
figure: images/oop/ball-object.svg

code: c++

    class Ball {
    public:
        Ball(int x0, int y0);
        void move();
        int get_x();
        int get_y();

        static const int ARENA_W = 320;
        static const int ARENA_H = 240;
        static const int W = 20;
        static const int H = 20;

    private:
        int x; int y;
        int dx; int dy;
    };

---

title: Implementazione: ball.cpp

code: c++

    #include "ball.h"

    Ball::Ball(int x0, int y0) {
        x = x0; y = y0; dx = 5; dy = 5;
    }
    void Ball::move() {
        if (!(0 <= x + dx && x + dx <= ARENA_W - W)) dx = -dx;
        if (!(0 <= y + dy && y + dy <= ARENA_H - H)) dy = -dy;
        x += dx; y += dy;
    }
    int Ball::get_x() {
        return x;
    }
    int Ball::get_y() {
        return y;
    }

---

title: Applicazione: main.cpp

code: c++

    #include "ball.h"
    // ...
    int main() {
        Ball ball1{40, 80};
        Ball ball2{80, 40};

        string line;
        while (getline(cin, line)) {
            ball1.move();
            ball2.move();

            cout << ball1.get_x() << ", " << ball1.get_y() << endl;
            cout << ball2.get_x() << ", " << ball2.get_y() << endl << endl;
        }
    }

---

title: Allocazione dinamica

code: c++

    // ...
    int main() {
        Ball ball1{40, 80};
        Ball* ball2 = new Ball{80, 40};
        // Ball* alias1 = &ball1; // no new ball is created
        // Ball* alias2 = ball2;  // no new ball is created

        for (string line; getline(cin, line);) {
            ball1.move();
            ball2->move();
            cout << ball1.get_x() << ", " << ball1.get_y() << endl;
            cout << ball2->get_x() << ", " << ball2->get_y() << endl << endl;
        }
        delete ball2;
    }

---

title: Swig: C++ per moduli Python

code: file: ball.i

    %module ball
    %include "std_string.i"
    %{
    #include "ball.h"
    %}
    %include "ball.h"

code: cmd

    swig -python -c++ ball.i
    g++ -fPIC -c ball.cpp ball_wrap.cxx -I/usr/include/python3.4/ -std=c++11
    g++ -shared ball.o ball_wrap.o -o _ball.so

code: python

    >>> from ball import Ball
    >>> b = Ball(60, 60)
    >>> b.move()
    >>> print(b.get_x(), b.get_y())

---

title: Puntatori
figure: images/oop/pointer.png

- Ogni dato presente in memoria ha un indirizzo: variabile puntatore per memorizzarlo
    - Operatore `&` per indirizzo di un dato
    - Op. `*` per accesso a dato puntato (*dereferenziazione*)

code: c++

    char i = 56;  // a byte
    char* p;      // a ptr to some byte (uninitialized)
    p = &i;       // now p points to i
    *p = *p + 1;  // ++i
    p = nullptr;  // ptr to nothing

- No *garbage collection*: a `new` deve corrispondere `delete`
- *Resource Acquisition Is Initialization (RAII)*
    - *Costruttore* alloca risorse, *distruttore* le libera: `~Ball()`

---

title: Livelli di astrazione
class: segue dark

---

title: Livelli di astrazione
figure: images/oop/actors.svg

- `Actor`: *classe base*
    - Dichiara un metodo `move` ecc.
    - `virtual`: il metodo può essere ridefinito nelle sottoclassi (*polimorfo*)
    - `= 0`: il metodo non è implementato qui (la classe è *astratta*)

code: c++

    class Actor {
        virtual void move() = 0;
        // ...
    };

---

title: Composizione

code: c++

    class Arena {  // ...
    public:
        void add(Actor* a);
        void move_all();
    private:
        vector<Actor*> actors;
    };

code: c++

    void Arena::add(Actor* c) {
        actors.push_back(a);
    }
    void Arena::move_all() {
        for (auto a : actors) a->move();
    }

---

title: Ereditarietà e polimorfismo

code: c++

    arena->add(new Ball(4, 8));
    arena->add(new Ghost(12,4));
    arena->move_all();

code: c++

    class Ghost: public Actor {
        // ...
        Ghost() { /* ... */ }
        
        void move() {
            vector<int> vals = {-5, 0, 5};
            int dx = vals[rand() % 3];  // one of {-5, 0, +5}
            int dy = vals[rand() % 3];
            x = (x + dx + arena->get_w()) % arena->get_w();
            y = (y + dy + arena->get_h()) % arena->get_h();
        }
    };

---

title: Ciclo di animazione in Qt

code: C++

    // fields: int x = 0; QPixmap image{"ball.png"};

    Widget::Widget() {
        startTimer(1000 / 60);  // 60 fps
    }
    void Widget::timerEvent(QTimerEvent* event) {
        x = (x + 5) % 600;  // or width()
        update();           // async: this widget should be redrawn
    }
    void Widget::paintEvent(QPaintEvent* event) {
        QPainter painter{this};
        painter.drawPixmap(x, 10, image);
    }

>

Progetto: *Application* → *Qt Widgets Application*

---

title: Fifteen – Gioco astratto
figure: images/qt/fifteen-puzzle.jpg

code: C++

    class Game {
    public:
        virtual void play_at(int x, int y) = 0;
        virtual int cols() = 0;
        virtual int rows() = 0;
        virtual std::string get_val(int x, int y) = 0;
        virtual bool finished() = 0;
        virtual std::string message() = 0;
    };

---

title: Fifteen – Gui generica
figure: images/qt/puzzle.png

code: C++

    class GameGui : public QWidget {
        Q_OBJECT
    public:
        GameGui(Game* game);
        void handle_click(int x, int y);
        void update_button(int x, int y);
        void update_all_buttons();
    private:
        Game* game_;
        int cols_, rows_;
    };

---

title: Strutture dati lineari
class: segue dark

---

title: Vector, array dinamici
figure: images/fun/dynamic-array.svg
class: large-figure

- **Array**: area di memoria che contiene in *celle contigue* elementi tutti dello *stesso tipo*
- Usato internamente dai `vector` del C++
    - Riallocazione dinamica e trasparente per inserimenti e rimozioni
- `Vector` come **array dinamici**
    - Accesso casuale: `O(1)`
    - Aggiunta o rimozione in fondo all'array: `O(1)`, ma a volte riallocazione
    - Inserimento o rimozione: `O(n)`

---

title: Vector di float

code: C++

    class FloatVector {  // ...
        int capacity_;
        int size_;
        float* data_;
    public:
        FloatVector(int size, float val);
        float get(int pos);
        void set(int pos, float val);
        void insert(int pos, float val);
        float remove(int pos);
        int size();
    };

Implementazione nel repository di esempi

---

title: Inserimento in vector

code: C++

    void FloatVector::insert(int pos, float val) {
        if (pos < 0 || pos > size_) throw out_of_range("wrong pos");
        if (size_ == capacity_) expand_capacity();
        for (int i = size_; i > pos; --i) data_[i] = data_[i - 1];
        data_[pos] = val;
        ++size_;
    }
    void FloatVector::expand_capacity() {
        capacity_ *= 2;
        float* bigger = new float[capacity_];
        for (int i = 0; i < size_; i++) bigger[i] = data_[i];
        delete[] data_;
        data_ = bigger;
    }

---

title: Liste concatenate

![](images/fun/linked-list.svg)

- Ciascun **nodo** contiene un *valore* della lista ed un *puntatore* al nodo successivo
    - Accesso casuale: `O(n)`
    - Aggiunta o rimozione in testa all'array: `O(1)`
    - Aggiunta o rimozione in fondo all'array: `O(n)`, oppure `O(1)` se noto ultimo nodo
    - Inserimento o rimozione: `O(1) + O(n)` per ricerca

---

title: Lista di float

code: C++

    struct Node {
        float val;
        Node* next;
    };
    class FloatList {  // ...
        Node* head_; int size_;
    public:
        FloatList(int size, float val);
        float get(int pos);
        void set(int pos, float val);
        void insert(int pos, float val);
        float remove(int pos);
        int size();
    };

Implementazione nel repository di esempi

---

title: Inserimento in lista

code: C++

    void FloatList::insert(int pos, float val) {
        if (pos < 0 || pos > size_) throw out_of_range("wrong pos");
        if (pos == 0) {
            head_ = new Node{val, head_};
        } else {
            Node* n = head_;
            for (int i = 0; i < pos - 1; ++i) n = n->next;
            n->next = new Node{val, n->next};
        }
        ++size_;
    }

---

title: Template C++

- **Programmazione generica**: codice che opera su *tipi parametrizzati*
    - Es. liste di `int`, `string` ecc.: cambia solo il tipo di dato!
- **Template**: meccanismo di programmazione generica in C++
    - Generaz. trasparente di codice specializzato per un tipo
    - Es. `vector<float>` genera una classe ≈ `FloatVector`

code: C++

    template <class T>
    T max(T a, T b) {
        if (a >= b) return a;
        return b;
    }

code: C++

    double x = max<double>(5.0, 3.5);  # <double>, <int>: optional
    int i = max<int>(4, 6);            # inferred from parameters


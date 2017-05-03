title: Gui con Qt
subtitle: Introduzione alla programmazione
figure: images/qt/slogan.png

---

title: Caratteristiche di Qt

- **Sviluppo con meno codice**
    - *Design OO*: classi intuitive, riusabili ed estendibili
    - Sviluppo *visuale* o *dichiarativo* di gui
    - Personalizzazione aspetto delle app con *CSS*
- **Sviluppo libero e multipiattaforma**
    - *Qt Project*: codice open source (Nokia → Digia)
    - *Qt Creator*: ambiente integrato di sviluppo
- **App portabili e avanzate**: buone prestazioni con poche risorse
    - Sistemi desktop: Windows, MacOS, Linux …
    - Mobile/embedded: Android, iOS, Symbian, BlackBerry QNX, MeeGo-JollaOS, Tizen, Ubuntu Touch, Raspberry Pi …
    - KDE, KOffice, VLC, Google Earth, Skype (Linux), Mathematica…

---

title: Libreria modulare

- Qt Core: classi base, stringhe ecc.
- **Qt GUI**: supporto grafica 2D
    - Integraz. OpenGL, anti-aliasing, trasparenza, trasformaz. vettoriali
- **Qt Widgets**: insieme di *widget* evoluti
    - Usabilità, esperienza più soddisfacente per utente
- Qt Multimedia, Qt Multimedia Widgets
- Qt Network
- Qt QML, Qt Quick, Qt Quick Controls, Qt Quick Layouts
- Qt SQL
- Qt Test
- Qt WebKit, Qt WebKit Widgets

---

title: Bottoni e display

![](images/qt/buttons.jpg)

![](images/qt/displays.jpg)

---

title: Input
figure: images/qt/calendar-example.png
figcaption: Esempio, con QCalendarWidget

![](images/qt/inputs.jpg)

---

title: Viste di elementi

![](images/qt/views.jpg)

---

title: Contenitori

![](images/qt/single-page-containers.jpg)

![](images/qt/multi-page-containers.jpg)

>

Inoltre: QMenu, QMenuBar, QToolBar, QStatusBar

---

title: Finestre di dialogo

![](images/qt/feedback-dialogs.jpg)

---

title: File e stampa

![](images/qt/file-print-dialogs.jpg)

---

title: Colori e font

![](images/qt/color-font-dialogs.jpg)

---

title: Stili

- Qt sfrutta le primitive grafiche della piattaforma
    - Efficienza, aspetto familiare
    - Ma possibile stile personalizzato!
    - `QApplication::setStyle(new QWindowsStyle);`
    - `QApplication::setStyleSheet`
    - `QWidget::setStyleSheet`

![](images/qt/styles.png)

---

title: Disposizione dei widget
class: segue dark

---

title: Visualizzare un widget
figure: images/qt/notepad-1.png

code: C++

    #include <QApplication>
    #include <QTextEdit>

    int main(int argc, char* argv[]) {
        QApplication app{argc, argv};

        QTextEdit text_edit;
        text_edit.show();

        return app.exec();  // event management
    }

---

title: Creare un nuovo widget

- Estendere **`QWidget`**, o una sua sottoclasse
    - Creare nuovi campi e metodi, sovrascrivere metodi *virtual*
    - Altrimenti, **ereditate** le caratteristiche della classe base
- Incapsulare parti dell'interfaccia utente
    - Nuovo widget: **composto** da widget elementari
    - Resto dell'applicazione non ha bisogno di conoscere i dettagli
- Nuovo widget riusabile
    - Nella stessa applicazione o in altri progetti

---

title: Sottoclasse di QWidget
figure: images/qt/notepad-2.png

code: C++

    class Notepad : public QWidget {
    public:
        Notepad();

    private:
        QTextEdit* text_edit;      // simple widgets:
        QPushButton* exit_button;  // encapsulated as private fields
    };

- Da *Qt Creator*:
    - *Create Project →  Applications →  Qt Gui Application*
    - *Base class*: `QWidget` -- *Generate form*: `no`
- **C++11**: aggiungere al file `.pro` (di progetto): `CONFIG += C++11`

---

title: Costruire la GUI
figure: images/qt/notepad-2.png

code: C++

    Notepad::Notepad() {
        // construtor: build the GUI
        // QObject::tr translates GUI texts (see Qt Linguist)

        text_edit = new QTextEdit;
        exit_button = new QPushButton{tr("Quit")};

        // widgets in a vertical layout
        auto layout = new QVBoxLayout;
        layout->addWidget(text_edit);
        layout->addWidget(exit_button);

        setLayout(layout); // QWidget
    }

---

title: Layout principali

- Qt usa il meccanismo dei *layout* per disporre i widget
- Ci sono tre classi di layout pricipali
    - `QHBoxLayout`
    - `QVBoxLayout`
    - `QGridLayout`
- Per installare un layout su un widget, dobbiamo invocare il metodo `setLayout` del widget
- Il layout gestisce l'area *interna* al widget

---

title: Layout compositi
figure: images/qt/notepad-layout.png images/qt/notepad-nostretch.png
figcaption: With and without <code>addStretch()</code>

- È possibile inserire un layout dentro un altro
- Es. Layout aggiuntivo a destra, con bottoni in verticale

code: C++

    // ctor
    auto button_layout = new QVBoxLayout;
    button_layout->addWidget(open_button);
    button_layout->addWidget(save_button);
    button_layout->addWidget(exit_button);
    button_layout->addStretch();

    auto main_layout = new QHBoxLayout;
    main_layout->addWidget(text_edit);
    main_layout->addLayout(button_layout);
    setLayout(main_layout);

---

title: Click dei bottoni
class: segue dark

---

title: Definire gli slot

code: C++

    class Notepad : public QWidget {
        // add support for signals and slots...
        Q_OBJECT
    public:
        Notepad();
        // slots, to connect with signals
        void open();
        void save();
        void exit();
    private:
        QTextEdit* text_edit = new QTextEdit;
        QPushButton* open_button = new QPushButton{tr("&Open")};
        QPushButton* save_button = new QPushButton{tr("&Save")};
        QPushButton* exit_button = new QPushButton{tr("E&xit")};
    };

---

title: Connettere segnali e slot

code: C++

    Notepad::Notepad() {
        // ... at the end of ctor ...
        connect(open_button, &QPushButton::clicked, this, &Notepad::open);
        connect(save_button, &QPushButton::clicked, this, &Notepad::save);
        connect(exit_button, &QPushButton::clicked, this, &Notepad::exit);
    }

![](images/qt/notepad-connections.svg)

---

title: Accoppiamento tra segnali e slot
figure: images/qt/abstract-connections.png

- **Accoppiamento lasco**
    - Un oggetto emette un *segnale*, ma non sa quali *slot* lo ricevono
    - Molti segnali ad un singolo slot, un segnale a molti slot
- **Type safe**
    - La *firma* del segnale (numero e tipo di parametri) deve corrispondere a quella degli  slot collegati
    - Se la firma di uno slot è più corta, trascura degli argomenti che riceve
    - Compilatore rileva errori
- **Estensione alla sintassi C++**
    - Segnali e slot sono una estensione specifica di Qt alla sintassi del C++

---

title: Aprire un file

code: C++

    void Notepad::open() {
        // choose the input file
        auto filename = QFileDialog::getOpenFileName(this);
        if (filename != "") {
            ifstream in{filename.toStdString()};
            if (in.good()) {
                // read the whole text
                string content; getline(in, content, '\0');
                text_edit->setText(content.c_str());
            } else {
                QMessageBox::critical(this, tr("Error"),
                                      tr("Could not open file"));
            }
        }
    }

---

title: Salvare in un file

code: C++

    void Notepad::save() {
        // choose the output file
        auto filename = QFileDialog::getSaveFileName(this);
        if (filename != "") {
            ofstream out{filename.toStdString()};
            if (out.good()) {
                // write the whole text
                auto text = text_edit->toPlainText();
                out << text.toStdString();
            } else {
                QMessageBox::critical(this, tr("Error"),
                                      tr("Could not save file"));
            }
        }
    }

---

title: Chiudere l'app

code: C++

    void Notepad::exit() {
        auto button = QMessageBox::question(
            this,
            tr("Notepad - Quit"),
            tr("Do you really want to quit?"),
            QMessageBox::Yes | QMessageBox::No);

        if (button == QMessageBox::Yes) {
            window()->close();
        }
    }

    // See documentation (F1): QMessageBox, QInputDialog, QDialog

---

title: Finestra principale
figure: images/qt/mainwindow.png

- `QMainWindow`: widget complesso, con un proprio layout particolare, per aggiungere:
    - `QMenuBar`, `QStatusBar`, `QToolBar`, `QDockWidget`
    - Widget principale al centro

code: C++

    // ... set a layout in the central area
    setCentralWidget(new QWidget);
    centralWidget()->setLayout(layout);

---

title: Menù e toolbar
figure: images/qt/notepad-toolbar.png

code: C++

    class NotepadWindow: public QMainWindow // ...

code: C++

    NotepadWindow::NotepadWindow() {
        auto notepad = new Notepad; setCentralWidget(notepad);

        auto menu = menuBar()->addMenu(tr("&File"));  // QMenu*
        auto open_act = menu->addAction(tr("&Open"));  // QAction*
        auto save_act = menu->addAction(tr("&Save"));
        menu->addSeparator();
        auto exit_act = menu->addAction(tr("E&xit"));
        // auto tools = addToolBar(tr("&File")); tools->addAction(open_act); ...

        connect(open_act, &QAction::triggered, notepad, &Notepad::open);
        connect(save_act, &QAction::triggered, notepad, &Notepad::save);
        connect(exit_act, &QAction::triggered, notepad, &Notepad::exit);
    }

---

title: Griglia di bottoni
class: segue dark

---

title: Griglia di bottoni
figure: images/qt/calculator.png

- **`QGridLayout`**: dispone i widget in una griglia
- All'inserimento del widget, specificare riga e colonna (*0-indexed*)
- Possibile specificare anche l'occupazione di più celle adiacenti

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
    private:
        void handle_click(int x, int y);
        void update_button(int x, int y);
        void update_all_buttons();

        Game* game_;
        int cols_, rows_;
    };

---

title: Fifteen – Costruzione gui

code: C++

    GameGui::GameGui(Game* game) {
        cols_ = game->cols(); rows_ = game->rows();
        game_ = game;
        auto grid = new QGridLayout; setLayout(grid);
        for (auto y = 0; y < rows_; ++y) {
            for (auto x = 0; x < cols_; ++x) {
                auto b = new QPushButton; 
                grid->addWidget(b, y, x);
                connect(b, &QPushButton::clicked,
                        [=]{ handle_click(x, y); });
            }
        }
        update_all_buttons();
    }

- *Funzioni lambda*: anonime, annidate (*Church*, 1936)
- *Closure*: cattura di valori dal contesto; `this`, `x`, `y`

---

title: Fifteen – Aggiornamento bottoni

code: C++

    void GameGui::update_button(int x, int y) {
        auto val = game_->get_val(x, y);
        auto b = layout()->itemAt(y * cols_ + x)->widget();
        dynamic_cast<QPushButton*>(b)->setText(val.c_str());
    }

    void GameGui::update_all_buttons() {
        for (auto y = 0; y < rows_; y++) {
            for (auto x = 0; x < cols_; x++) {
                update_button(x, y);
            }
        }
    }

---

title: Fifteen – Gestione click
figure: images/qt/puzzle-solved.png

code: C++

    void GameGui::handle_click(int x, int y) {
        game_->play_at(x, y);
        update_all_buttons();  // ...

        if (game_->finished()) {
            QMessageBox::information(this,
                                     tr("Game finished"),
                                     tr(game_->message().c_str()));
            window()->close();
        }
    }

---

title: Pyside
class: segue dark

---

title: Pyside – Costruzione gui
figure: images/qt/puzzle.png

code: python

    class GameGui(QWidget):
        def __init__(self, game: Game):
            QWidget.__init__(self)
            self._game = game
            self._cols, self._rows = game.size()
            self.setLayout(QGridLayout())
            for y in range(self._rows):
                for x in range(self._cols):
                    b = QPushButton()
                    self.layout().addWidget(b, y, x)
                    b.clicked.connect(lambda x=x, y=y:
                        self.handle_click(x, y))
            self.update_all_buttons()
        # ...

---

title: Pyside – Aggiornamento bottoni

code: python

    class GameGui(QWidget):
        # ...
        def update_button(self, x: int, y: int):
            val = self._game.get_val(x, y)
            b = self.layout().itemAt(y * self._cols + x).widget()
            b.setText(val)

        def update_all_buttons(self):
            for y in range(self._rows):
                for x in range(self._cols):
                    self.update_button(x, y)
                    
---

title: Pyside – Gestione click
figure: images/qt/puzzle-solved.png

code: python

    class GameGui(QWidget):
        # ...
        def handle_click(self, x: int, y: int):
            self._game.play_at(x, y)
            self.update_all_buttons()
            
            if self._game.finished():
                QMessageBox.information(self, 
                                        self.tr('Game finished'),
                                        self.tr(self._game.message()))
                self.window().close()

---

title: Eventi in Qt
class: segue dark

---

title: Dispatching degli eventi

- Eventi
    - Attività *esterne* che interessano l'applicazione
    - O cambiamenti *interni* all'applicazione
    - Gestibili da qualsiasi istanza di `QObject` (spesso widget)
- Quando si verifica un evento:
    - Creato oggetto per rappresentarlo, istanza (indiretta) di `QEvent`
    - `QResizeEvent`, `QPaintEvent`, `QMouseEvent`, `QKeyEvent`, `QCloseEvent`
- Sulla base del **tipo** di evento:
    - Invocato un **metodo specifico** dell'oggetto interessato
    - Dispatching attraverso il metodo `event` di `QObject`
    - L'evento può essere accettato oppure ignorato

---

title: Eventi della tastiera
figure: images/qt/tetrix.png

code: C++

    void TetrixBoard::keyPressEvent(QKeyEvent* e) {
        switch (e->key()) {
        case Qt::Key_Left:
            tryMove(curPiece, curX - 1, curY);
            break;
            // ...
        case Qt::Key_Down:
            tryMove(curPiece.rotatedRight(), curX, curY);
        break;
            default:
            QFrame::keyPressEvent(e);
        }
    }

Metodi `keyPressEvent` e `keyReleaseEvent` per gestire la tastiera

---

title: Segnali periodici
figure: images/qt/analogclock.png

code: C++

    AnalogClock::AnalogClock() {
        QTimer* timer = new QTimer{this};
        connect(timer, &QTimer::timeout,
                this, &AnalogClock::update);
        timer->start(1000);
    }

    void AnalogClock::paintEvent(QPaintEvent *event) {
        QPainter painter{this};
        // draw the clock ...
    }

`QTimer`: periodicamente emette segnale `timeout`, da associare ad uno (o più) slot

Metodo `paintEvent` per ridisegno di un widget, con oggetto `painter`

---

title: Disegni e animazioni
class: segue dark

---

title: Ridisegno

- Metodo **`update`** accoda una richiesta di ridisegno *asincrono* del widget (evento)
    - L'operazione non avviene immediatamente
    - L'*event dispatcher* esegue il metodo **`paintEvent`** appena può
- Widget Qt operano di default in *double buffering*
    - No *flicker* dovuto a lettura e scrittura effettuate direttamente su aree di memoria → schermo
    - Es. si traccia sfondo prima di img in primo piano
    - Se parte visualizzazione a schermo, img in primo piano scompare per un frame

---

title: Sistema di coordinate
figure: images/qt/coord-rect.png images/qt/coord-line.png

code: C++

    // ...
    QPainter painter{this};
    painter.setPen(Qt::darkGreen);
    painter.drawRect(1, 2, 6, 4);
    painter.drawLine(2, 7, 6, 1);

---

title: Disegno di immagini

- `QPainter` può disegnare anche immagini `QPixmap`
    - `QPainter::drawPixmap(int x, int y, const QPixmap& pixmap);`
    - Immagine caricata facilmente da file, passandone il nome al costruttore
- Immagini su bottoni ed etichette
    - `QPushButton::setPixmap(QPixmap& pixmap)`
    - `QLabel::setIcon(QIcon& icon)`, oppure `setText` con HTML
    - Altrimenti, sfondo: `QWidget::setStyleSheet`
- `QPixmap` sono anche superfici di disegno custom
    - `QPainter::QPainter{QPaintDevice* d};`

---

title: Superfici ed elementi grafici
figure: images/qt/graphicsview.png

- **`QGraphicsScene`**
    - Superficie che contiene diversi elementi grafici bidimensionali: fornisce supporto per animazioni e rilevamento collisioni
- **`QGraphicsItem`**
    - Immagini, linee, poligoni, testo e altri elementi
- **`QGraphicsView`**
    - Widget per visualizzare l'intera scena o per zoomare su una parte

---

title: Dichiarazione di segnali
class: segue dark

---

title: Dichiarazione di segnali

- Qt: distribuzione dei segnali gestita automaticamente
    - I segnali si dichiarano in maniera simile a metodi
    - Non devono essere implementati da nessuna parte
    - Devono restituire `void`
- Nota sugli argomenti
    - L'esperienza mostra che segnali e slot sono più riusabili se non usano tipi speciali
    - Raccogliere segnali da diversi widget sarebbe molto più difficile

---

title: Emissione di segnali

- Un oggetto emette un segnale chiamando `emit`
    - Quando si verifica evento o stato interno cambia
    - Se il cambiamento può interessare altri oggetti
- Emesso segnale → slot connessi eseguiti subito
    - Come una normale chiamata a metodo
    - Codice seguente ad `emit` eseguito dopo aver eseguito tutti gli slot connessi al segnale
    - Se più slot, eseguiti in sequenza arbitraria
- Esistono anche connessioni asincrone (*queued*)
    - Codice dopo `emit` eseguito subito, poi gli slot

---

title: Meta-Object Compiler

- Il *moc* è un programma che gestisce le estensioni di Qt al C++
- Se una dichiarazione di classe contiene la macro `Q_OBJECT`, il *moc* produce altro codice C++ per quella classe
- Tra le altre cose, il “*meta-object code*” è necessario per il meccanismo di segnali e slot
- **Segnali e slot sono una estensione specifica di Qt alla sintassi C++**

---

title: Bottone con click destro

code: C++

    class RightPushButton : public QPushButton {
        Q_OBJECT
    public:
        using QPushButton::QPushButton;
    protected:
        void mouseReleaseEvent(QMouseEvent* e);
    signals:
        void rightClicked();  // new signal, in addition to QPushButton::clicked
    };
    
code: C++
    
    void RightPushButton::mouseReleaseEvent(QMouseEvent* e) {
        if (e->button() == Qt::RightButton) emit rightClicked();
        QPushButton::mouseReleaseEvent(e);  // base class behaviour
    }
        
---

title: Altre caratteristiche di Qt
class: segue dark

---

title: Altre caratteristiche di Qt

![](images/qt/resources.png)

- Possibile inserire dati (img, snd ecc.) direttamente nel file eseguibile
    - Aggiungere un “*Qt Resource File*” al progetto
    - Aggiungere le singole risorse al descrittore `.qrc`
    - Percorso delle risorse richiede “`:`” come prefisso


---

title: Gruppo di bottoni

- **`QButtonGroup`**: raggruppamento *logico* di bottoni
- Non fornisce **nessuna rappresentazione** *visuale*
- Utile per associare i bottoni ad un indice intero
    - Definisce il segnale **`buttonClicked`**, che trasmette come parametro l'indice del bottone
    - Possibile connettere questo segnale anziché il segnale `clicked` di ciascun bottone
- Utile anche per raggruppare bottoni radio
    - Gestisce lo stato di tutti i bottoni nel gruppo
    - Se `exclusive`, solo un bottone selezionato

---
title: Utilizzare le traduzioni

code: C++

    int main(int argc, char* argv[]) {
        QApplication a{argc, argv};

        // run lupdate(.pro->.ts), linguist and lrelease(.ts->.qm), first!
        QTranslator appTranslator;
        appTranslator.load(":/translations/myapp_"
          + QLocale::system().name());
        a.installTranslator(&appTranslator);

        QTranslator qtTranslator;
        qtTranslator.load("qt_" + QLocale::system().name(),
          QLibraryInfo::location(QLibraryInfo::TranslationsPath));
        a.installTranslator(&qtTranslator);

        return a.exec();
    }

---

title: QString

- Caratteri `QChar` a 16 bit (UTF-16, rari simboli a due QChar)
- Metodi `static`: *`fromStdString`*, `number`
- Metodi: *`toStdString`*, `toInt`, `toFloat`
- Metodo `split` (genera una `QStringList`)
- Sostituzione automatica di numeri, caratteri e stringhe
    - `QString status = QString{"Processing file %1 of %2: %3"}.arg(i).arg(total).arg(fileName);`
- Operatori `[], >, <, ==, +, +=` ecc.


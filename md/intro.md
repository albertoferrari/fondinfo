title: Presentazione del corso
subtitle: Fondamenti di informatica + Lab
figure: images/misc/theory-practice.png

---

title: 1. Introduzione all'informatica
figure: images/sys/globe.jpg

- Rappresentazione dei dati
    - Numeri; testi; immagini; suoni
- Teoria della computazione
    - Linguaggi; automi e calcolabilità; complessità
- Sviluppo del software
    - Ciclo di vita; qualità e collaudo
- Sistemi di elaborazione
    - Calcolatori; sistemi operativi; Internet e Web

---

title: 2.  Introduzione alla programmazione
figure: images/misc/problem-solving.jpg
class: large-figure

- Algoritmi in Python 3
- Collezioni e flussi di dati
- Funzioni
- Oggetti e interfacce
- Linguaggio C++11
- Interfacce grafiche

---

title: 3. Esercitazioni in laboratorio
figure: images/misc/geek-girl.jpg

- Esercizi di base, in Python
- Piccoli progetti a oggetti
    - Prima a riga di comando e poi con interfaccia grafica
    - Prima in Python e poi in C++
- **Attenzione**: non sono sufficienti le poche ore in laboratorio per imparare a programmare!
    - “Venite già studiati”
    - Completate tutti gli esercizi, a casa
    - Assiduità!

> If you wish to learn swimming you have to go into the water and if you wish to become a problem solver you have to solve problems. *(George Polya)*

---

title: Istruzioni per i laboratori

- Verificare in anticipo il proprio account per l'accesso ai lab
    - <http://www.cedi.unipr.it/gestioneaccounts>
- Esercitazioni ogni lunedì pomeriggio, su 2 turni distinti
    - 13:30-15:30 *matricole pari*, 15:30-17:30 *matricole dispari*
- Possibile sviluppare da soli o in coppia
    - Ma tassativamente *non più di due!*
    - Se si sviluppa in coppia, turno determinato dalla matricola minore
- Verifica esercitazioni
    - Alla fine di ogni esercitazione, consegna dei programmi in una cartella denominata con la propria matricola
    - Periodicamente, lavori consegnati sottoposti a *valutazioni intermedie*, non preannunciate

---

title: Esame
figure: images/misc/quiz.png

- **(1)** Prova sull'*Introduzione all'informatica* (quiz)
    - A fine corso, oppure...
    - Appelli usuali
- **(2)** Prova sull'*Introduzione alla programmazione* (lab)
    - Svolgimento esercitazioni in laboratorio, oppure…
    - Prova in appelli usuali (~3 ore)
- Le due prove si possono svolgere in tempi diversi e ciascuna resta valida per l'intero anno (fino ad ottobre)
- Il voto finale è determinato:
    - per 1/4 dalla teoria
    - per 3/4 dalla programmazione

---

title: Testi di riferimento
figure: images/misc/books.png

- *Fondamenti di informatica e lab.* (A.A. 2014-2015). McGraw-Hill custom publishing. ISBN 978-13-082-4813-4 (~25€, 250pp., nelle [librerie universitarie](http://www.informagiovanionline.it/emiliaromagna/parma/tempo-libero/godersi-larte-e-la-cultura/libri-in-rete/librerie-scolastiche-e-universitarie-parma) )
- A.B. Downey et al.: *How to Think Like a Computer Scientist*: Learning with Python 3, 3rd Edition - <http://openbookproject.net/thinkcs/>
- M. Beri: *Python*, Apogeo Pocket, 2010, 978-8850329151 (~8€)
- C. S. Horstmann: *Fondamenti di C++*, McGraw-Hill Education, 2003, 978-8838661051 (~43€, 768pp.)

---

title: Altri testi e video

- M. Dawson: *Python Programming for the Absolute Beginner*, Course Technology, 2010, 978-1435455009 (~21€, 450pp.)
- K. A. Lambert: *Programmazione in Python*, Apogeo, 2012, 978-8838786990 (~29€, 384pp.)
- MIT: *Introduction to CS and Programming* - Video delle lezioni, Pyhton 2 - <http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/> <br/> <br/>
- M. Dawson: *Beginning C++ Through Game Programming*, 4th Edition, Course Technology, 2014, 978-1305109919 (~36€, 390pp.)
- A. Lorenzi, V. Moriggia: *Programmazione ad oggetti e linguaggio C++*, Atlas, 2004, 978-8826811956 - Testo per le superiori (~12€, 380pp.)
- S.B. Lippman, J. Lajoie, B.E. Moo: *C++ Primer*, Addison Wesley, 2012, 978-0321714114 (~36€, 940pp.)

---

title: Software
figure: images/misc/python.png images/misc/cpp-logo.jpg

- Strumenti open source, multi-piattaforma
- **Python 3**, *battery included*: <http://python.org/>
    - Brython: <http://brython.info/>
    - PyGame: <http://pygame.org/>
    - PySide: <http://wiki.qt.io/PySide>
- **C++11**: <http://isocpp.org/>
    - Documentazione: <br> <http://cplusplus.com/reference/> <br> <http://cppreference.com/>
    - Librerie Qt ed ambiente di sviluppo <br> <http://qt.io/> <br>
      Windows: ver. 5.x *con MinGW* <br>
      Ubuntu: "qtcreator" da Software Center <br>
      Mac: installare prima il pacchetto "xcode"
    
---

title: Esempi di progetti
class: segue dark

---

title: Pac-Man
figure: images/misc/pac-man.png

- *Pac-Man*
    - Guidato dal giocatore, con la tastiera
    - Applica i comandi solo solo agli incroci
- *Fantasmi*
    - Uccidono Pac-Man se lo toccano
    - Agli incroci svoltano casualmente
    - Ma non tornano mai indietro!
- *Biscotti*
    - Pac-Man deve mangiarli tutti, per terminare il gioco
- *SuperBiscotti*
    - Danno per breve tempo a Pac-Man il potere di mangiare i fantasmi

---

title: Slitherlink
figure: images/misc/slitherlink-solved.png

- Regole
    - Connect adjacent dots with vertical or horizontal lines to make a single loop
    - The numbers indicate how many lines surround it, while empty cells may be surrounded by any number of lines
    - The loop never crosses itself and never branches off

>

<http://www.nikoli.com/en/puzzles/slitherlink/>

<https://www.brainbashers.com/slitherlinkhelp.asp>

---

title: Bubble Bobble
figure: images/misc/bubble-bobble.png

- *Draghetto*: guidato dal giocatore
    - Si muove e salta sulle *piattaforme*
    - Muore se cade in fondo allo schermo
- *Avversari*
    - Saltano come il draghetto sulle *piattaforme*
    - Ma scelgono casualmente la direzione
    - Uccidono il draghetto se lo urtano
- *Bolle*
    - Lanciate in orizzontale dal draghetto
    - Dopo un po' deviano verso l'alto
    - Catturano gli avversari che urtano

---

title: Hitori
figure: images/misc/hitori.svg images/misc/hitori-completed.svg

- Regole
    - Color cells so no number appears more than once in a row or column
    - The sides of black cells never touch
    - White cells form a continuous network
- Ad ogni mossa, permettere all'utente di annerire un numero, oppure cerchiarlo
    - Controllare la violazione delle regole
    - Controllare il completamento del gioco (ogni numero: correttamente annerito o cerchiato) 

>

<http://www.nikoli.com/en/puzzles/hitori>

---

title: Snake
figure: images/misc/snake.png

- **Serpente**: guidato dal giocatore
    - Avanza continuamente
    - Non può tornare indietro
    - Se tocca se stesso, muore
- **Cibo**: disposto casualmente
    - Il serpente si allunga dopo aver mangiato
- **Muri**: in posizione fissa
    - Il serpente muore se ci va a sbattere

---

title: Prato fiorito
figure: images/misc/mines.png

- N <b>fiori nascosti</b> a caso in tabella rettangolare
- Ad ogni turno, l'utente scopre una casella:
    - Fiore → <i>partita persa</i>
    - Solo N caselle coperte (con fiori) → <i>partita vinta</i>
    - Altrimenti, <i>conteggio fiori</i> nelle 8 caselle adiacenti

---

title: Akari - Light up
figure: images/misc/akari.svg

- Scopo: <b>illuminare</b> tutte le celle bianche
    - Una lampada illumina tutte le celle visibili sulla sua riga e la sua colonna
    - Due lampade non possono illuminarsi a vicenda
    - Vincolo numerico: # lampade nelle 4 celle adiacenti

>

<http://www.nikoli.com/en/puzzles/bijutsukan/rule.html>

---

title: Othello
figure: images/misc/othello.png

- In due, bianco e nero
    - All'inizio: 2 coppie di pedine al centro, incrociate
    - A turno, ciascun giocatore aggiunge una pedina
    - È obbligatorio catturare, se non ci sono mosse si passa il turno
- Se viene *circondata una fila* di pedine avversarie, queste cambiano tutte colore
- Vince chi alla fine ha più pedine

---

title: Pong
figure: images/misc/pong.png

- Campo rettangolare
- **Pallina**: si muove a 45°, rimbalza su bordi lunghi e barrette
- **Barrette**: si muovono solo verticalmente
- **Punti**: segnati quando la pallina esce dal campo

---

title: Frogger
figure: images/misc/frogger.png

- **Rana** guidata dall'utente, salta in 4 direzioni: ↕ ↔
- Deve attraversare la strada, senza essere investita dai **camion**
- Deve attraversare il fiume, saltando sui **tronchi**

---

title: Space invaders
figure: images/misc/invaders.png

- **Cannone**: l'utente lo sposta in orizzontale; spara verso l'alto, contro gli alieni
- **Alieni**: si muovono tutti nella stessa direzione; percorso a serpentina; sparano verso il basso, contro il cannone
- **Muri**: si ditruggono lentamente dove colpiti

---

title: Tents puzzle
figure: images/misc/tents.png

- Posizionare tende sulla griglia, in modo che ogni albero sia *assegnato* ad una tenda
    - Inizialmente, nessun albero è assegnato ad una tenda
    - Tenda adiacente (in orizzontale o verticale) ad un solo albero non assegnato ⇒ albero *assegnato* a quella tenda
    - Tante tende, quanti sono gli alberi
- Le tende non possono toccarsi tra loro, nemmeno in diagonale
- Vincoli numerici fuori dalla griglia: numero di tende nella riga o colonna

>

<http://www.brainbashers.com/tentshelp.asp>



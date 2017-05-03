title: Bubble Bobble in Python
subtitle: Stage formativo a Ingegneria Informatica 12-16 giugno 2017
figure: images/misc/space-invaders.png

---

title: A chi è rivolto lo stage?
figure: images/misc/young-programmer.png

- A **tutti** gli studenti delle scuole superiori
- Senza particolari prerequisiti
- **Corso introduttivo alla programmazione**: ognuno imparerà qualcosa
- … Ma utili eventuali precedenti esperienze, con qualsiasi linguaggio <br />
- Agli studenti senza precedente esperienza di programmazione, si consiglia di seguire le esercitazioni pomeridiane, che si svolgeranno tutti i giorni dello stage (h.14:00-18:00)

---

title: Come si svolgerà? 
figure: images/misc/geek-girl.jpg
class: large-image

- Ogni giorno, dalle 9:00 alle 13:00
    - ~ *un'ora* di lezione e *tre* di lavoro al computer
    - Lavoro in autonomia, ma assistito dall'insegnante
- Tutti i pomeriggi, possibilità di assistenza per gli esercizi proposti

Giorno | Argomento
-------|----------
Lun 12/6 | Programmazione strutturata in Python
Mar 13/6 | Oggetti e animazioni grafiche
Mer 14/6 | Creazione personaggi
Mer 15/6 | Interazione tra personaggi
Ven 16/6 | Completamento del gioco

---

title: A cosa servirà?

- Realizzazione in *autonomia* di una versione funzionante e *personale* del gioco **Space Invaders**, eseguibile su piattaforme diverse
- Introduzione alla programmazione e al *problem solving*: concetti base, orientamento a modularità e riuso
- Panoramica sulle attività di laboratorio dei corsi di base di *Ingegneria Informatica*
- Sperimentazione diretta con *strumenti* di sviluppo gratuiti, liberi e multi-piattaforma

> If you wish to learn swimming you have to go into the water and if you wish to become a problem solver you have to solve problems. *(George Polya)*

---

title: Come iscriversi?

- Lo stage è **gratuito**, ma limitato ad un numero massimo di 90 studenti
- Per iscriversi, entro il **30 aprile**, inviare richiesta a: <stage@ce.unipr.it> (tel. 0521-905708)
    - Da ciascuna scuola saranno inizialmente ammessi al massimo 5 studenti
    - Gli studenti in sovrannumero saranno tenuti in attesa e ammessi solo nel caso di posti disponibili
    - Gli studenti infine ammessi dovranno inviare conferma della presenza, entro il 31 maggio
- Gli alunni interessati sono invitati a rivolgersi alla segreteria del proprio istituto, per l'inoltro della richiesta
    - **Fac-simile** del modulo di richiesta d'iscrizione disponibile su <http://www.ce.unipr.it/stage>

---

title: Strumenti utilizzati
figure: images/misc/python.png images/misc/devices.png images/misc/raspberry-pi.png

- **Python 3**, *battery included*
    - <http://python.org/>
- Libreria Pygame
    - <http://pygame.org/>
- Sviluppo **open-source** e **multi-piattaforma**
    - PC, cellulari e tablet
- Anche su Raspberry Pi
    - <http://raspberrypi.org/>

---

title: Approfondimento
figure: images/misc/books.png

- A.B. Downey et al.: *How to Think Like a Computer Scientist: Learning with Python 3*, 3rd Edition - <http://openbookproject.net/thinkcs/>
- M. Beri: *Python*, Apogeo Pocket, 2010, 978-8850329151
- M. Dawson: *Python Programming for the Absolute Beginner*, Course Technology, 2010, 978-1435455009
- MIT: *Introduction to CS and Programming* - Video delle lezioni, Pyhton 2 - <http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/>

---

title: Esempi di progetti
class: segue dark

---

title: Frogger
figure: images/misc/frogger.png

- **Rana** guidata dall'utente, salta in 4 direzioni: ↕ ↔
- Deve attraversare la strada, senza essere investita dai **camion**
- Deve attraversare il fiume, saltando sui **tronchi**

---

title: Super Mario
figure: images/misc/super-mario.jpg

- *Mario*: guidato dal giocatore
    - Si muove e salta sulle piattaforme
    - Cade secondo gravità, fuori dalle piattaforme
    - Ma non accelera oltre una velocità limite
    - Muore se cade in fondo allo schermo
- *Muri e piattaforme*
    - Mario ci atterra dall'alto
    - Non si possono attraversare in nessuna direzione
- *Avversari*
    - Si muovono sulle piattaforme come Mario, ma scelgono casualmente la direzione
    - Uccidono Mario se lo urtano, ma muoiono se Mario ci salta sopra

---

title: Bubble Bobble
figure: images/misc/bubble-bobble.png

- *Draghetto*: guidato dal giocatore
    - Si muove e salta sulle piattaforme
    - Cade, fuori dalle piattaforme
    - Muore se cade in fondo allo schermo
- *Piattaforme*
    - Il draghetto ci atterra dall'alto
    - Si possono attraversare dal basso verso l'alto
    - Non si possono attraversare lateralmente
- *Avversari*
    - Si muovono come il draghetto
    - Ma scelgono casualmente la direzione
    - Uccidono il draghetto se lo urtano

---

title: Space invaders
figure: images/misc/invaders.png

- **Cannone**: l'utente lo sposta in orizzontale; spara verso l'alto, contro gli alieni
- **Alieni**: si muovono tutti nella stessa direzione; percorso a serpentina; sparano verso il basso, contro il cannone
- **Muri**: si ditruggono lentamente dove colpiti

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

title: Hitori
figure: images/misc/hitori.svg images/misc/hitori-completed.svg

- Color cells so no number appears more than once in a row or column
- The sides of black cells never touch
- White cells form a continuous network

>

<http://www.nikoli.com/en/puzzles/hitori>

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

title: Slitherlink
figure: images/misc/slitherlink.png

- Regole
    - Connect adjacent dots with vertical or horizontal lines to make a single loop
    - The numbers indicate how many lines surround it, while empty cells may be surrounded by any number of lines
    - The loop never crosses itself and never branches off

>

<http://www.nikoli.com/en/puzzles/slitherlink/>

<https://www.brainbashers.com/slitherlinkhelp.asp>



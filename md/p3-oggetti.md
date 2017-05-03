title: Oggetti e grafica
subtitle: Introduzione alla programmazione
figure: images/oop/modules.png images/oop/pygame-logo.png

---

title: Oggetto
figure: images/oop/basic-object.svg

- Rappresenta un *oggetto fisico* o un *concetto* del dominio
- Memorizza il suo **stato** interno in *campi privati*
    - *Incapsulamento (black box)*
- Offre un insieme di **servizi**, come *metodi pubblici*
    - Realizza un *tipo di dato astratto (ADT)*

---

title: Classi ed oggetti
figure: images/oop/cookie-cutter.png

- Ogni *oggetto* ha una **classe** di origine
    - La classe dà la stessa forma iniziale (campi e metodi) a tutti i suoi oggetti
- Ma ogni *oggetto* ha la sua **identità** 
    - Stato e locazione in memoria distinti da quelli di altri oggetti
    - Sia instanze di classi diverse che della stessa classe

---

title: Definizione della classe
figure: images/oop/ball-object.svg images/oop/ball-uml.svg
figcaption: Class diagram UML

- **Incapsulamento** dei dati: *convenzione* sui nomi
    - Prefisso `_` per i nomi dei *campi privati*

> Siamo tutti adulti consenzienti. *(GvR)*
      
code: python

    class Ball:
        W, H = 20, 20
        ARENA_W, ARENA_H = 320, 240

        def __init__(self, x: int, y: int):
            self._x = x
            self._y = y
            self._dx = 5
            self._dy = 5
        # ...

---

title: Costruzione oggetti

- **`__init__`**: metodo *inizializzatore*
    - Eseguito automaticamente alla creazione di un oggetto
    - *Instantiation is initialization*
- **`self`**: primo parametro di tutti i metodi
    - Non bisogna passare un valore esplicito
    - Assegnato l'oggetto di cui si chiama il metodo
    - Permette ai metodi di accedere ai campi
- Costanti definite direttamente nella *classe*
    - Per usarle, precedute dal nome della classe e “`.`”
    - Caratteristiche della classe, non di una singola istanza

code: python

    ball = Ball(40, 80)  # Allocation and initialization

---

title: Metodi

- Espongono *servizi* ad altri oggetti

code: python

    class Ball:
        # ...
        def move(self):
            if not (0 <= self._x + self._dx <= Ball.ARENA_W - Ball.W):
                self._dx = -self._dx
            if not (0 <= self._y + self._dy <= Ball.ARENA_H - Ball.H):
                self._dy = -self._dy
            self._x += self._dx
            self._y += self._dy

        def rect(self) -> (int, int, int, int):
            return self._x, self._y, Ball.W, Ball.H

---

title: Applicazione

code: python

    from p4_ball import Ball  # Ball is defined in p4_ball.py

    # Create two objects, instances of the Ball class
    b1 = Ball(40, 80)
    b2 = Ball(80, 40)
    print('Ball 1 @', b1.rect())
    print('Ball 2 @', b2.rect())

    while input() != 'x':
        b1.move()
        b2.move()
        print('Ball 1 @', b1.rect())
        print('Ball 2 @', b2.rect())

---

title: Il primo parametro, self

- Il primo parametro di ogni metodo si chiama `self` (per convenzione)
- L'oggetto, di cui viene invocato il metodo, viene assegnato come valore di `self`
- In Python, una chiamata a metodo è interpretata così:

code: python

    b1 = Ball(40, 80)
    b1.move()
    
code: python

    b1 = Ball(40, 80)  # also, automatically call
                       # Ball.__init__(b1, 40, 80)
    Ball.move(b1)

**Nota.** Meglio usare la prima notazione, che evidenzia l'*oggetto* anzichè la classe!

---

title: Animazione di due palline

code: python

    from game2d import *
    from p4_ball import Ball

    def update():
        canvas_fill(canvas, (255, 255, 255))  # BG
        b1.move()
        b2.move()
        draw_rect(canvas, (127, 127, 127), b1.rect())  # FG
        draw_rect(canvas, (127, 127, 127), b2.rect())  # FG

    b1 = Ball(40, 80)
    b2 = Ball(80, 40)
    canvas = canvas_init((Ball.ARENA_W, Ball.ARENA_H))
    set_interval(update, 1000 // 30)  # Millis

---

title: Animazione lista di palline

code: python

    from game2d import *
    from p4_ball import Ball

    def update():
        canvas_fill(canvas, (255, 255, 255))  # BG
        for b in balls:
            b.move()
            draw_rect(canvas, (127, 127, 127), b.rect())  # FG

    balls = [Ball(40, 80), Ball(80, 40), Ball(120, 120)]
    canvas = canvas_init((Ball.ARENA_W, Ball.ARENA_H))
    set_interval(update, 1000 // 30)  # Millis

---

title: Composizione
figure: images/oop/ball-arena.svg

- Associazione di tipo **has-a**, **part-of** tra oggetti
    - Una *arena* può *contenere* diverse *palline*

code: python

    class BallArena:  # ...
        def __init__(self):
            self._balls = []
        def add(self, b: Ball):
            self._balls.append(b)
        def move_all(self):
            for b in self._balls:
                b.move()

code: python

    arena = BallArena()
    arena.add(Ball(40, 80)); arena.add(Ball(80, 40)) # ...
    arena.move_all()

---

title: Proprietà (++)

- Permettono un accesso controllato allo stato

code: python

    class Ball:

        @property  # a getter for the pos property
        def pos(self) -> (int, int):
            return self._x, self._y

        # @pos.setter  # if you also really need a setter
        # def pos(self, val: (int, int)):
        #     self._x, self._y = val

code: python

    ball = Ball(40, 80)
    print('ball @', ball.pos)
    # ball.pos = (60, 20)   # with the setter, you could change the pos

---

title: Ciclo di vita di un oggetto (++)
figure: images/dev/garbage-truck.jpg

- Creazione di un oggetto: allocata memoria per tenere lo stato dell’oggetto
- In Python: variabile = riferimento ad un oggetto
    - *Oggetti*: *allocazione dinamica*, in memoria *heap*
    - *Variabili*: *allocazione automatica*, in memoria *stack*
- Oggetto non più associato a nessuna variabile: necessario liberare memoria
- **Garbage collection**: gestione automatica della restituzione di memoria

---

title: Garbage collection (++)

- Vantaggi
    - Non è possibile dimenticare di liberare la memoria (*memory leak*)
    - Non è possibile liberare della memoria che dovrà essere utilizzata in seguito (*dangling pointer*)
- Svantaggi
    - Il garbage collector decide autonomamente quando liberare la memoria
    - Liberare e compattare la memoria richiede del calcolo
- Diversi algoritmi
    - *Reference counting*: idea di base, ma cicli…
    - *Mark & sweep*: parte da riferimenti locali/globali, marca oggetti raggiungibili
    - *Generational garbage collection*: controlla spesso oggetti recenti

---

title: Livelli di astrazione
class: segue dark backdrop

---

title: Livelli di astrazione
figure: images/oop/inheritance.png

- Relazione **is-a** tra classi
    - Specializzazione, sotto-insieme
- Es. classificazioni in biologia
    - I *vertebrati* sono una sottoclasse degli *animali*
    - I *mammiferi* sono una sottoclasse dei *vertebrati*
    - I *felini* sono una sottoclasse dei *mammiferi*
    - I *gatti* sono una sottoclasse dei *felini*
- Ogni sottoclasse...
    - Eredita le caratteristiche della classe base
    - Ma introduce delle specializzazioni

---

title: Livelli di astrazione
figure: images/oop/actors.svg

- `Actor`: *classe base*
    - Dichiara un metodo `move` ecc.
- Vari attori: *classi derivate*
    - Ereditano caratteristiche di `Actor`
    - Definiscono comportamenti specifici

code: python

    class Actor:
        def move(self):
            raise NotImplementedError("Abstract method")

---

title: Generalizzazione e riuso

code: python

    class Arena:  # ...
        def __init__(self):
            self._actors = []
        def add(self, a: Actor):
            self._actors.append(a)
        def move_all(self):
            for a in self._actors:
                a.move()

- Codice dipendente dalle classi più astratte, più in alto nella gerarchia
    - `Arena` riutilizzabile creando nuove classi derivate di `Actor`

---

title: Sostituzione
figure: images/oop/actor.svg

code: python

    arena.add(Ball(40, 80))
    arena.add(Ghost(120, 40)) # ...
    arena.move_all()

- Principio di **sostituzione** di Liskov
    - Si può sempre usare un oggetto di una *classe derivata*, al posto di uno della *classe base*
- Relazione *has-a* tra un oggetto `Arena` e gli oggetti `Actor` che contiene
- Relazione *is-a* tra classi derivate (`Ball` e `Ghost`) e classe base (`Actor`)

---

title: Ereditarietà e polimorfismo

- **Classe derivata**
    - Eredita le caratteristiche della classe base
    - Può definire nuove caratteristiche specifiche
- **Metodo polimorfo**
    - Ridefinito nelle classi derivate
    - Attori diversi possono muoversi in modo diverso

code: python

    class Ghost(Actor):  # ...
        def move(self):
            dx = random.choice([-5, 0, 5])
            dy = random.choice([-5, 0, 5])
            arena_w, arena_h = self._arena.size()
            self._x = (self._x + dx) % arena_w
            self._y = (self._y + dy) % arena_h

---

title: Animazione dei personaggi
class: segue dark

---

title:  Rimbalzi nel browser
figure: images/oop/bounce.png

code: python

    from game2d import *
    from bounce import Arena, Ball, Ghost, Turtle

    def update():
        arena.move_all()  # Game logic
        canvas_fill(canvas, (255, 255, 255))  # Background
        for a in arena.actors():
            x, y, w, h = a.rect();  xs, ys = a.symbol()
            # Foreground; cut an area from a larger image__init__
            image_blit(canvas, sprites, (x, y), area=(xs, ys, w, h))

    arena = Arena(320, 240)
    Ball(arena, 40, 80);  Ball(arena, 80, 40);  Ghost(arena, 120, 80)
    turtle = Turtle(arena, 80, 80)
    canvas = canvas_init(arena.size())
    sprites = image_load("sprites.png")
    set_interval(update, 1000 // 30)  # Millis

---

title:  Controllo da tastiera
figure: images/oop/bounce.png

code: python

    def keydown(e):
        if e.code == "ArrowUp":
            turtle.go_up()
        elif e.code == "ArrowDown":
            turtle.go_down()
        elif e.code == "ArrowLeft":
            turtle.go_left()
        elif e.code == "ArrowRight":
            turtle.go_right()

    def keyup(e):
        turtle.stay()

    doc.onkeydown = keydown
    doc.onkeyup = keyup

---

title: Collisioni
figure: images/oop/collision.svg images/oop/reflection.png

- Molti algoritmi di *collision detection*
    - Casi semplici: intersezione di rettangoli
- In caso di collisione, `Arena`...
    - Invoca il metodo `collide` di entrambi gli oggetti
    - Collisione tra personaggio `self` e personaggio `other` (secondo parametro)
- Possibili errori nel calcolo del rimbalzo
    - Di solito accettabili
    - Altrimenti, applicare correzioni
    
---

title: Urti delle palline

code: python

    class Ball(Actor):
        # ...
        def collide(self, other):
            if not isinstance(other, Ghost):
                x, y, w, h = other.rect()
                if x < self._x:
                    self._dx = self.SPEED
                else:
                    self._dx = -self.SPEED
                # ... same for y

- `isinstance(obj, cls)`
    - Controlla se l'oggetto `obj` è istanza della classe `cls`
    - ... o di una sua sottoclasse
    - Restituisce un `bool`

---

title: Grafica con pyGame (++)
figure: images/oop/pygame-logo.png images/oop/pygame-loop.png

- Libreria per giochi 2D
- Grafica e suoni
- Su *SDL* - Simple DirectMedia Layer
- Semplice e veloce
- Open-source
- Multi-piattaforma

>

[pygame.org](http://www.pygame.org/)

---

title:  Disegno con PyGame (++)
figure: images/oop/pygame-logo.png images/oop/raster-coord.png
figcaption: → pygame.org/docs

code: python

    import pygame
    pygame.init()                     # Prepare pygame
    screen = pygame.display.set_mode((640, 480)) # (w, h)
    screen.fill((255, 255, 255))      # BG (Red, Green Blue)

    # Yellow rectangle, left=50, top=75, w=90, h=50
    pygame.draw.rect(screen, (255, 255, 0), (50, 75, 90, 50))

    # Blue circle, center=(300, 50), radius=20
    pygame.draw.circle(screen, (0, 0, 255), (300, 50), 20)

    pygame.display.flip()             # Update the screen
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

---

title: Animazione con PyGame (++)

code: python

    import pygame
    pygame.init()                     # Prepare pygame
    screen = pygame.display.set_mode((320, 240))
    clock = pygame.time.Clock()       # To set game speed
    image = pygame.image.load('ball.png')

    x = 50; playing = True
    while playing:
        for e in pygame.event.get():  # Handle events: mouse, keyb etc.
            if e.type == pygame.QUIT: playing = False
        screen.fill((255, 255, 255))  # Draw background        
        screen.blit(image, (x, 50))   # Draw foreground
        x = (x + 5) % 320             # Update ball's position
        pygame.display.flip()         # Surface ready, show it!
        clock.tick(30)                # Wait 1/30 seconds
    pygame.quit()                     # Close the window

---

title: Ciclo di animazione (++)

code: python

    import pygame
    pygame.init()                     # Prepare pygame
    screen = pygame.display.set_mode((320, 240))
    clock = pygame.time.Clock()       # To set game speed
    image = pygame.image.load('ball.png')

    x = 50; playing = True
    while playing:
        for e in pygame.event.get():  # Handle events: mouse, keyb etc.
            if e.type == pygame.QUIT: playing = False
        screen.fill((255, 255, 255))  # Draw background        
        screen.blit(image, (x, 50))   # Draw foreground
        x = (x + 5) % 320             # Update ball's position
        pygame.display.flip()         # Surface ready, show it!
        clock.tick(30)                # Wait 1/30 seconds
    pygame.quit()                     # Close the window

---

title:  Rimbalzi in PyGame (++)
figure: images/oop/bounce.png

code: python

    arena = Arena(320, 240)
    Ball(arena, 40, 80); Ball(arena, 80, 40); 
    Ghost(arena, 120, 80) # ...
    # a map from an actor type to an image
    images = {Ball: pygame.image.load('ball.png'),
              Ghost: pygame.image.load('ghost.png')}
    screen = pygame.display.set_mode(arena.size())
    playing = True
    while playing:
        # Handle events here!

        arena.move_all()             # Game logic
        screen.fill((255, 255, 255)) # Background
        for a in arena.actors():
            x, y, w, h = a.rect()
            img = images[type(a)]
            screen.blit(img, (x, y)) # Foreground [...]

---

title:  Tastiera e mouse (++)

code: python

    from pygame.locals import (KEYDOWN, KEYUP, K_RIGHT, K_d,
        MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION)
    # ...
    for e in pygame.event.get():
        # print(e)
        if e.type == KEYDOWN and e.key in (K_RIGHT, K_d):
            print('Right arrow (or D) pressed')
        elif e.type == KEYUP and e.key in (K_RIGHT, K_d):
            print('Right arrow (or D) released')
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            print('Left mouse button pressed')
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            print('Left mouse button released')
        elif e.type == MOUSEMOTION:
            print 'Mouse at (%d, %d)' % e.pos

---

title: Testo e suoni (++)

code: python

    # Red (anti-aliased) text, centered, rotated 30° ccw
    font = pygame.font.SysFont('arial', 48)
    surface = font.render('Game over!', True, (255, 0, 0))
    surface = pygame.transform.rotate(surface, 30)
    x = (screen.get_width() - surface.get_width()) // 2
    y = (screen.get_height() - surface.get_height()) // 2
    screen.blit(surface, (x, y))  # surface ~ image

code: python

    # Some sound
    pick_up_sound = pygame.mixer.Sound('pickup.wav')
    pick_up_sound.play()  # play(-1) to loop, then stop()

---

title: Collaudo in Python
class: segue dark

---

title: Come collaudare il codice?

- Usare un *debugger* per valutare espressioni in fase di esecuzione
    - Si può decidere cosa valutare a seconda del flusso di esecuzione e dei valori generati, senza ricompilare
- Istruzioni di *stampa* all'interno del programma
    - Valore di espressioni scritto a console o su file di log
- Entrambi gli stili, scarsamente *automatizzati*
    - Necessità di intervento attivo durante i test
    - Giudizio dei risultati da parte dell'utente
    - Quali valori analizzare? Sono coerenti?
- Scarsamente *componibili*
    - Difficile controllare molte espressioni nel debugger
    - "*Scroll blindness*": troppe istruzioni di stampa ⇒ codice poco leggibile

---

title: Libreria unittest

- I test `unittest` non richiedono continuo intervento o giudizio da parte dell'utente
- Facile eseguire molti test assieme, su un certo progetto
- Come definire un test?
    - Creare una sottoclasse di `unittest.TestCase`
    - Scrivere metodi di test, denominati con prefisso `test`
    - Per controllare la validità di una espressione, usare `assertTrue(bool)`

---

title: Esempio di test

- Controllare che una pallina rimbalzi correttamente contro il bordo inferiore

code: Python

    import unittest

    class SimpleBallTest(unittest.TestCase):

        def test_bounce_down(self):
            b = Ball(300, 220)  # dx = 5, dy = 5
            b.move()
            self.assertTrue(b.rect() == (295, 215, 20, 20))

    if __name__ == '__main__':
        unittest.main(exit=False)

---

title: Esecuzione dei test

- Meccanismi per definire i test da eseguire e organizzare i risultati
- Esecuzione di test dalla linea di comando
    - Inclusione dei test di un modulo, di una classe, o metodi di test specifici
    - Implementata anche una semplice forma di *test discovery*

code: cmd
    
    python -m unittest test_module1 test_module2
    python -m unittest test_module.TestClass
    python -m unittest test_module.TestClass.test_method
    python -m unittest discover

- Annotazione `@unittest.skip("reason for skipping")`
    - Indica al framework di ignorare un certo metodo di test
    - Messaggio per documentare la decisione

---

title: Controllare le eccezioni

- Mestiere del programmatore
    - Codice che completa correttamente l'esecuzione nei casi normali...
    - Ma che anche in situazioni eccezionali mostra il comportamento atteso
- Come verificare che una eccezione attesa sia effettivamente sollevata?
    - Usare il metodo `assertRaises` direttamente, passando una funzione ed i parametri
    - Oppure creare un *contesto* con `with`
- Esempio: `Ball` solleva effettivamente una eccezione attesa?
    
code: Python

    def test_out_of_arena(self): 
        with self.assertRaises(ValueError):
            b = Ball(-1, -1)
---

title: Test parametrizzati

- Ripetere un test con diversi parametri
    - Un test case per ogni gruppo di parametri?
    - In alcune applicazioni, enorme quantità di test!
- Soluzione semplicistica: test contente un ciclo
    - Ad ogni iterazione, preparato un gruppo di parametri diversi
    - Eseguite le istruzioni da testare sui nuovi parametri
    - Problema: il test si blocca al primo errore

---

title: Test parametrizzato, semplicistico

code: Python

    class ParamBallTest(unittest.TestCase):
        TEST_VALUES = ( (40, 80, 45, 85),
                        (40, 215, 45, 220),
                        (40, 220, 45, 215),
                        (295, 80, 300, 85),
                        (300, 80, 290, 85) )

        def test_move(self):
            for param in ParamBallTest.TEST_VALUES:
                x0, y0, x1, y1 = param
                b = Ball(x0, y0)
                b.move()
                self.assertTrue(b.rect() == (x1, y1, 20, 20))


---

title: Sotto-test, Python 3.4

- Eseguiti tutti i sottotest, anche se uno fallisce

code: Python

    class ParamBallTest(unittest.TestCase):
        TEST_VALUES = ()  # same values...

        def test_move(self):
            for param in ParamBallTest.TEST_VALUES:
                with self.subTest(param=param):
                    x0, y0, x1, y1 = param
                    b = Ball(x0, y0)
                    b.move()
                    self.assertTrue(b.rect() == (x1, y1, 20, 20))

---

title: Fixture

- Due o più test operano su insiemi di oggetti uguali o simili
    - Questa configurazione iniziale comune si definisce *fixture*
- Se ci sono diversi test con una fixture comune...
    - Aggiungere dei campi per le varie parti della fixture
    - Inizializzare questi campi, nel metodo `setUp`
    - Liberare evenutali risorse allocate, nel metodo `tearDown`
- Una volta creata la fixture, può essere usata da tutti i test case
    - Aggiungere metodi di test alla classe
    - `setUp` e `tearDown` eseguiti prima e dopo ogni test

---

title: Esempio di fixture

- Numerosi metodi di test che operano su stessi dati iniziali
    - Esempio, una combinazione di palline in posizioni predefinite

code: Python

    class SimpleBallTest(unittest.TestCase):
        
        def setUp(self): 
            self.b1 = Ball(80, 40)
            self.b2 = Ball(40, 80)
            self.b3 = Ball(120, 20)


---

title: Test suite

- Meccanismo per *raggruppare* logicamente dei test ed *eseguirli assieme*
- La classe `TestSuite` rappresenta una test suite
    - Lista di classi di test aggiunte con il metodo `addTest`
- La classe `TestRunner` rappresenta un esecutore di test
    - Per la console, si usa `TextTestRunner`, già inclusa nel framework

code: Python

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleBallTest))
    runner = unittest.TextTestRunner()
    runner.run(suit)


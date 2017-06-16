title: Gui con Tkinter
subtitle: Introduzione alla programmazione
figure: images/oop/tk-logo.svg

---

title: Gui con Tkinter

- Tk: libreria leggera e intuitiva, per interfacce grafiche
- In Python modulo `tkinter` (*Tk interface*)
- Portabile tra diversi sistemi
- Usa le primitive grafiche della piattaforma ospite
    - → Efficiente anche su sistemi embedded
- Windows, MacOS, Linux, vari Unix...
- Tcl, Ruby, Python, Perl

---

title:  Hello Notepad
figure: images/oop/tk-notepad-1.png

code: Python

    from tkinter import Tk, Text

    window = Tk()
    text_edit = Text(window)
    text_edit.pack(expand=1, fill='both')
    window.title('Notepad')
    # event loop: mouse, keyb etc.
    window.mainloop()

---

title:  Aggiungere un bottone
figure: images/oop/tk-notepad-2.png

code: Python

    from tkinter import Tk, Text, Button

    window = Tk()
    text_edit = Text(window)
    text_edit.pack()

    # When button is clicked, window's
    # destroy method is executed
    quit_button = Button(window, text='Quit',
                         command=window.destroy)
    # widgets in vertical layout
    quit_button.pack()

    window.title('Notepad')
    window.mainloop()

---

title:  Classe per il Notepad

code: Python

    from tkinter import Tk, Text, Button, messagebox
    class Notepad(Tk):
        def __init__(self):
            super().__init__()
            # basic widgets as private fields
            self._text = Text(self)
            self._text.pack()
            self._quit = Button(self, text='Quit', command=self.exit)
            self._quit.pack()
        def exit(self):
            if messagebox.askokcancel('Quit', 'Are you sure?'):
                self.destroy()
    if __name__ == '__main__':
        win = Notepad()
        win.mainloop()

---

title:  Creazione di un menù

code: Python

    from tkinter import Tk, Text, Menu

    class Notepad(tk.Tk):
        def __init__(self):
            super().__init__()
            text_edit = Text(self)
            text_edit.pack()

            menu_bar = Menu(self)  # tearoff=0
            self.config(menu=menu_bar)
            menu_file = Menu(menu_bar)
            menu_file.add_command(label='Open')
            menu_file.add_command(label='Save')
            menu_file.add_command(label='Exit', command=self.exit)
            menu_bar.add_cascade(label='File', menu=menu_file)  # ...
            
---

title: Disposizione widget
figure: images/oop/tk-notepad-3.png

- Tk usa il meccanismo dei *geometry manager* per disporre i widget
- Ci sono tre sistemi di disposizione pricipali
- È possibile comporre più `Frame` (riquadri), per realizzare gerarchie di contenimento tra widget

code: Pyhton

    # vertical layout, default side='top'
    widget.pack()
    # horizontal layout
    widget.pack(side='left')
    # grid layout
    widget.grid(column=x, row=y)

---

title:  Riquadri compositi

code: Python

    from tkinter import Tk, Text, Frame, Button

    class Notepad(Tk):
        def __init__(self):
            super().__init__()
            text_edit = Text(self)
            text_edit.pack(side='left')

            v_box = Frame(self)
            v_box.pack(side='left')  # fill='y'
            open_btn = Button(v_box, text='Open')
            open_btn.pack()  # side='top'
            save_btn = Button(v_box, text='Save')
            save_btn.pack()
            exit_btn = Button(v_box, text='Exit')
            exit_btn.pack()

---

title:  Layout a griglia
figure: images/oop/tk-fifteen-gui.png

- Divide in una griglia lo spazio disponibile e dispone i widget nelle celle
- Specificare riga e colonna all'inserimento (l'indice parte da 0)
- Possibile specificare anche l'occupazione di più celle adiacenti

---

title:  FifteenGui – Costruttore

code: Python

    class FifteenGui(Tk):
        def __init__(self, puzzle: FifteenPuzzle):
            super().__init__()
            self._puzzle = puzzle
            self._cols = puzzle.cols()
            self._rows = puzzle.rows()
            for y in range(self._rows):
                for x in range(self._cols):
                    b = Button(self, command=lambda x=x, y=y:
                               self.handle_click(x, y))
                    b.grid(column=x, row=y)
            self.update_buttons()
        # ...

---

title:  FifteenGui – Click

code: Python

    class FifteenGui(Tk):
        # ...
        def handle_click(self, x: int, y: int):
            self._puzzle.move_position(x, y)
            self.update_buttons()
            if self._puzzle.is_finished():
                messagebox.showinfo('Congrats', 'Puzzle solved')
                self.destroy()
                
        def update_buttons(self):
            for y in range(self._rows):
                for x in range(self._cols):
                    val = str(self._puzzle.get(x, y))
                    # Get the button on the grid @ (x, y)
                    b = self.grid_slaves(column=x, row=y)[0]
                    b['text'] = val


from tkinter import *

class Accueil:
    def __init__(self, root, back_callback):
        self.root = root
        self.root.geometry('1280x720')
        self.root['bg'] = 'black'
        self.root.resizable(height=False, width=False)

        self.accueil_frame = Frame(root, bg='white')
        self.accueil_frame.pack(expand=YES, fill=BOTH)

        label = Label(self.accueil_frame, text="Blue Launcher", font=("algerian", 28), fg='blue')
        label.place(x=0, y=10)

        self.back_button = Button(self.accueil_frame, text="Retour", command=back_callback, font=("algerian", 12), bg='grey', fg='orange', relief=RAISED)
        self.back_button.place(x=10, y=50)

    def show(self):
        self.accueil_frame.pack(expand=YES, fill=BOTH)

    def hide(self):
        self.accueil_frame.pack_forget()

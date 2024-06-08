from tkinter import *
from tkinter import ttk, messagebox
from data.database_handler import DatabaseHandler

class Formulaire:
    def __init__(self, frame, back_callback):
        self.frame = frame
        self.back_callback = back_callback
        self.db_handler = DatabaseHandler('login.db')

        # Titre de page
        title = Label(frame, text="Blue Launcher", font=("algerian", 28), bg='black', fg='blue')
        title.pack(pady=5)

        

        # Champ du formulaire
        box = Frame(self.frame, bg='grey')
        box.place(x=300, y=100, width=700, height=500)

        btitle = Label(box, text='Créer un compte', font=('algerian', 18, 'bold'), bg='grey', fg='orange')
        btitle.place(x=50, y=30)

        # Username
        user = Label(box, text='Gamertags', font=("times new roman", 15), bg='grey', fg='black')
        user.place(x=50, y=90)
        self.writeu = Entry(box, font=("times new roman", 12), bg='lightgrey')
        self.writeu.place(x=50, y=120)

        # Prénom
        prenom = Label(box, text='Prénom', font=("times new roman", 15), bg='grey', fg='black')
        prenom.place(x=370, y=90)
        self.writepn = Entry(box, font=("times new roman", 12), bg='lightgrey')
        self.writepn.place(x=370, y=120)

        # Nom
        nom = Label(box, text='Nom', font=("times new roman", 15), bg='grey', fg='black')
        nom.place(x=370, y=150)
        self.writen = Entry(box, font=("times new roman", 12), bg='lightgrey')
        self.writen.place(x=370, y=180)

        # Password
        password = Label(box, text='Mot de passe', font=("times new roman", 15), bg='grey', fg='black')
        password.place(x=50, y=150)
        self.writep = Entry(box, font=("times new roman", 12), bg='lightgrey', fg='black', show='*')
        self.writep.place(x=50, y=180)

        confpass = Label(box, text='Confirmer le mot de passe', font=("times new roman", 15), bg='grey', fg='black')
        confpass.place(x=50, y=210)
        self.writecp = Entry(box, font=("times new roman", 12), bg='lightgrey', show='*')
        self.writecp.place(x=50, y=240)

        # Email
        email = Label(box, text='Email', font=("times new roman", 15), bg='grey', fg='black')
        email.place(x=370, y=210)
        self.writee = Entry(box, font=("times new roman", 12), bg='lightgrey')
        self.writee.place(x=370, y=240)

        # Question
        question = Label(box, text='Choisissez une question', font=("times new roman", 15), bg='grey', fg='black')
        question.place(x=50, y=270)
        self.writeq = ttk.Combobox(box, font=("times new roman", 12), state='readonly', style='TCombobox')
        self.writeq['values'] = ('select', 'Ton surnom', 'Ton lieu de naissance', 'Ton meilleur jeu')
        self.writeq.place(x=50, y=300)
        self.writeq.current(0)

        reponse = Label(box, text='Repondre', font=("times new roman", 15), bg='grey', fg='black')
        reponse.place(x=370, y=270)
        self.writeqr = Entry(box, font=("times new roman", 12), bg='lightgrey')
        self.writeqr.place(x=370, y=300)

        # Terme et condition
        self.var_chech = IntVar()
        chk = Checkbutton(box, variable=self.var_chech, onvalue=1, offvalue=0, text="J'accepte les termes et les conditions", font=("times new roman", 12), bg='grey')
        chk.place(x=50, y=330)

        # Bouton creer le compte
        cbtn = Button(box, text="Créer le compte", command=self.creer, font=("algerian", 18), bg='grey', fg='orange', bd=3, relief=RAISED)
        cbtn.place(x=50, y=380)
        cbtn.bind("<Enter>", self.on_enter)
        cbtn.bind("<Leave>", self.on_leave)

        # Bouton retour
        retour_btn = Button(box, text="Retour", command=self.back_callback, font=("algerian", 18), bg='grey', fg='orange', bd=3, relief=RAISED)
        retour_btn.place(x=50, y=430)
        cbtn.bind("<Enter>", self.on_enter)
        cbtn.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(relief=SUNKEN, bd=5)

    def on_leave(self, event):
        event.widget.config(relief=RAISED, bd=5)

    def creer(self):
        if self.writepn.get() == "" or self.writeu.get() == "" or self.writee.get() == "" or self.writep.get() == "" or self.writecp.get() == "" or self.writeq.get() == "" or self.writeqr.get() == "":
            messagebox.showerror("erreur", "Remplir les champs", parent=self.root)
        elif self.writep.get() != self.writecp.get():
            messagebox.showerror("erreur", "Les mots de passe ne sont pas identiques", parent=self.root)
        elif self.var_chech.get() == 0:
            messagebox.showerror("Erreur", "Veuillez accepter les termes et conditions.", parent=self.root)
        else:
            try:
                # Insérer les données dans la base de données
                self.db_handler.create_person(
                    self.writeu.get(),
                    self.writepn.get(),
                    self.writen.get(),
                    self.writee.get(),
                    self.writep.get(),
                    self.writeq.get(),
                    self.writeqr.get()
                )
                messagebox.showinfo("Succès", "Compte créé avec succès!", parent=self.root)
            except Exception as es:
                messagebox.showerror("erreur", f"Erreur de connexion: {str(es)}", parent=self.root)

    def show(self):
        self.frame.pack(expand=YES, fill=BOTH)

    def hide(self):
        self.frame.pack_forget()
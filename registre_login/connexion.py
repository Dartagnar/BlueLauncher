from tkinter import *
from tkinter import messagebox

class LoginInterface:
    def __init__(self, root, create_account_callback, accueil_callback):
        self.root = root
        self.root.geometry('1280x720')
        self.root['bg'] = 'black'
        self.root.resizable(height=False, width=False)

        self.create_account_callback = create_account_callback
        self.accueil_callback = accueil_callback

        self.login_frame = Frame(root, bg='black')
        self.login_frame.pack(expand=YES, fill=BOTH)


        # titre de page
        label = Label(self.login_frame, text="Blue Launcher", font=("algerian", 28), bg='black', fg='blue')
        label.pack(pady=10)

        # champ de connexion
        self.boxco = Frame(self.login_frame, bg='grey', highlightbackground='white', highlightthickness=2)
        self.boxco.place(x=465, y=120, width=350, height=400)

        titleco = Label(self.boxco, text="Connexion", font=("algerian", 18, 'bold'), bg='grey', fg='orange')
        titleco.place(x=50, y=30)

        # username
        gamertags = Label(self.boxco, text='Gamertags', font=("times new roman", 15), bg='grey', fg='black')
        gamertags.place(x=75, y=90)
        self.writeu = Entry(self.boxco, font=("times new roman", 12), bg='lightgrey')
        self.writeu.place(x=75, y=120)

        # password
        password = Label(self.boxco, text='Mot de passe', font=("times new roman", 15), bg='grey', fg='black')
        password.place(x=75, y=150)
        self.writep = Entry(self.boxco, font=("times new roman", 12), bg='lightgrey')
        self.writep.place(x=75, y=180)

        # bouton creer un compte
        self.create_account_button = Button(self.boxco, text="Créer un compte", font=("algerian", 12), bg='grey', fg='orange', relief=RAISED, command=create_account_callback)
        self.create_account_button.place(x=40, y=215)
        self.create_account_button.bind("<Enter>", self.on_enter)
        self.create_account_button.bind("<Leave>", self.on_leave)

        # bouton connexion
        self.cobtn = Button(self.boxco, command=self.connex, text="Connexion", font=("algerian", 12), 
        bg='grey', fg='orange', bd=3, relief=RAISED)
        self.cobtn.place(x=200, y=215)
        self.cobtn.bind("<Enter>", self.on_enter)
        self.cobtn.bind("<Leave>", self.on_leave)

        # bouton temporaire accueil
        self.tab = Button(self.boxco, text="accueil", command=accueil_callback)
        self.tab.place(x=40, y=250)

    def on_enter(self, event):
        event.widget.config(relief=SUNKEN, bd=5)

    def on_leave(self, event):
        event.widget.config(relief=RAISED, bd=5)

    # message derreur
    def connex(self):
        if self.writeu.get()=="" or self.writep.get()=="":
            messagebox.showerror("erreur","Veuillez entrer les champs si dessous", parent=self.root)
        
            # reste a faire la fonction pour que le bouton connexionn switch sur la page accueil si le user et password sont valider avec la database





        
    # doit etre a la fin (sert a masquer la page)
    def show(self):
        self.login_frame.pack(expand=YES, fill=BOTH)

    def hide(self):
        self.login_frame.pack_forget()

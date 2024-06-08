from tkinter import *
from tkinter import messagebox
from registre_login.formulaire import Formulaire
from registre_login.connexion import LoginInterface
from core.accueil import Accueil

class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720')
        self.root.title('Blue Launcher')
        self.root['bg'] = 'black'
        self.root.resizable(height=True, width=True)

        # instance de connexion
        self.login_interface = LoginInterface(root, self.show_create_account, self.show_accueil)
        
        # instance de l'accueil
        self.accueil_interface = Accueil(root, self.show_login)
        self.accueil_interface.hide()  # cacher l'instance accueil au demarrage
        
        self.form_frame = Frame(root, bg='black')
        self.formulaire_interface = None  # Initialiser l'interface de formulaire à None

    def show_create_account(self):
        self.login_interface.hide()
        self.accueil_interface.hide()  # Cacher l'accueil lors de l'affichage du formulaire de création de compte
        if self.formulaire_interface is None:
            # Créer l'interface de formulaire seulement si elle n'existe pas encore
            self.form_frame.pack(expand=YES, fill=BOTH)
            self.formulaire_interface = Formulaire(self.form_frame, self.show_login)
        else:
            # Si l'interface de formulaire existe déjà, simplement l'afficher
            self.form_frame.pack(expand=YES, fill=BOTH)
            self.formulaire_interface.show()

    def show_login(self):
        self.form_frame.pack_forget()
        self.accueil_interface.hide()  # Cacher l'accueil lors de l'affichage de la connexion
        self.login_interface.show()

    def show_accueil(self):
        self.login_interface.hide()
        self.form_frame.pack_forget()
        self.accueil_interface.show()

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    app.login_interface.show()  # Affiche l'interface de connexion au démarrage
    root.mainloop()

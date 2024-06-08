import os
import sqlite3

class DatabaseHandler:
    def __init__(self, Database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{Database_name}")
        self.con.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        cursor = self.con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Gamertags TEXT,
                Prénom TEXT,
                Nom TEXT,
                Email TEXT,
                Mot_de_passe TEXT,
                question TEXT,
                reponse TEXT
            )
        """)
        cursor.close()
        self.con.commit()

    def create_person(self, Gamertags: str, Prénom: str, Nom: str, Email: str, Mot_de_passe: str, question: str, reponse: str):
        cursor = self.con.cursor()
        query = """
            INSERT INTO login (Gamertags, Prénom, Nom, Email, Mot_de_passe, question, reponse) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (Gamertags, Prénom, Nom, Email, Mot_de_passe, question, reponse))
        cursor.close()
        self.con.commit()

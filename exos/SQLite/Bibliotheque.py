import sqlite3

con = sqlite3.connect('biblio.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Auteurs
            (idAuteur PRIMARY KEY, nom text, prenom text, nat text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Livres
            (idLivre PRIMARY KEY, titre text, annee integer, auteur text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Abonnes
            (idAbonne PRIMARY KEY, nom text, prenom text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Emprunts
            (idAbonne text, idLivre text)''')
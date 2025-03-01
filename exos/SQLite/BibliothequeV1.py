import sqlite3

# Connexion à la base et activation des clés étrangères
con = sqlite3.connect('biblio.db')
con.execute("PRAGMA foreign_keys = ON")
cur = con.cursor()

# Création des tables

# Table Auteurs
cur.execute('''
    CREATE TABLE IF NOT EXISTS Auteurs (
        idAuteur INTEGER PRIMARY KEY AUTOINCREMENT, 
        nom TEXT, 
        prenom TEXT, 
        nat TEXT
    )
''')

# Table Livres avec contrainte de clé étrangère vers Auteurs
cur.execute('''
    CREATE TABLE IF NOT EXISTS Livres (
        idLivre INTEGER PRIMARY KEY AUTOINCREMENT, 
        titre TEXT, 
        annee INTEGER, 
        auteur INTEGER,
        FOREIGN KEY(auteur) REFERENCES Auteurs(idAuteur)
    )
''')

# Table Abonnes
cur.execute('''
    CREATE TABLE IF NOT EXISTS Abonnes (
        idAbonne INTEGER PRIMARY KEY AUTOINCREMENT, 
        nom TEXT, 
        prenom TEXT
    )
''')

# Table Emprunts avec clé primaire composite et clés étrangères
cur.execute('''
    CREATE TABLE IF NOT EXISTS Emprunts (
        idAbonne INTEGER, 
        idLivre INTEGER,
        PRIMARY KEY (idAbonne, idLivre),
        FOREIGN KEY(idAbonne) REFERENCES Abonnes(idAbonne),
        FOREIGN KEY(idLivre) REFERENCES Livres(idLivre)
    )
''')

con.commit()


def menu():
    print("=== Menu Bibliothèque ===")
    print("1. Obtenir la liste des livres (avec les informations de l'auteur)")
    print("2. Obtenir la liste des auteurs")
    print("3. Obtenir la liste des abonnés")
    print("4. Obtenir la liste des emprunts (avec les informations de l'abonné et du livre)")
    print("5. Obtenir la liste des livres empruntés")
    print("6. Ajouter un livre")
    print("7. Ajouter un auteur")
    print("8. Ajouter un abonné")
    print("9. Ajouter un emprunt")
    print("10. Supprimer un emprunt")
    print("11. Obtenir les informations sur un livre (par titre)")
    print("12. Obtenir la liste des livres d'une année donnée")
    print("13. Obtenir la liste des livres d'un auteur donné")
    print("14. Obtenir la liste des emprunts d'un abonné")
    print("15. Obtenir le nombre de livres de la bibliothèque")
    print("16. Obtenir le nom des abonnés")
    print("17. Obtenir le nombre de livres empruntés par un abonné")
    print("18. Obtenir le nombre de livres empruntés")
    print("19. Savoir si un livre est emprunté ou disponible")
    print("0. Quitter")


def lister_livres():
    query = '''
        SELECT Livres.titre, Livres.annee, Auteurs.nom, Auteurs.prenom 
        FROM Livres 
        JOIN Auteurs ON Livres.auteur = Auteurs.idAuteur
    '''
    for row in cur.execute(query):
        print(row)


def lister_auteurs():
    query = "SELECT * FROM Auteurs"
    for row in cur.execute(query):
        print(row)


def lister_abonnes():
    query = "SELECT * FROM Abonnes"
    for row in cur.execute(query):
        print(row)


def lister_emprunts():
    query = """
        SELECT Emprunts.idAbonne, Abonnes.nom, Abonnes.prenom, 
                Emprunts.idLivre, Livres.titre
        FROM Emprunts
        JOIN Abonnes ON Emprunts.idAbonne = Abonnes.idAbonne
        JOIN Livres ON Emprunts.idLivre = Livres.idLivre
    """
    for row in cur.execute(query):
        print(row)


def lister_livres_empruntes():
    query = """
        SELECT DISTINCT Livres.idLivre, Livres.titre, Livres.annee, 
                        Auteurs.nom, Auteurs.prenom
        FROM Livres
        JOIN Emprunts ON Livres.idLivre = Emprunts.idLivre
        JOIN Auteurs ON Livres.auteur = Auteurs.idAuteur
    """
    for row in cur.execute(query):
        print(row)


def ajouter_livre():
    titre = input("Titre du livre : ")
    annee = input("Année de sortie : ")

    # Display available authors
    print("Liste des auteurs disponibles :")
    query = "SELECT idAuteur, nom, prenom FROM Auteurs"
    for row in cur.execute(query):
        print(row)

    auteur_id = input("Entrez l'id de l'auteur : ")

    # Check if the author ID exists in the Auteurs table
    query = "SELECT COUNT(*) FROM Auteurs WHERE idAuteur = ?"
    cur.execute(query, (auteur_id,))
    count = cur.fetchone()[0]

    if count == 0:
        print("L'ID de l'auteur n'existe pas dans la base de données. Veuillez essayer un ID valide.")
    else:
        # Insert the book if the author ID is valid
        query = "INSERT INTO Livres (titre, annee, auteur) VALUES (?, ?, ?)"
        cur.execute(query, (titre, annee, auteur_id))
        con.commit()
        print("Livre ajouté.")



def ajouter_auteur():
    nom = input("Nom de l'auteur : ")
    prenom = input("Prénom de l'auteur : ")
    nat = input("Nationalité de l'auteur : ")
    query = "INSERT INTO Auteurs (nom, prenom, nat) VALUES (?, ?, ?)"
    cur.execute(query, (nom, prenom, nat))
    con.commit()
    print("Auteur ajouté.")


def ajouter_abonne():
    nom = input("Nom de l'abonné : ")
    prenom = input("Prénom de l'abonné : ")
    query = "INSERT INTO Abonnes (nom, prenom) VALUES (?, ?)"
    cur.execute(query, (nom, prenom))
    con.commit()
    print("Abonné ajouté.")


def ajouter_emprunt():
    print("Liste des abonnés :")
    query = "SELECT idAbonne, nom, prenom FROM Abonnes"
    for row in cur.execute(query):
        print(row)
    idAbonne = input("Entrez l'id de l'abonné : ")
    
    print("Liste des livres disponibles (non empruntés) :")
    query = """ SELECT idLivre, titre FROM Livres 
                WHERE idLivre NOT IN (SELECT idLivre FROM Emprunts)
    """
    for row in cur.execute(query):
        print(row)
    idLivre = input("Entrez l'id du livre à emprunter : ")
    
    query = "INSERT INTO Emprunts (idAbonne, idLivre) VALUES (?, ?)"
    try:
        cur.execute(query, (idAbonne, idLivre))
        con.commit()
        print("Emprunt ajouté.")
    except sqlite3.IntegrityError as e:
        print("Erreur lors de l'ajout de l'emprunt :", e)


def supprimer_emprunt():
    idAbonne = input("Entrez l'id de l'abonné : ")
    idLivre = input("Entrez l'id du livre à retourner : ")
    query = "DELETE FROM Emprunts WHERE idAbonne = ? AND idLivre = ?"
    cur.execute(query, (idAbonne, idLivre))
    con.commit()
    print("Emprunt supprimé (livre retourné).")


def infos_livre():
    titre = input("Entrez le titre du livre : ")
    query = """ SELECT Livres.idLivre, Livres.titre, Livres.annee, Auteurs.nom, Auteurs.prenom
                FROM Livres
                JOIN Auteurs ON Livres.auteur = Auteurs.idAuteur
                WHERE Livres.titre LIKE ?
    """
    for row in cur.execute(query, ('%' + titre + '%',)):
        print(row)


def livres_annee():
    annee = input("Entrez l'année : ")
    query = "SELECT * FROM Livres WHERE annee = ?"
    for row in cur.execute(query, (annee,)):
        print(row)


def livres_auteur():
    auteur_nom = input("Entrez le nom de l'auteur : ")
    query = """ SELECT Livres.idLivre, Livres.titre, Livres.annee 
                FROM Livres
                JOIN Auteurs ON Livres.auteur = Auteurs.idAuteur
                WHERE Auteurs.nom LIKE ?
    """
    for row in cur.execute(query, ('%' + auteur_nom + '%',)):
        print(row)


def emprunts_abonne():
    idAbonne = input("Entrez l'id de l'abonné : ")
    query = """ SELECT Emprunts.idLivre, Livres.titre, Livres.annee
                FROM Emprunts
                JOIN Livres ON Emprunts.idLivre = Livres.idLivre
                WHERE Emprunts.idAbonne = ?
    """
    for row in cur.execute(query, (idAbonne,)):
        print(row)


def nb_livres():
    query = "SELECT COUNT(*) FROM Livres"
    count = cur.execute(query).fetchone()[0]
    print("Nombre de livres dans la bibliothèque :", count)


def nom_abonnes():
    query = "SELECT nom, prenom FROM Abonnes"
    for row in cur.execute(query):
        print(row)


def nb_livres_abonne():
    idAbonne = input("Entrez l'id de l'abonné : ")
    query = "SELECT COUNT(*) FROM Emprunts WHERE idAbonne = ?"
    count = cur.execute(query, (idAbonne,)).fetchone()[0]
    print("Nombre de livres empruntés par l'abonné :", count)


def nb_livres_empruntes():
    query = "SELECT COUNT(*) FROM Emprunts"
    count = cur.execute(query).fetchone()[0]
    print("Nombre total de livres empruntés :", count)


def etat_livre():
    idLivre = input("Entrez l'id du livre : ")
    query = "SELECT COUNT(*) FROM Emprunts WHERE idLivre = ?"
    count = cur.execute(query, (idLivre,)).fetchone()[0]
    if count > 0:
        print("Le livre est emprunté.")
    else:
        print("Le livre est disponible.")


# Boucle principale du menu
while True:
    menu()
    choix = input("Votre choix : ")
    if choix == "1":
        lister_livres()
    elif choix == "2":
        lister_auteurs()
    elif choix == "3":
        lister_abonnes()
    elif choix == "4":
        lister_emprunts()
    elif choix == "5":
        lister_livres_empruntes()
    elif choix == "6":
        ajouter_livre()
    elif choix == "7":
        ajouter_auteur()
    elif choix == "8":
        ajouter_abonne()
    elif choix == "9":
        ajouter_emprunt()
    elif choix == "10":
        supprimer_emprunt()
    elif choix == "11":
        infos_livre()
    elif choix == "12":
        livres_annee()
    elif choix == "13":
        livres_auteur()
    elif choix == "14":
        emprunts_abonne()
    elif choix == "15":
        nb_livres()
    elif choix == "16":
        nom_abonnes()
    elif choix == "17":
        nb_livres_abonne()
    elif choix == "18":
        nb_livres_empruntes()
    elif choix == "19":
        etat_livre()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide")
    input("Appuyez sur Entrée pour continuer...")
    print()
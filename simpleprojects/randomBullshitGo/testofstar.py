import sqlite3

# Création de la base de données et de la table Clients
def creer_base():
    with sqlite3.connect('clients.db') as con:
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Clients (
                idClient INTEGER PRIMARY KEY AUTOINCREMENT, 
                nom TEXT NOT NULL, 
                prenom TEXT NOT NULL, 
                age INTEGER CHECK(age > 0)
            )
        ''')
        con.commit()

# Ajouter un client
def ajouter_client():
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    
    # Vérification de l'âge
    while True:
        try:
            age = int(input("Âge : ").strip())
            if age <= 0:
                print("L'âge doit être un nombre positif.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un âge valide.")

    try:
        with sqlite3.connect('clients.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Clients (nom, prenom, age) VALUES (?, ?, ?)", (nom, prenom, age))
            con.commit()
            print(f"✅ Client {nom} {prenom} ajouté avec succès.")
    except sqlite3.Error as e:
        print("❌ Erreur lors de l'ajout :", e)

# Modifier un client
def modifier_client():
    afficher_clients()
    try:
        id_client = int(input("Entrez l'ID du client à modifier : ").strip())
        nom = input("Nouveau nom : ").strip()
        prenom = input("Nouveau prénom : ").strip()
        age = int(input("Nouvel âge : ").strip())

        with sqlite3.connect('clients.db') as con:
            cur = con.cursor()
            cur.execute("UPDATE Clients SET nom=?, prenom=?, age=? WHERE idClient=?", (nom, prenom, age, id_client))
            if cur.rowcount > 0:
                con.commit()
                print(f"✅ Client {id_client} modifié avec succès.")
            else:
                print("❌ Aucun client trouvé avec cet ID.")
    except ValueError:
        print("❌ ID ou âge invalide.")
    except sqlite3.Error as e:
        print("❌ Erreur lors de la modification :", e)

# Supprimer un client
def supprimer_client():
    afficher_clients()
    try:
        id_client = int(input("Entrez l'ID du client à supprimer : ").strip())

        with sqlite3.connect('clients.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Clients WHERE idClient=?", (id_client,))
            if cur.rowcount > 0:
                con.commit()
                print(f"✅ Client {id_client} supprimé avec succès.")
            else:
                print("❌ Aucun client trouvé avec cet ID.")
    except ValueError:
        print("❌ ID invalide.")
    except sqlite3.Error as e:
        print("❌ Erreur lors de la suppression :", e)

# Afficher les clients
def afficher_clients():
    try:
        with sqlite3.connect('clients.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Clients")
            clients = cur.fetchall()
            if clients:
                print("\n📜 Liste des clients :")
                print("-" * 40)
                for client in clients:
                    print(f"ID: {client[0]} | Nom: {client[1]} | Prénom: {client[2]} | Âge: {client[3]}")
                print("-" * 40)
            else:
                print("📭 Aucun client trouvé.")
    except sqlite3.Error as e:
        print("❌ Erreur lors de l'affichage :", e)

# Menu principal
def menu():
    while True:
        print("\n📌 MENU PRINCIPAL")
        print("1️⃣  Ajouter un client")
        print("2️⃣  Modifier un client")
        print("3️⃣  Supprimer un client")
        print("4️⃣  Afficher les clients")
        print("9️⃣  Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_client()
        elif choix == "2":
            modifier_client()
        elif choix == "3":
            supprimer_client()
        elif choix == "4":
            afficher_clients()
        elif choix == "9":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide. Veuillez essayer à nouveau.")

# Lancer le programme
if __name__ == "__main__":
    creer_base()
    menu()

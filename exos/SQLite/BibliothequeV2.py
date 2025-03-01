import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Database Connection
con = sqlite3.connect('biblio.db')
con.execute("PRAGMA foreign_keys = ON")
cur = con.cursor()

# Create Tables (if not exist)
def create_tables():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Auteurs (
            idAuteur INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom TEXT, 
            prenom TEXT, 
            nat TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Livres (
            idLivre INTEGER PRIMARY KEY AUTOINCREMENT, 
            titre TEXT, 
            annee INTEGER, 
            auteur INTEGER,
            FOREIGN KEY(auteur) REFERENCES Auteurs(idAuteur)
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Abonnes (
            idAbonne INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom TEXT, 
            prenom TEXT
        )
    ''')
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

# GUI Setup
root = tk.Tk()
root.title("Bibliothèque")
root.geometry("800x600")
root.configure(bg="#2E2E2E")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#444", font=("Arial", 12))
style.configure("TLabel", foreground="white", background="#2E2E2E", font=("Arial", 12))
style.configure("TFrame", background="#2E2E2E")
style.configure("TText", background="#444", foreground="white")

# Main Frame
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Title
title_label = ttk.Label(frame, text="Bibliothèque", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Output Text Widget
output_text = tk.Text(frame, height=15, wrap="word", bg="#444", fg="white", font=("Arial", 12))
output_text.pack(fill="both", expand=True, pady=10)

# Fetch and display books
def list_books():
    output_text.delete("1.0", tk.END)
    query = """
        SELECT Livres.titre, Livres.annee, Auteurs.nom, Auteurs.prenom 
        FROM Livres 
        JOIN Auteurs ON Livres.auteur = Auteurs.idAuteur
    """
    result = cur.execute(query).fetchall()
    for row in result:
        output_text.insert(tk.END, f"{row}\n")

# Other functions for displaying information
def list_authors():
    output_text.delete("1.0", tk.END)
    query = "SELECT * FROM Auteurs"
    result = cur.execute(query).fetchall()
    for row in result:
        output_text.insert(tk.END, f"{row}\n")

def list_subscribers():
    output_text.delete("1.0", tk.END)
    query = "SELECT * FROM Abonnes"
    result = cur.execute(query).fetchall()
    for row in result:
        output_text.insert(tk.END, f"{row}\n")

def list_loans():
    output_text.delete("1.0", tk.END)
    query = """
        SELECT Emprunts.idAbonne, Abonnes.nom, Abonnes.prenom, 
               Emprunts.idLivre, Livres.titre
        FROM Emprunts
        JOIN Abonnes ON Emprunts.idAbonne = Abonnes.idAbonne
        JOIN Livres ON Emprunts.idLivre = Livres.idLivre
    """
    result = cur.execute(query).fetchall()
    for row in result:
        output_text.insert(tk.END, f"{row}\n")

# Functions for adding data
def add_author():
    def submit():
        cur.execute("INSERT INTO Auteurs (nom, prenom, nat) VALUES (?, ?, ?)", (name_entry.get(), surname_entry.get(), nationality_entry.get()))
        con.commit()
        messagebox.showinfo("Succès", "Auteur ajouté !")
        add_window.destroy()
    
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un Auteur")
    ttk.Label(add_window, text="Nom:").pack()
    name_entry = ttk.Entry(add_window)
    name_entry.pack()
    ttk.Label(add_window, text="Prénom:").pack()
    surname_entry = ttk.Entry(add_window)
    surname_entry.pack()
    ttk.Label(add_window, text="Nationalité:").pack()
    nationality_entry = ttk.Entry(add_window)
    nationality_entry.pack()
    ttk.Button(add_window, text="Ajouter", command=submit).pack()

def add_book():
    def submit():
        cur.execute("INSERT INTO Livres (titre, annee, auteur) VALUES (?, ?, ?)", (title_entry.get(), year_entry.get(), author_entry.get()))
        con.commit()
        messagebox.showinfo("Succès", "Livre ajouté !")
        add_window.destroy()
    
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un Livre")
    ttk.Label(add_window, text="Titre:").pack()
    title_entry = ttk.Entry(add_window)
    title_entry.pack()
    ttk.Label(add_window, text="Année:").pack()
    year_entry = ttk.Entry(add_window)
    year_entry.pack()
    ttk.Label(add_window, text="ID Auteur:").pack()
    author_entry = ttk.Entry(add_window)
    author_entry.pack()
    ttk.Button(add_window, text="Ajouter", command=submit).pack()

def add_subscriber():
    def submit():
        cur.execute("INSERT INTO Abonnes (nom, prenom) VALUES (?, ?)", (name_entry.get(), surname_entry.get()))
        con.commit()
        messagebox.showinfo("Succès", "Abonné ajouté !")
        add_window.destroy()
    
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un Abonné")
    ttk.Label(add_window, text="Nom:").pack()
    name_entry = ttk.Entry(add_window)
    name_entry.pack()
    ttk.Label(add_window, text="Prénom:").pack()
    surname_entry = ttk.Entry(add_window)
    surname_entry.pack()
    ttk.Button(add_window, text="Ajouter", command=submit).pack()

# Buttons Frame
buttons_frame = ttk.Frame(frame)
buttons_frame.pack(fill="x", pady=10)

# Buttons
buttons = [
    ("Lister Livres", list_books),
    ("Lister Auteurs", list_authors),
    ("Lister Abonnés", list_subscribers),
    ("Lister Emprunts", list_loans),
    ("Ajouter Auteur", add_author),
    ("Ajouter Livre", add_book),
    ("Ajouter Abonné", add_subscriber),
    ("Quitter", root.quit)
]

for text, command in buttons:
    btn = ttk.Button(buttons_frame, text=text, command=command)
    btn.pack(side="left", padx=5, pady=5)

# Initialize tables
create_tables()

# Run the application
root.mainloop()

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
root.geometry("850x800")
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
        SELECT  Emprunts.idAbonne, Abonnes.nom, Abonnes.prenom, 
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

def add_loan():
    def submit():
        cur.execute("INSERT INTO Emprunts (idAbonne, idLivre) VALUES (?, ?)", (subscriber_entry.get(), book_entry.get()))
        con.commit()
        messagebox.showinfo("Succès", "Emprunt ajouté !")
        add_window.destroy()
    
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un Emprunt")
    ttk.Label(add_window, text="ID Abonné:").pack()
    subscriber_entry = ttk.Entry(add_window)
    subscriber_entry.pack()
    ttk.Label(add_window, text="ID Livre:").pack()
    book_entry = ttk.Entry(add_window)
    book_entry.pack()
    ttk.Button(add_window, text="Ajouter", command=submit).pack()

def remove_loan():
    def submit():
        cur.execute("DELETE FROM Emprunts WHERE idAbonne = ? AND idLivre = ?", (subscriber_entry.get(), book_entry.get()))
        con.commit()
        messagebox.showinfo("Succès", "Emprunt supprimé !")
        remove_window.destroy()
    
    remove_window = tk.Toplevel(root)
    remove_window.title("Supprimer un Emprunt")
    ttk.Label(remove_window, text="ID Abonné:").pack()
    subscriber_entry = ttk.Entry(remove_window)
    subscriber_entry.pack()
    ttk.Label(remove_window, text="ID Livre:").pack()
    book_entry = ttk.Entry(remove_window)
    book_entry.pack()
    ttk.Button(remove_window, text="Supprimer", command=submit).pack()

def book_info_by_title():
    def submit():
        query = "SELECT * FROM Livres WHERE titre = ?"
        result = cur.execute(query, (title_entry.get(),)).fetchall()
        output_text.delete("1.0", tk.END)
        for row in result:
            output_text.insert(tk.END, f"{row}\n")
        info_window.destroy()
    
    info_window = tk.Toplevel(root)
    info_window.title("Informations Livre par Titre")
    ttk.Label(info_window, text="Titre:").pack()
    title_entry = ttk.Entry(info_window)
    title_entry.pack()
    ttk.Button(info_window, text="Obtenir", command=submit).pack()

def books_by_year():
    def submit():
        query = "SELECT * FROM Livres WHERE annee = ?"
        result = cur.execute(query, (year_entry.get(),)).fetchall()
        output_text.delete("1.0", tk.END)
        for row in result:
            output_text.insert(tk.END, f"{row}\n")
        year_window.destroy()
    
    year_window = tk.Toplevel(root)
    year_window.title("Livres par Année")
    ttk.Label(year_window, text="Année:").pack()
    year_entry = ttk.Entry(year_window)
    year_entry.pack()
    ttk.Button(year_window, text="Obtenir", command=submit).pack()

def books_by_author():
    def submit():
        query = "SELECT * FROM Livres WHERE auteur = ?"
        result = cur.execute(query, (author_entry.get(),)).fetchall()
        output_text.delete("1.0", tk.END)
        for row in result:
            output_text.insert(tk.END, f"{row}\n")
        author_window.destroy()
    
    author_window = tk.Toplevel(root)
    author_window.title("Livres par Auteur")
    ttk.Label(author_window, text="ID Auteur:").pack()
    author_entry = ttk.Entry(author_window)
    author_entry.pack()
    ttk.Button(author_window, text="Obtenir", command=submit).pack()

def loans_by_subscriber():
    def submit():
        query = """
            SELECT Emprunts.idLivre, Livres.titre
            FROM Emprunts
            JOIN Livres ON Emprunts.idLivre = Livres.idLivre
            WHERE Emprunts.idAbonne = ?
        """
        result = cur.execute(query, (subscriber_entry.get(),)).fetchall()
        output_text.delete("1.0", tk.END)
        for row in result:
            output_text.insert(tk.END, f"{row}\n")
        subscriber_window.destroy()
    
    subscriber_window = tk.Toplevel(root)
    subscriber_window.title("Emprunts par Abonné")
    ttk.Label(subscriber_window, text="ID Abonné:").pack()
    subscriber_entry = ttk.Entry(subscriber_window)
    subscriber_entry.pack()
    ttk.Button(subscriber_window, text="Obtenir", command=submit).pack()

def total_books():
    query = "SELECT COUNT(*) FROM Livres"
    result = cur.execute(query).fetchone()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Total des livres : {result[0]}\n")

def subscribers_names():
    query = "SELECT nom, prenom FROM Abonnes"
    result = cur.execute(query).fetchall()
    output_text.delete("1.0", tk.END)
    for row in result:
        output_text.insert(tk.END, f"{row[0]} {row[1]}\n")

def books_borrowed_by_subscriber():
    def submit():
        query = """
            SELECT COUNT(*)
            FROM Emprunts
            WHERE idAbonne = ?
        """
        result = cur.execute(query, (subscriber_entry.get(),)).fetchone()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Nombre de livres empruntés : {result[0]}\n")
        borrowed_window.destroy()
    
    borrowed_window = tk.Toplevel(root)
    borrowed_window.title("Livres empruntés par Abonné")
    ttk.Label(borrowed_window, text="ID Abonné:").pack()
    subscriber_entry = ttk.Entry(borrowed_window)
    subscriber_entry.pack()
    ttk.Button(borrowed_window, text="Obtenir", command=submit).pack()

def total_borrowed_books():
    query = "SELECT COUNT(*) FROM Emprunts"
    result = cur.execute(query).fetchone()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Total des livres empruntés : {result[0]}\n")

def check_book_status():
    def submit():
        query = """
            SELECT COUNT(*) 
            FROM Emprunts
            WHERE idLivre = ?
        """
        result = cur.execute(query, (book_entry.get(),)).fetchone()
        output_text.delete("1.0", tk.END)
        if result[0] == 0:
            output_text.insert(tk.END, "Le livre est disponible.\n")
        else:
            output_text.insert(tk.END, "Le livre est emprunté.\n")
        status_window.destroy()
    
    status_window = tk.Toplevel(root)
    status_window.title("Vérifier statut Livre")
    ttk.Label(status_window, text="ID Livre:").pack()
    book_entry = ttk.Entry(status_window)
    book_entry.pack()
    ttk.Button(status_window, text="Vérifier", command=submit).pack()

# Update Buttons to include new actions
buttons.extend([
    ("Ajouter Emprunt", add_loan),
    ("Supprimer Emprunt", remove_loan),
    ("Informations Livre par Titre", book_info_by_title),
    ("Livres par Année", books_by_year),
    ("Livres par Auteur", books_by_author),
    ("Emprunts par Abonné", loans_by_subscriber),
    ("Total Livres", total_books),
    ("Noms des Abonnés", subscribers_names),
    ("Livres empruntés par Abonné", books_borrowed_by_subscriber),
    ("Total Livres empruntés", total_borrowed_books),
    ("Vérifier statut Livre", check_book_status)
])

# Buttons Frame - Use grid layout instead of pack
buttons_frame = ttk.Frame(frame)
buttons_frame.pack(fill="x", pady=10)

# Create the buttons with grid placement
buttons = [
    ("Lister Livres", list_books),
    ("Lister Auteurs", list_authors),
    ("Lister Abonnés", list_subscribers),
    ("Lister Emprunts", list_loans),
    ("Ajouter Auteur", add_author),
    ("Ajouter Livre", add_book),
    ("Ajouter Abonné", add_subscriber),
    ("Ajouter Emprunt", add_loan),
    ("Supprimer Emprunt", remove_loan),
    ("Informations Livre par Titre", book_info_by_title),
    ("Livres par Année", books_by_year),
    ("Livres par Auteur", books_by_author),
    ("Emprunts par Abonné", loans_by_subscriber),
    ("Total Livres", total_books),
    ("Noms des Abonnés", subscribers_names),
    ("Livres empruntés par Abonné", books_borrowed_by_subscriber),
    ("Total Livres empruntés", total_borrowed_books),
    ("Vérifier statut Livre", check_book_status),
    ("Quitter", root.quit)
]

# Place each button on a new line, 4 buttons per row (can adjust the number of columns as needed)
num_columns = 4
for i, (text, command) in enumerate(buttons):
    row = i // num_columns  # Determine the row number
    column = i % num_columns  # Determine the column number
    btn = ttk.Button(buttons_frame, text=text, command=command)
    btn.grid(row=row, column=column, padx=5, pady=5)

# Optionally, you can set column and row weights to make sure buttons stretch properly
for col in range(num_columns):
    buttons_frame.grid_columnconfigure(col, weight=1)


# Initialize tables
create_tables()

# Run the application
root.mainloop()
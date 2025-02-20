import os

def generer_code_html(dico, folder_path="C:\\Users\\eliha\\vsc\\cove\\html", filename="page.html"):
    # Vérifie si le dossier existe, sinon crée-le
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Crée le chemin complet du fichier
    file_path = os.path.join(folder_path, filename)
    
    # Ouvre le fichier en mode écriture
    with open(file_path, "w") as f:
        # Génération de la structure de base HTML
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title> Page générée en python </title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1> Articles en stock </h1>\n")
        f.write("<table>\n")
        
        # Boucle sur le dictionnaire pour générer les lignes du tableau
        for article, quantite in dico.items():
            f.write(f"<tr><td>{article}</td><td>{quantite}</td></tr>\n")
        
        # Fin du tableau et du reste de la page HTML
        f.write("</table>\n")
        f.write("</body>\n")
        f.write("</html>\n")
    
    print(f"Le code HTML a été écrit dans le fichier {file_path}")

# Exemple de dictionnaire avec des articles et leurs quantités
dico_articles = {
    "Article 1": 10,
    "Article 2": 5,
    "Article 3": 20,
    "Article 4": 15
}

# Appel de la fonction pour générer et écrire le code HTML dans un fichier dans le dossier spécifié
generer_code_html(dico_articles)

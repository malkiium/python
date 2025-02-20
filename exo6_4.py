def generer_code_html(dico):
    # Génération de la structure de base HTML
    print("<html>")
    print("<head>")
    print("<title> Page générée en python </title>")
    print("</head>")
    print("<body>")
    print("<h1> Articles en stock </h1>")
    print("<table>")
    
    # Boucle sur le dictionnaire pour générer les lignes du tableau
    for article, quantite in dico.items():
        print(f"<tr><td>{article}</td><td>{quantite}</td></tr>")
    
    # Fin du tableau et du reste de la page HTML
    print("</table>")
    print("</body>")
    print("</html>")

# Exemple de dictionnaire avec des articles et leurs quantités
dico_articles = {
    "Article 1": 10,
    "Article 2": 5,
    "Article 3": 20,
    "Article 4": 15
}

# Appel de la fonction pour générer et afficher le code HTML
generer_code_html(dico_articles)

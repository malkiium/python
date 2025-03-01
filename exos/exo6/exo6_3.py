dico = {
    "bonjour": "hello",
    "au revoir": "goodbye",
    "chien": "dog",
    "chat": "cat",
    "école": "school",
    "aide": "help"
}

def traduction():
    while True:
        ajtmot = input("Entrez un mot et sa traduction (format: mot:traduction) ou 'fin' pour arrêter: ").strip()
        
        if ajtmot.lower() == "fin":
            print("Fin du programme.")
            break
        
        if ":" not in ajtmot:
            print("Format invalide. Veuillez entrer sous la forme 'mot:traduction'.")
            continue

        mot, trad = ajtmot.split(":")
        
        if mot in dico:
            print(f"Le mot '{mot}' existe déjà dans le dictionnaire avec la traduction '{dico[mot]}'.")
        else:
            dico[mot] = trad
            print(f"Le mot '{mot}' a été ajouté avec la traduction '{trad}'.")
    dico_sorted = sorted(dico.items())
    print(dico_sorted)
    print()

    invdico = {v: k for k, v in dico.items()}
    
    while True:
        mot_a_retirer = input("Entrez un mot à retirer du dictionnaire ou 'fin' pour arrêter: ").strip()
        if mot_a_retirer.lower() == "fin":
            print("Fin du programme.")
            break
        if mot_a_retirer in invdico:
            del invdico[mot_a_retirer]
            print(f"Le mot '{mot_a_retirer}' a été retiré du dictionnaire.")
    print(invdico)

traduction()

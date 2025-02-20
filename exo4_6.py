def cartes():
    cartestype = ["coeur", "carreau", "pique", "trefle"]
    cartesvaleur = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
    tjeu = []

    for i in range(len(cartestype)):
        for j in range(len(cartesvaleur)):
            tjeu.append((cartesvaleur[j], cartestype[i]))

    return tjeu

def convertir_valeur(valeur):
    if valeur == "valet":
        return 11
    elif valeur == "dame":
        return 12
    elif valeur == "roi":
        return 13
    return valeur

def jeu(cartes: list):
    joeur1 = input("Joueur 1: ")
    jeujoeur1 = []
    joeur2 = input("Joueur 2: ")
    jeujoeur2 = []
    
    import random
    jeujoeur1.extend(random.sample(cartes, 5))
    jeujoeur2.extend(random.sample(cartes, 5))
    
    print()
    print(joeur1, jeujoeur1)
    print(joeur2, jeujoeur2)
    print()

    cartetypechoisit = input("Type de carte: ")

    biggestj1 = None
    biggestj2 = None
    for i in range(5):
        if jeujoeur1[i][1] == cartetypechoisit:
            if biggestj1 is None or convertir_valeur(jeujoeur1[i][0]) > convertir_valeur(biggestj1[0]):
                biggestj1 = (jeujoeur1[i])
        if jeujoeur2[i][1] == cartetypechoisit:
            if biggestj2 is None or convertir_valeur(jeujoeur2[i][0]) > convertir_valeur(biggestj2[0]):
                biggestj2 = (jeujoeur2[i])

    if convertir_valeur(biggestj2[0]) > convertir_valeur(biggestj1[0]):
        print(joeur2, "a la plus grande carte :", biggestj2)
    else:
        print(joeur1, "a la plus grande carte :", biggestj1)


cartes = cartes()
jeu(cartes)
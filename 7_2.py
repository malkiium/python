import random

# Fonction pour charger les mots à partir du fichier baseMots.txt
def charger_mots():
    mots_par_longueur = []
    
    try:
        with open("baseMots.txt", "r") as f:
            for line in f:
                mots = line.strip().split(",")
                longueur_mots = len(mots[0])  # On suppose que tous les mots ont la même longueur sur une ligne
                if len(mots_par_longueur) <= longueur_mots:
                    mots_par_longueur.extend([[]] * (longueur_mots - len(mots_par_longueur) + 1))
                mots_par_longueur[longueur_mots].extend(mots)
                
    except FileNotFoundError:
        print("Le fichier baseMots.txt n'a pas été trouvé.")
        return []
    
    return mots_par_longueur

# Fonction pour gérer le jeu du pendu
def jouer(mot_a_trouver):
    erreurs = 0
    lettres_proposees = set()
    mot_affiche = ["_"] * len(mot_a_trouver)
    
    while erreurs < 4:
        print(f"Mot à deviner: {' '.join(mot_affiche)}")
        print(f"Erreurs: {erreurs}/4")
        print(f"Lettres proposées: {', '.join(sorted(lettres_proposees))}")
        
        lettre = input("Proposez une lettre: ").lower()
        
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        
        if lettre in lettres_proposees:
            print(f"Vous avez déjà proposé la lettre '{lettre}'. Essayez une autre lettre.")
            continue
        
        lettres_proposees.add(lettre)
        
        if lettre in mot_a_trouver:
            print(f"La lettre '{lettre}' est dans le mot !")
            for i in range(len(mot_a_trouver)):
                if mot_a_trouver[i] == lettre:
                    mot_affiche[i] = lettre
        else:
            erreurs += 1
            print(f"La lettre '{lettre}' n'est pas dans le mot.")
        
        if "_" not in mot_affiche:
            print(f"Félicitations, vous avez trouvé le mot: {''.join(mot_affiche)}")
            return
        
    print(f"Vous avez perdu ! Le mot était: {mot_a_trouver}")

# Fonction pour initialiser le jeu et choisir un mot au hasard
def initialiser():
    mots_par_longueur = charger_mots()
    
    if not mots_par_longueur:
        return
    
    # Demander à l'utilisateur la longueur du mot à deviner
    while True:
        try:
            longueur = int(input("Choisissez la longueur des mots à deviner (par exemple, 5 pour des mots de 5 lettres): "))
            if longueur >= len(mots_par_longueur):
                print("Aucune liste disponible pour cette longueur, veuillez choisir une autre longueur.")
                continue
            mots_disponibles = mots_par_longueur[longueur]
            if mots_disponibles:
                break
            else:
                print(f"Aucun mot disponible de longueur {longueur}. Essayez une autre longueur.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Choisir un mot au hasard parmi les mots disponibles
    mot_choisi = random.choice(mots_disponibles)
    print(f"\nLe jeu commence avec un mot de {longueur} lettres.")
    
    # Lancer la partie de pendu
    jouer(mot_choisi)

# Lancer le jeu
if __name__ == "__main__":
    initialiser()

coul1, coul2 = ["violet", "bleu", "rouge", "rose", "mauve"], ["marron", "vert", "jaune", "orange", "mauve"]

def afficherCouleurs(couleurs):
    for couleur in couleurs:
        print(couleur, end=" ")
    print()

afficherCouleurs(coul1)
afficherCouleurs(coul2)
print()

def dispo(couleur:str, couleurs:list):
    if couleur in couleurs:
        print(True)
        return True
    else:
        print(False)
        return False

dispo("rouge", coul1)
dispo("rouge", coul2)
print()


def enCommun(lst1:list, lst2:list):
    for i in lst1:
        for j in lst2:
            if i == j:
                print(i, "est en commun", end=" ")

enCommun(coul1, coul2)
print()
print()

def ajouter(couleur:str, couleurs:list):
    couleurs.append(couleur)
    print("ajour de :", couleur, ", a la list :",couleurs)

ajouter("noir", coul1)
print()

def collection(couleur1:list, couleur2:list):
    enscouleur = couleur1.copy()
    for i in couleur2:
        if i not in enscouleur:
            enscouleur.append(i)
    print("couleurs totale:", enscouleur)

collection(coul1, coul2)
print()

def diff(co1:list, co2:list):
    diff = []
    for i in co1:
        if i not in co2:
            diff.append(i)
    print("couleurs qui sont dans le 1er magazin mais pas le 2nd:", diff)

diff(coul1, coul2)
print()
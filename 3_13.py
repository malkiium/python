import random
from statistics import correlation

couleurs = ['R', 'G', 'B', 'V', 'J', 'M']



def creer_combinaison():
    tab = [''] * 6

    for i in range(len(tab)):
        tab[i] = random.choice(couleurs)
    return tab

def evaluer_proposition(tab: list, prop: list):
    correct = 0
    bad_place = 0

    temp_tab = tab.copy()
    temp_prop = prop.copy()

    for i in range(len(tab)):
        if prop[i] == tab[i]:
            correct += 1
            temp_tab[i] = None
            temp_prop[i] = None

    for couleur in temp_prop:
        if couleur is not None and couleur in temp_tab:
            bad_place += 1
            temp_tab[temp_tab.index(couleur)] = None

    print(correct, bad_place)
    return correct, bad_place


def lire_proposition():
    prop = list(input("------------------ \n"))
    if len(prop) == 6:
        for i in range(6):
            if prop[i] not in couleurs:
                print("incorrect. veuilleur réessayer.")
                lire_proposition()
            else:
                return prop
    else:
        print("incorrect. veuilleur réessayer.")
        lire_proposition()

def jouer():
    tries = 0
    tab = creer_combinaison()

    while True:
        prop = lire_proposition()
        tries += 1
        correct, bad_place = evaluer_proposition(tab, prop)

        if correct == 6:
            print("Bien jouer ! vous avec trouver en:", tries, "essais.")
            return 1

jouer()
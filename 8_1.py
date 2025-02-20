"""Ecrire un programme permettant de saisir un entier. Si l’utilisateur saisit autre chose qu’un entier,
afficher un message d’erreur en gérant l’exception ValueError. Le programme doit boucler
jusqu’à ce que l’utilisateur saisisse bien un entier."""


def saisir_entier():
    try:
        entier = int(input("Saisissez un entier: "))
    except ValueError:
        print("Vous devez saisir un entier.")
        saisir_entier()

saisir_entier()
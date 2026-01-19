# Écrire un programme, permettant d’afficher à l’écran ligne par ligne la table de multiplication des
# entiers de 1 à 10.
# On ne cherchera pas ici à stocker la table en mémoire mais juste à l’afficher.
# NB : on pourra utiliser la fonction str pour convertir un entier en chaîne de caractères et l’opérateur
# + pour concaténer des chaînes de caractères.




for n in range(1,11):
    table, nmb = "", 0
    for y in range(1,11):
        nmb = n*y
        table += str(nmb) + str(" ")
    print(table)
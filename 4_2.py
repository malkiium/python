def trouver_indice(element, tuple_entiers):
    try:
        indice = tuple_entiers.index(element)
    except ValueError:
        indice = -1

    print(f"Élément à rechercher: {element_a_rechercher}")
    print(f"Tuple d'entiers: {tuple_d_entiers}")
    print(f"Résultat de la recherche: {indice}")
    return indice

element_a_rechercher = 9
tuple_d_entiers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

resultat = trouver_indice(element_a_rechercher, tuple_d_entiers)
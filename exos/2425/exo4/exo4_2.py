def indiceOccurenceElem(element, tuple_entiers):
    try:
        indice = tuple_entiers.index(element)
    except ValueError:
        indice = -1

    print(f"Élément à rechercher: {element}")
    print(f"Tuple d'entiers: {tuple_entiers}")
    print(f"Résultat de la recherche: {indice}")
    print()
    return indice

tup1 = (1,5,4,10)
assert indiceOccurenceElem(5,tup1) == 1
assert indiceOccurenceElem(12,tup1) == -1
assert indiceOccurenceElem(10,tup1) == 3
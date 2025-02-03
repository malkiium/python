def ligne_pleine(car, nb):
    return car * nb


def ligne_creuse(car, nb):
    if nb == 1:
        return car
    return car + ' ' * (nb - 2) + car


def rectangle_plein(car, longueur, largeur):
    for _ in range(largeur):
        print(ligne_pleine(car, longueur))


def rectangle_creux(car, longueur, largeur):
    if largeur == 1:
        print(ligne_pleine(car, longueur))
    else:
        print(ligne_pleine(car, longueur))
        for _ in range(largeur - 2):
            print(ligne_creuse(car, longueur))
        print(ligne_pleine(car, longueur))


def triangle_plein(car, hauteur):
    for i in range(1, hauteur + 1):
        print(ligne_pleine(car, i))


def triangle_creux(car, hauteur):
    if hauteur == 1:
        print(car)
        return
    print(car)
    for i in range(2, hauteur):
        print(ligne_creuse(car, i))
    print(ligne_pleine(car, hauteur))



wha = int(input("what do you want ? : \n 1 triangle \n 2 hollow triangle \n 3 rect \n 4 hollow rect \n"))

if wha == 1:
    car = str(input("what type of char ? : "))
    hauteur = int(input("What height for the triangle? : "))
    triangle_plein(car, hauteur)
elif wha == 2:
    car = str(input("what type of char ? : "))
    hauteur = int(input("What height for the hollow triangle? : "))
    triangle_creux(car, hauteur)
elif wha == 3:
    car = str(input("what type of char ? : "))
    longueur = int(input("What length for the rectangle? : "))
    largeur = int(input("What height for the rectangle? : "))
    rectangle_plein(car, longueur, largeur)
elif wha == 4:
    car = str(input("what type of char ? : "))
    longueur = int(input("What length for the hollow rectangle? : "))
    largeur = int(input("What height for the hollow rectangle? : "))
    rectangle_creux(car, longueur, largeur)
else:
    print("Invalid option.")
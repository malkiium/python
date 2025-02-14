x_min = -150
x_max = 150

def limite_amplitude(val:list, x_min:int, x_max:int):
    if val > x_max:
        val = x_max
    elif val < x_min:
        val = x_min
    print(val)
    return val

def ecrete(tab:list, x_min:int, x_max:int):
    for i in range(len(tab)):
        if tab[i]>x_max:
            tab[i] = x_max
        elif tab[i]<x_min:
            tab[i] = x_min
    print(tab)
    return tab

assert limite_amplitude(50,-150,150) == 50
assert limite_amplitude(-200,-150,150) == -150
assert limite_amplitude(200,-150,150) == 150

assert ecrete([],-150,150) == []

valeurs = [30,5,-2,15,12]
attendu = [30,5,-2,15,12]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur, la fonction a renvoyé {resultat}"

valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur, la fonction a renvoyé {resultat}"
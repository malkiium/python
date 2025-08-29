def divPar2(nb):
    original = nb  # Store the original number
    count = 0
    while nb % 2 == 0:
        nb //= 2
        count += 1
    oui = [nb, count]
    divParImpair(oui, original)
    return [nb, count]

def divParImpair(tab: list, original):
    nb = tab[0]
    div = 3
    factors = []
    while nb > 1:
        if nb % div == 0:
            nb //= div
            factors.append(div)
        else:
            div += 2
    new_tab = tab + factors
    affichage(original, new_tab)
    return new_tab

def affichage(n: int, tab: list):

    count2 = tab[1] if len(tab) > 1 else 0
    odd_factors = tab[2:] if len(tab) > 2 else []

    factors = ([2] * count2) + odd_factors

    if len(factors) == 1 and factors[0] == n:
        print(f"{n} est un nombre premier !")
    else:
        factor_str = " * ".join(map(str, factors))
        print(f"{n} = {factor_str}")





affichage(46, [23, 1, 23])
affichage(24, [3, 3, 3])
affichage(7, [7, 0, 7])
affichage(125, [125, 0, 5, 5, 5])
affichage(360, [45, 3, 3, 3, 5])

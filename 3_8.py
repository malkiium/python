def divPar2(nb):
    count = 0
    while nb % 2 == 0:
        nb //= 2
        count += 1
    oui = [nb, count]
    divParImpair(oui)
    return [nb, count]

def divParImpair(tab:list):
    nb = tab[0]  # Extract the number to be factored
    div = 3
    factors = []

    while nb > 1:
        if nb % div == 0:
            nb //= div
            factors.append(div)
            div = 3
        else:
            div += 2
    affichage(tab[0], factors)
    return tab + factors

def affichage(n: int, tab: list):
    # Clean the list to remove 1s and 0s from the factorization
    cleaned_tab = [x for x in tab if x > 1]

    if len(cleaned_tab) == 1 and cleaned_tab[0] == n:
        print(f"{n} est un nombre premier.")
    else:
        # Format the factors as a multiplication string
        mults = " * ".join(map(str, cleaned_tab))
        print(f"{n} = {mults}")




assert divPar2(46) == [23, 1]
assert divPar2(24) == [3, 3]
assert divPar2(7) == [7, 0]
assert divPar2(125) == [125,0]
assert divPar2(360) == [45,3]

assert divParImpair([23,1]) == [23,1,23]
assert divParImpair([3,3]) == [3,3,3]
assert divParImpair([7,0]) == [7,0,7]
assert divParImpair([125,0]) == [125,0,5,5,5]
assert divParImpair([45,3]) == [45,3,3,3,5]
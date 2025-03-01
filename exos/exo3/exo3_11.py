import random

tab = []
deb = 0
fin = len(tab)

def rechercheDichotomie(elem, deb:int, fin:int, tab:list):
    if deb > fin:
        return False

    milieux = (deb+fin)//2

    if elem == tab[milieux]:
        return True
    elif deb == fin:
        if elem == tab[deb]:
            return True
        else:
            return False
    elif elem < tab[milieux]:
        print(elem, deb, milieux-1)
        return rechercheDichotomie(elem, deb, milieux-1, tab)
    else:
        print(elem, deb, milieux-1)
        return rechercheDichotomie(elem, milieux+1, fin, tab)

tab = [0]*random.randint(0, 100)
for i in range(len(tab)):
    tab[i] = random.randint(0, 100)
tab.sort()
print(len(tab), tab)
element = 7
resultat = rechercheDichotomie(element, 0, len(tab) - 1, tab)

if resultat:
    print(f"L'élément {element} est trouvé dans le tableau.")
else:
    print(f"L'élément {element} n'est pas dans le tableau.")
def construireTabCoeff(tab: list, n: int):
    for i in range(len(tab), n):
        ligne = [1]
        for j in range(1, i):
            ligne.append(tab[i - 1][j - 1] + tab[i - 1][j])
        ligne.append(1)
        tab.append(ligne)
    return tab


def affichage(tab: list):

    for ligne in tab:
        print(" ".join(map(str, ligne)))


tab =[[1], [1, 1]]
construireTabCoeff(tab, 23)
affichage(tab)
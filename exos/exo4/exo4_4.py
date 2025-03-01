def jouable(jeux:list, nb_joueurs:int):
    jeux_possible = []
    for jeu in jeux:
        if jeu[1] <= nb_joueurs <= jeu[2]:
            jeux_possible.append(jeu[0])
    print(jeux_possible, "jeux possible \n")
    return jeux_possible


tab = []
tab.append(('dark castle',3,6))
tab.append(('lucky numbers',2,4))
tab.append(('lueurs',2,4))

assert jouable(tab,2)==['lucky numbers','lueurs']
assert jouable(tab,5)==['dark castle']
assert jouable(tab,1)==[]
assert jouable(tab,4)==['dark castle','lucky numbers','lueurs']
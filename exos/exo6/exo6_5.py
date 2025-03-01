def ajouter(dico, clef):
    if clef in dico:
        dico[clef] += 1
    else:
        dico[clef] = 1

def decomposer(chaine):
    dico = {}
    for lettre in chaine:
        ajouter(dico, lettre)
    print(dico)
    return dico

# Tests avec des assertions
assert decomposer("bonjour") == {'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}
assert decomposer("abcd") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
assert decomposer("aa bb c") == {'a': 2, ' ': 2, 'b': 2, 'c': 1}
assert decomposer("aaa") == {'a': 3}
assert decomposer("") == {}

print("Tous les tests sont passés ! ✅")

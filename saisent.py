intermediar = 0

def saisirEntier():
    premier = input("saisisez un entier : ")
    premier = int(premier)
    if premier.is_integer():
        saisieEntierSuivant(premier)
    else:
        print("ceci n'est pas un entier")
        saisirEntier()

def saisieEntierSuivant(premier):
    second = input("saisisez un second entier : ")
    second = int(second)
    if second.is_integer() and second > premier:
        somme(premier, second)
    else:
        print("ceci n'est pas un entier, ou il est plus petit que le 1er.")
        saisieEntierSuivant(premier)

def somme(premier, second):
    global intermediar
    for i in range(premier, second+1):
        intermediar += premier
        premier += 1
    print(intermediar)



saisirEntier()
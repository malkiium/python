tries = 0
lis = []

def saisie(numbs : list, tries : int) -> list:
    numbs2 = []
    while tries < 4:
        newnumb = input("entrer un chiffre, celui que vous voullez : ")
        if len(newnumb) != 1 or not newnumb.isdecimal():
            print("please retry.")
        else:
            tries +=1
            numbs.append(newnumb)
            print(tries)
    
    for i in range(len(numbs)):
        numbs[i] = float(numbs[i])
        numbs2.append(numbs[i] * 2)

    print("l'originale :", numbs, "et son double :", numbs2)


saisie(lis, tries)
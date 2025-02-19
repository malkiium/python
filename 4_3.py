lst = []

def listToTuple():
    global lst
    try:
        nmb = int(input("Entrez un nombre: "))
        if nmb >= 0:
            lst.append(nmb)
            listToTuple()
        else:
            lst = tuple(lst)
            print("\n", lst)
            return lst
    except ValueError:
        print("Vous devez entrer un nombre entier.")
        listToTuple()

listToTuple()
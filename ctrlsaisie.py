totsai = 1
nmb = ""

def ses():
    global totsai, nmb

    while totsai<5:
        print("choisiser votre", totsai, end=" ")
        choix = input("chiffre : ")

        if choix.isdigit() and len(choix) == 1:
            totsai += 1
            nmb += choix
            print("le nombe validée est :", choix)
        elif len(choix) > 1:
            print("le chiffre comprend 2 nombre. veuillez reessayer avec un seul.")
        else:
            print("ceci n'est pas pas un numero. veuillez réessayer en relancant le programe.", end="\n")

    print()
    print("le nombre formée est :", nmb, "et sont double est :", int(nmb)*2)

ses()
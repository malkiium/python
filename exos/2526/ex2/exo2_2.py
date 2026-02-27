def saisir_entier(mess: int) -> function :
    num = input(mess)

    if not num.isdigit():
        print("not a number. please retry.")
        return(saisir_entier(mess))
    else:
        return(saisir_entier_sup(mess, num))

def saisir_entier_sup (mess : int, inf : int) -> list:
    num = input(mess)
    interv = []

    if not num.isdigit():
        print("not a number. please retry.")
        return(saisir_entier_sup(mess, inf))
    elif num < inf:
        print("the second number is smaller than the first one. please retry.")
        return(saisir_entier_sup(mess, inf))
    else:
        num, inf = int(num), int(inf)
        for i in range(num-inf):
            interv.append(i+inf)
        interv.append(num)
        print(interv)
        return interv

saisir_entier("veuillez entrer un chiffre :")
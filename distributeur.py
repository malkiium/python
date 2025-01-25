billets_amt = 20
billets_prix = 5
pieces_amt = 100
piece_prix = 1
billets_rendu = 0
pieces_rendu = 0

def distrib():
    global billets_rendu, pieces_rendu, pieces_amt, billets_amt, piece_prix, billets_prix

    while billets_amt or pieces_amt > 0:
        print()
        print("il reste : " + str(billets_amt) + " x " + str(billets_prix) + "€ billets. et : " + str(pieces_amt) + " x " + str(piece_prix) + "€ pieces.")
        prix = int(input("quel est le prix de l'item ? : "))
        donner = int(input("monter donner a la machine ? :"))

        while donner < prix:
            insf = int(input("le montant est insufisant. donner plus : "))
            donner = int((insf+donner))
        if donner > prix:
            a_rendre = donner - prix
            print("le montant a rendre : " + str(a_rendre))

            if a_rendre > ((billets_prix*billets_amt) + (pieces_amt*piece_prix)):
                print("la machine ne peut pas vous redoner le montant exacte. elle vous redonne ce que vous lui avez donner.")
                print("la machine vous a rendu :" + str(donner))
                donner = 0
                a_rendre = 0
                distrib()


        while a_rendre > 0:
            if a_rendre>= billets_prix and billets_amt > 0:
                a_rendre -= billets_prix
                billets_amt -= 1
                billets_rendu += 1
            elif pieces_amt > 0:
                a_rendre -= 1
                pieces_amt -= 1
                pieces_rendu += 1

        print("montant rendu : " + str(billets_rendu) + " x " + str(billets_prix) + "billets. et, " + str(pieces_rendu) + " x " + str(piece_prix) + "pieces")
    print("il n'y a plus d'argent dans la caisse.")

distrib()
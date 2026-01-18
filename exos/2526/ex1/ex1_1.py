# Sachant que la somme : 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 – 1/15 + … tend vers π/4, écrire un
# programme permettant de calculer une valeur approchée de π. On pourra écrire deux versions :
# selon que l’on demande à l’utilisateur le nombre de termes souhaités, ou la valeur du dénominateur
# du dernier terme pris en compte dans le calcul.

positive = False
numb = 3
currentnumb = 1
prevnumb = 1

comptageshouaiter = int(input(
                                "quelle facon voullez vous faire ? \n" \
                                " 1 = le nombre de termes souhaités \n" \
                                " 2 = la valeur du dénominateur (doit etre un nombre inpaire, sinon il sera aroundit) \n" \
                                " : " ))

if comptageshouaiter == 1:
    denumv = int(input("quel est le nombre de termes souhaités? :"))
    for n in range(denumv):
        if positive:
            currentnumb += (1/numb)
        else:
            currentnumb -= (1/numb)
        
        print("pi de 1/", numb, "=", currentnumb*4)
        positive = not positive
        numb += 2

elif comptageshouaiter == 2:
    denumv = int(input("quel est le 1/x shouaiter ? :"))
    denumv /= 2
    denumv = int(denumv)
    for n in range(denumv):
        if positive:
            currentnumb += (1/numb)
        else:
            currentnumb -= (1/numb)
        
        print("pi de 1/", numb, "=", currentnumb*4)
        positive = not positive
        numb += 2

else:
    print("incorrect. veuillez réessayer")
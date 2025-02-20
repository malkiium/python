"""Ecrire un programme permettant de saisir deux entiers : une distance à parcourir (en km) et une
vitesse moyenne (en km/h). Pour chaque saisie, on adoptera le même comportement que dans
l’exercice précédent via une fonction prenant en paramètre le message d’invite à afficher.
Dans un deuxième temps, le programme doit calculer le nombre d’heures nécessaires pour parcourir
la distance spécifiée à la vitesse spécifiée. Si la vitesse est égale à 0 alors en gérant l’exception
ZeroDivisionError, le programme doit afficher un message d’erreur. Sinon le programme
doit afficher la durée obtenue.
"""

def vtsEtDst():
    try:
        vitesse = int(input("Saisissez une vitesse moyenne (en km/h): "))
        distance = int(input("Saisissez une distance à parcourir (en km): "))
    except ValueError:
        print("Vous devez saisir un entier.")
    except ZeroDivisionError:
        print("La vitesse ne peut pas être nulle.")
    

    hours = distance / vitesse
    heures_entieres = int(hours)
    minutes = int((hours - heures_entieres) * 60)

    print(f"⏳ La durée nécessaire pour parcourir {distance} km à {vitesse} km/h est de {heures_entieres}h{minutes:02d}.")


vtsEtDst()
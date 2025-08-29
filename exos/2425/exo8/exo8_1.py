def saisir_entier():
    try:
        entier = int(input("Saisissez un entier: "))
    except ValueError:
        print("Vous devez saisir un entier.")
        saisir_entier()

saisir_entier()
def saisie():
    nmb = ""
    for i in range(4):
        while True:
            chiffre = input(f"Entrez le chiffre {i+1} : ")
            if len(chiffre) == 1 and chiffre.isdigit():
                print(f"Validé : {chiffre}")
                nmb += chiffre
                break
            else:
                print("Erreur : Veuillez entrer un seul chiffre (0-9).")
    
    nombre = int(nmb)
    print(f"\nNombre saisi : {nombre}")
    print(f"Son double : {nombre * 2}")

saisie()

# Écrire un programme qui affiche à l’écran un damier composé des lettres X et O. La taille du coté
# du damier sera demandée à l’utilisateur. Voici le résultat obtenu avec un coté de taille 8 :







taille = int(input("quelle taille pour le damier ? : "))
for curln in range(taille):
    line = ""
    if curln%2 == 0:
        for aded in range(taille):
            if aded%2 == 1:
                line += "O "
            else:
                line+="X "
    else:
        for aded in range(taille):
            if aded%2 == 1:
                line += "X "
            else:
                line+="O "
    print(line)
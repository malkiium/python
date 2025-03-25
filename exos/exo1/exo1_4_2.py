taille = int(input("quelle est la taille du damier ? : "))

for i in range(taille):
    for j in range(taille):
        if (i+j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
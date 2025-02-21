def table(n:int):
    for i in range(1, 11):
        print()
        nmb = n*i
        for j in range(1, 11):
            print(nmb*j, end=" ")

nmb = int(input("Entrez un nombre: "))
table(nmb)
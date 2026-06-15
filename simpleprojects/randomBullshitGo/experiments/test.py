ll = [1, 2, 3, 4, 5]

ll2 = ll.copy()

ll2[0] = 100
print(ll)
print(ll2)

ll3 = ll2.copy()
ll3.sort()
print(ll3)


matrix = [
          ['G', 'G', 'G', '', ''],
          ['F', 'F', '', '', ''],
          ['F', 'F', '', 'G', 'G'],
          ['', '', '', '', ''],
          ['G', 'G', 'G', 'G', 'G']
          ]

for i in range(len(matrix)):
    pers = {"garcons": 0, "filles": 0, "vide": 0}
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'G':
            pers["garcons"] += 1
        elif matrix[i][j] == 'F':
            pers["filles"] += 1
        else:
            pers["vide"] += 1
    print(pers)


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'G':
            print("G", end=" ")
        elif matrix[i][j] == 'F':
            print("F", end=" ")
        else:
            print("-", end=" ")
    print()

print("\n\n\n\n")

matr = [
    ["name", "alice"],
    ["age", 20],
]
for i in range(len(matr)):
        print(matr[i][0], end=": ")
        print(matr[i][1], end=" ")
        print()

print()

allistair = {
    "name": "Allistair",
}

allistair["age"] = 19

allistair["pays"] = "France"
allistair["ville"] = "chauvigny"
allistair["ville"] = "paris"

for key, value in allistair.items():
    print(key, ":", value)

del allistair["ville"]

allistair["ville"] = "paris"
for key, value in allistair.items():
    print(key, ":", value)











print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")












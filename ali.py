print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




lieste = [x for x in range(1, 100) if x % 2 == 0 and x % 3 == 0 and x % 5 == 0 ]
print(lieste)
print("\n\n\n")

def triple(x):
    return x*3

tripleList = list(map(triple, lieste))
print(tripleList)
print("\n\n\n")


liste1 = [1, 2, 3, 4, 5]
liste2 = [1, 2, 3, 4, 5]
liste3 = liste1



print(liste1 == liste2)
print(liste1 is liste2)
print(liste1 == liste3)
print(liste1 is liste3)
print("\n\n\n")

mot = "blyyyyyyyat"

print(mot.find("y"))
print(mot.count("y"))
print(mot.find("Z"))
print(mot.index("y"))

print("\n\n\n")


liste1.extend(liste2)
print(liste1)
print("\n\n\n")
liste1.insert(6, 69)
print(liste1)
print("\n\n\n")
liste1.remove(69)
print(liste1)
liste1.clear()
print(liste1)
liste1.extend(liste2)
print(liste1)
liste1.reverse()
print(liste1)
liste1 = liste1[::-1]
print(liste1)
liste1.insert(4,69)
liste1.insert(2,70)
print(liste1)
liste1 = liste1[::-2]
print(liste1)
listeuwu = list(sorted(liste1))
print(listeuwu)




insta = ["insta", 245]
allistaire = ["telegram", insta, "tiktok"]
tuple1 = tuple(allistaire)
allistaire.append("snapchat")
insta.append("instagram")
print(tuple1)


print("\n\n\n\n\n\n")

E = {1, 2, 3, 4, 5}
F = {4, 5, 6, 7, 8}
print(E & F)  # Intersection
print(E - F)
print(F - E)  # Difference
print(E | F)  # Union
print(E ^ F)  # Symmetric difference
print((E | F) - (E & F))  # Union minus intersection

print("\n\n\n\n\n\n")

alli = {
    "name": "Ali",
    "age": 20,
    "city": "Paris",
    "hobbies": ["reading", "gaming", "coding"],
}

alli["salaire"] = 2000
alli["age"] = 19
del alli["age"]



for key, value in alli.items():
    print(f"{key}: {value}")
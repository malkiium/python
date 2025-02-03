ll = [x for x in range(0,7)]
print("\n creation liste", ll)

ll.append(45) # ajoute a la fin
print("\n append", ll)

ll.append(23)
print("\n append", ll)

ll.extend([56,43]) # ajoute a la liste ce bout de liste
print("\n extend", ll)

ll.insert(6, 5) # ajout 5 avec le chiffre 6 dans la liste
print("\n insert", ll)

# copy only makes a double of the list, but the information of the list has the same reference.
# change 1 lists contenant and it changes the other
ll2 = ll.copy()

ll2.sort() #organise la liste de facon croissance SUPER UTILE
print("\n sort", ll2)
print(ll) #permet de verif que ll a pas etait organiser

lltri = list(sorted(ll)) #permet de faire une liste triée dans une nouvelle liste, sans trier la liste originale
print("\n lltri", lltri)

ll2.reverse() #fait la liste... a l'envers.
print("\n reverse", ll2)

ll2.clear()
print("\n clear", ll2)

li2 = [a for a in range(0,5)]
print("\n li2", li2)
for i in range(len(li2)): #this needs a list with information INSIDE OF IT, empty list = no go
    li2[i] = 2**i
print("\n for loop with lists", li2)


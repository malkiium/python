def insere(nu:int, numbs:list):
    numbs.append(nu)
    numbs.sort()
    print(numbs)


exemple_1 = [1, 2, 4, 5]
insere(3, exemple_1)
assert exemple_1 == [1, 2, 3, 4, 5]

exemple_2 = [1, 2, 7, 12, 14, 25]
insere(7, exemple_2)
assert exemple_2 == [1, 2, 7, 7, 12, 14, 25]

exemple_3 = [2, 3, 4]
insere(1, exemple_3)
assert exemple_3 == [1, 2, 3, 4]

print("All tests passed! ✅")
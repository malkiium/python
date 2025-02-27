def enlever_redondances(l1: list):
    l1.sort()
    i = 0
    while i < len(l1) - 1:
        print(l1)
        if l1[i] == l1[i + 1]:
            del l1[i]
        else:
            i += 1


t = []
enlever_redondances(t)
assert t == [], "tableau obtenu :" + str(t)

t = [1, 2, 3]
enlever_redondances(t)
assert t == [1, 2, 3], "tableau obtenu :" + str(t)

t = [1, 1, 5, 8, 8, 8, 9, 9, 10]
enlever_redondances(t)
assert t == [1, 5, 8, 9, 10], "tableau obtenu :" + str(t)
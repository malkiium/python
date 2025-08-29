l1 = list(map(int, input("what numbers do you want ? ").split()))
l2 = []
l3 = []

for x in range(len(l1)):
    if l1[x]%2 == 0:
        l2.append(l1[x])
    else:
        l3.append(l1[x])

print(" evens :", l2, "\n odds :", l3)
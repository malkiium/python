u1, u2, nterm = 1, 1, int(input("combien d'itération?) : "))
for n in range(nterm):
    print("le", n+1, "terme =", u1)
    u1, u2 = u2, u1+u2
clientL = ["Jean", "Pierre", 19, "Le Havre"]
print("liste:")
print(f"nom : {clientL[0]}, prenom : {clientL[1]}, age : {clientL[2]}, ville : {clientL[3]}")
clientT = tuple(clientL)
print("tuple:")
print(f"nom : {clientT[0]}, prenom : {clientT[1]}, age : {clientT[2]}, ville : {clientT[3]}")
print()

print("pierre devient Ives")
print()

clientL[1] = "Ives"
print("liste:")
print(f"nom : {clientL[0]}, prenom : {clientL[1]}, age : {clientL[2]}, ville : {clientL[3]}")
print("tuple:")
print(f"nom : {clientT[0]}, prenom : {clientT[1]}, age : {clientT[2]}, ville : {clientT[3]}")

print("\n\n\n")

listedl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tupledl = tuple(listedl)
print("liste:")
print(listedl)
print("tuple:")
print(tupledl)

listedl[1][1] = 999
print("liste:")
print(listedl)
print("tuple:")
print(tupledl)

print("autrement dit. le tuple ne se modifie pas quand la liste est modifier. mais quand la liste de la liste est modifier. soit, cela arrive que au niveau N+2")
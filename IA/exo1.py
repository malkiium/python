liste = ["banane", "mangue", "maron"]
liste.append("chocolat")
liste[2] = "pouér"
print(len(liste))

dict = {"red": "rouge", "yellow": "jaune", "blue": "bleu"}

print(dict.keys())
print(dict.values())

# x = int(input("tu veut quoi ? : "))
# if x%2 == 0:
#    print("pair")
# else:
#    print("impaire")


def nbprm(a: int):
    other = False
    i = a - 1
    while not other and i > 1:
        if a % i == 0:
            other = True
            return other
        else:
            i -= 1
    return other


print(nbprm(13))

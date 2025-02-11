voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

def dentiste(mts:str):
    result = ""

    for lettre in mts:
        if lettre in voyelles:
            result += lettre

    print(result)
    return result



assert dentiste("j'ai mal") == 'aia'
assert dentiste("il fait chaud") == 'iaiau'
assert dentiste("ca tire") == 'aie'
assert dentiste("") == ''
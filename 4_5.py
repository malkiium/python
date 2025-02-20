txt = str(input(" : "))

def texCounter(txt: str):
    count_dict = {}
    for char in txt:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    caracter = [(char, count) for char, count in count_dict.items()]
    print(caracter)
    return caracter

texCounter(txt)

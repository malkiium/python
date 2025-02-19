txt = str(input(" : "))

def texCounter(txt: str):
    txt_list = list(txt)
    txt_list.sort()
    count = 1
    caracter = []

    for i in range(0, len(txt_list)):
        if txt_list[i] == txt_list[i-1]:  
            count += 1
        else:
            caracter.append((txt_list[i-1], count))
            count = 1
    print(caracter)
    return caracter

texCounter(txt)

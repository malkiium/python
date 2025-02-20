def decomposer(txt: str):
    count_dict = {}
    for char in txt:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    caracter = {char: count for char, count in count_dict.items()}
    print(caracter)
    return caracter

assert decomposer("bonjour")== {'b':1,'o':2,'n':1,'j':1,'u':1,'r':1}
assert decomposer("abcd")=={'a':1,'b':1,'c':1,'d':1}
assert decomposer("aa bb c")=={'a':2,' ':2,'b':2,'c':1}
assert decomposer("aaa") == {'a':3}
assert decomposer("") == {}
numb = 1
exp = 0

while True:
    numb += 1
    if numb >= 10:
        numb -= 9
        exp += 1
        print(f"{numb}e{exp}")
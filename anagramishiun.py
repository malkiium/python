ch1 = ""
ch2 = ""
difletters = 0

def bananagramstuff():
    global ch2, ch1

    ch1 = input("what is the first word ? : ")
    ch2 = input("what is the second word ? : ")

    if len(ch1.lower()) == len(ch2.lower()):
        difletters = len(set(ch1) ^ set(ch2))  # Symmetric difference
        if difletters == 0:
            print("True")
        else:
            print("False")
    else:
        print("False")

bananagramstuff()
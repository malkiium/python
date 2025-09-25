ch1 = ""
ch2 = ""

def bananagramstuff():
    global ch2, ch1

    ch1 = input("what is the first word ? : ")
    ch2 = input("what is the second word ? : ")

    if len(ch1.lower()) == len(ch2.lower()):
        ch1_s = sorted(list(ch1))
        ch2_s = sorted(list(ch2))
        if ch1_s == ch2_s:
            print("True")
        else:
            print("False")
    else:
        print("False")

bananagramstuff()
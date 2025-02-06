motATrou = list(input("quel est votre mot a trou ? "))
secondMot = list(input("quel est le second mot ? "))

def compare(mot1:list, mot2:list):

    if len(mot1) == len(mot2):

        print(mot1, "\n", mot2, "\n\n")

        for i in range(len(mot1)):
            if mot1[i] == ".":
                mot1[i] =  mot2[i]

        mot1.sort()
        mot2.sort()

        if mot1 == mot2:
            print("Vraie")

    else:
        print("get recked. try again. \n\n\n\n\n")



compare(motATrou, secondMot)
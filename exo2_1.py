sumb = 1

def multi():
    global sumb

    sumb = input("what is the number you want to multiply : ")

    if sumb.isdigit():
        for j in range (1, 11):
            for i in range(1, 11):
                sumb = int(sumb)
                print(sumb*j*i, end=" ")
            print()
    else:
        print("this is not a number. try again.")
        print()
        multi()

multi()
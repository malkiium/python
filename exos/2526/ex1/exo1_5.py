def buyCycle(billP: int, billA: int, coinA: int):
    print("\n" * 5)
    print("the machine currently has :", billA, "bills of", billP, "€, and", coinA, "coins of 1€")

    doesCont = input("do you wish to buy something ? y/n : ")
    if doesCont != "y":
        return

    objPrice = int(input("what is the price of the object ? : "))
    moneyGiven = int(input("how much do you give to the machine ? : "))

    difference = moneyGiven - objPrice

    if difference < 0:
        print("sorry, you havent given enough.")
        return buyCycle(billP, billA, coinA)

    billsub = min(difference // billP, billA)

    remaining = difference - (billsub * billP)

    if remaining > coinA:
        print("sorry, the machine doesnt have enough coins.")
        return buyCycle(billP, billA, coinA)

    billA -= billsub
    coinA -= remaining

    print("numbers of bills returned are :", billsub)
    print("numbers of coins returned are :", remaining)

    return buyCycle(billP, billA, coinA)


buyCycle(5, 20, 100)

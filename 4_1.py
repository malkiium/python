def nearest_tens(number):
    Tens = (number//10)*10
    if number/10 >= Tens:
        upperTens = Tens
        lowerTens = Tens-10
    else:
        upperTens = Tens+10
        lowerTens = Tens
    print(lowerTens, upperTens)
    return (lowerTens, upperTens)


n = int(input("give a number : "))
nearest_tens(n)
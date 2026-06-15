def sqrrt(numb):
    guess = numb / 2.0
    for _ in range(20):  # perform 20 iterations
        trial = 0.5*(guess + (numb / guess))
        guess = trial
        print(trial)


num = float(input("Enter a number to find the square root of: "))
sqrrt(num)
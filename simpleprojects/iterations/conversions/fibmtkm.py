fib = [0, 1]

def fibonacii(i):
    j = 2
    while fib[-1] < i:
        print(fib[j-1])
        fib.append(fib[j-2] + fib[j-1])
        j += 1


def kmtml(i):
    print(i * 1.609344, "km")
    print(i * 0.6213711922, "mi")
    






numbwanted = int(input("what number do you want to convert ? : "))

fibonacii(numbwanted)
print("\n")
kmtml(numbwanted)


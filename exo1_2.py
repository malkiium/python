def fib(n:int):
    if n < 2:
        return 1
    else:
        fibo = [0]*n
        fibo[0] = 1
        fibo[1] = 1
        for i in range(2, len(fibo)):
            fibo[i] = fibo[i-1] + fibo[i-2]
        return fibo


nmb = int(input("Entrez un nombre: "))
print(fib(nmb))
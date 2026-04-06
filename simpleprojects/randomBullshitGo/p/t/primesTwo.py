def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # tous les pairs sauf 2 sont non premiers
    for i in range(3, int(n**0.5) + 1, 2):  # test jusqu'à racine carrée de n
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def is_goldbach(n):
    if n % 2 != 0 or n < 4:
        return False  # La conjecture s'applique aux pairs > 2
    for p in primes:
        if p > n:
            break
        if (n - p) in primes:
            print(f"{n} = {p} + {n - p}")
            return True
    return False

limit = 25000000  # jusqu'où on veut tester
primes = generate_primes(limit)

for testnmb in range(4, limit + 1, 2):  # tester tous les pairs >= 4
    is_goldbach(testnmb)


print("Fin de la vérification de la conjecture de Goldbach.\n\n", primes)
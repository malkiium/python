import random

print()
A = []
Asize = 3
e = []
s = [10, 20, 30]
q = random.randint(0, 100)

for i in range(Asize):
    A.append([])
    e.append(random.randint(-1, 1))
    for j in range(Asize):
        A[i].append(random.randint(0, 10))
    print(" A:", A[i] )

matrixmult = []
for i in range(Asize):
    matrixmult.append(0)
    for j in range(Asize):
        matrixmult[i] += A[i][j] * s[j]
print("\n\n mm:", matrixmult)

noiseadd = []
for i in range(Asize):
    noiseadd.append(matrixmult[i] + e[i])

print("\n\n noiseadd:", noiseadd)

b = []
for i in range(Asize):
    b.append((noiseadd[i]) % q)
print("\n\n b:", b)
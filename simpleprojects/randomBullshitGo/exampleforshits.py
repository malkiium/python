a = 0
b = 0
c = 0
d = 0
j = 0


for i in range(10000):
    ab = a * 10 + b
    bc = b * 10 + c
    cd = c * 10 + d

    if ab + cd == bc:
        print(a, b, "+", c, d, "=" ,b, c)
        j += 1

    d += 1

    if d == 10:
        d = 0
        c += 1
        if c == 10:
            c = 0
            b += 1
            if b == 10:
                b = 0
                a += 1
                if a == 10:
                    break

print("number of functioning combinations:", j)

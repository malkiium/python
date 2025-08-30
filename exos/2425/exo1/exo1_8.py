j = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                ab = int(str(a) + str(b))
                cd = int(str(c) + str(d))
                bc = int(str(b) + str(c))

                if ab + cd == bc:
                    print(a, b, "+", c, d, "=" ,b, c)
                    j += 1

print("number of functioning combinations:", j)
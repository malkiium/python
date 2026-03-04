y, i = 2, 1

while True:
    x = y/i
    sq = x**2
    second = (2*x)-1
    if sq > second:
        print(sq, ">", second, "for :", y, i)
    else:
        print("found one !! : ", sq, ">", second, "for :", y, i)
        break
    y += 1
    i += 1
x = 1
strs = 1

while True:
    print(x, strs)
    if x%2 == 0:
        x = x//2
    elif x == 1:
        strs+=1
        x = strs
    else:
        x = x*3 +1
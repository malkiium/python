x = 1
strs = 1
iters = 0
maxiters = 0
nmbmaxiters = 0

while strs<1000000:
    iters+=1
    print(x, strs, iters)
    if x%2 == 0:
        x = x//2
    elif x == 1:
        if iters > maxiters:
            maxiters = iters
            nmbmaxiters = strs
        strs+=1
        x = strs
        iters = 0
    else:
        x = x*3 +1


print("max iters:", maxiters, "for number:", nmbmaxiters)

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                a, b, c, d = str(i), str(j), str(k), str(l)
                ab, cd, bc = a+b, c+d, b+c
                abi, cdi, bci = int(ab), int(cd), int(bc)
                if bci == abi+cdi:
                    print(ab, "+", cd, "=", bc)
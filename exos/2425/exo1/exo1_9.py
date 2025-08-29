def find_numbers():
    print("Solutions sans contrainte de chiffres différents :\n")
    for a in range(1, 50):
        for b in range(0, 50):
            for c in range(0, 50):
                for d in range(0, 50):
                    ab = a * 10 + b
                    cd = c * 10 + d
                    ccdd = a * 1000 + b * 100 + c * 10 + d
                    if ab * cd == ccdd:
                        print(f"{ab:2} * {cd:2} = {ccdd}")

def find_numbers_diff():
    print("\nSolutions avec chiffres différents :\n")
    for a in range(1, 50):
        for b in range(0, 50):
            if a == b:
                continue
            for c in range(0, 50):
                if c in {a, b}:
                    continue
                for d in range(0, 50):
                    if d in {a, b, c}:
                        continue
                    ab = a * 10 + b
                    cd = c * 10 + d
                    ccdd = a * 1000 + b * 100 + c * 10 + d
                    if ab * cd == ccdd:
                        print(f"{ab:2} * {cd:2} = {ccdd}")

find_numbers()
find_numbers_diff()

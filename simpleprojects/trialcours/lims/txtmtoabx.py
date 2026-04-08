x = 1.0

for _ in range(300):
    ans = x * int(1 / x)
    print(ans)
    x = x / 2
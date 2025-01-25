def factorial():
    x = 1
    yis = 1
    factorials = []

    while True:
        yis = yis * x
        factorials.append(yis)
        x += 1
        print(f"Stored {len(factorials)} factorials.")

factorial()

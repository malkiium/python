Un = -5/3
Un1 = 0

for i in range(100):
    try:
        Un1 = 1 / (1 + Un)
        Un = (round(Un1, 2))
    except ZeroDivisionError:
        print(f"   1 \n ----- \n 1{Un} \n\n this is a Zero Division. \n number Un+{i}")
        break
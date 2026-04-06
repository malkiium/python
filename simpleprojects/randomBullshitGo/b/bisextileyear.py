MINYEAR, MAXYEAR = 1500, 3000

for i in range(MINYEAR, MAXYEAR):
    if  i % 400 == 0:
        print(i)
    if i % 4 == 0 and i % 100 != 0:
        print(i)

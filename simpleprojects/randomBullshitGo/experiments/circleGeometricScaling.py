import math

def circleArea(radius: int):
    return (math.pi*(radius**2))


for i in range(2, 1000):
    prevArea=circleArea(i-1)
    nextArea=circleArea(i)
    geometricChange=nextArea/prevArea
    print(geometricChange)

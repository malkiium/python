def steps(stps : int) -> list:
    stepcount = 0
    steplist= []

    while stps>0:
        if stps > 5:
            stps -= 5
            stepcount += 1
            print("at step #", stepcount, "  it jumped 5 steps.   there is ", stps, " steps left")
            steplist.append(5)
        elif stps > 3:
            stps -= 3
            stepcount += 1
            print("at step #", stepcount, "  it jumped 3 steps.   there is ", stps, " steps left")
            steplist.append(3)
        else:
            stps -= 1
            stepcount += 1
            print("at step #", stepcount, "  it jumped 1 steps.   there is ", stps, " steps left")
            steplist.append(1)

    toalresult = [steplist, stepcount]

    return toalresult

steps(859)
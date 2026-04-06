def trials():
    if False:
        return False
    else:
        return True

def trials2():
    if trials():
        print("true")

    if trials() and trials2():
        return True
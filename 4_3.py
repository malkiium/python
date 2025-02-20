def listToTuple(lst:list):
    try:
        lst = tuple(lst)
        print("\n", lst)
        return lst
    except ValueError:
        print("Vous devez entrer une liste")
        listToTuple()

assert listToTuple([]) == ()
assert listToTuple([5]) == (5,)
assert listToTuple([5,9,2,4]) == (5,9,2,4)
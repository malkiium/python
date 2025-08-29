def permEtDern(find:int, l1:list):
    if find not in l1:
        return [-1, -1]

    first_index = l1.index(find)


    l1.reverse()
    for i in range(len(l1)):
        if l1[i] == find:
            last_index = len(l1) - (i+1)
            break
    
    print(first_index, last_index)
    return [first_index, last_index]


li = [1, 2, 3, 2, 4, 2]
assert (permEtDern(2, li))
li = [1,2,3,4]
assert(permEtDern(3,li))
li = [1,2,3,4]
assert(permEtDern(5,li))

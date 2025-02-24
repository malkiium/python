ll = [x for x in range(0,7)]
print("\n list creation", ll)

ll.append(45) # adds to the end
print("\n append", ll)

ll.append(23)
print("\n append", ll)

ll.extend([56,43]) # adds this sublist to the list
print("\n extend", ll)

ll.insert(6, 5) # adds 5 at index 6 in the list
print("\n insert", ll)

# copy only makes a duplicate of the list, but the list's data has the same reference.
# changing one list's content changes the other
ll2 = ll.copy()

ll2.sort() # organizes the list in ascending order, SUPER USEFUL
print("\n sort", ll2)
print(ll) # verifies that ll was not sorted

lltri = list(sorted(ll)) # creates a sorted list in a new list, without sorting the original list
print("\n lltri", lltri)

ll2.reverse() # reverses the list
print("\n reverse", ll2)

ll2.clear()
print("\n clear", ll2)

li2 = [a for a in range(0,5)]
print("\n li2", li2)
for i in range(len(li2)): # this needs a list with data INSIDE IT, an empty list = no go
    li2[i] = 2**i #if empty, then 2^empty = error. thus needs 2^0 = not error, and 0 will be changed by i in the for loop.
print("\n for loop with lists", li2)

def anyfunction(x: float):
    return 2*x

E = map(anyfunction, li2) # map lets you apply a function to a list and use it as a variable
print("\n E without list info", E)
E = list(E)
print("\n with list info", E)

list1 = []
list2 = []
list3 = list1
if list1 == list2:
    print("\n list1 == list2")
else:
    print("\n list1 != list2")

if list1 is list2:
    print("\n list1 is list2") # this is false because list1 and list2 are 2 different places in the memory even if they have the same data
else:
    print("\n list1 is not list2")

if list1 == list3:
    print("\n list1 == list3")
else:
    print("\n list1 != list3")

if list1 is list3:
    print("\n list1 is list3")
else:
    print("\n list1 is not list3")



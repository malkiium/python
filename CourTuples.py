# Creating an empty tuple
tuple1 = ()

# Tuples are similar to lists but they are immutable, meaning you cannot modify them after creation
# Example of a tuple with some elements
tuple2 = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(tuple2[0])  # Output: 1

# Tuples can also contain different data types
tuple3 = (1, "hello", 3.14)

# You can concatenate tuples
tuple4 = tuple2 + tuple3

# You can also use tuples for multiple assignments
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

print("----------------------------------------------------------------------------------")
# Example showing that you can change a list but cannot change a tuple
list1 = [1, 2, 3]
list1[0] = 10  # This is allowed
print(list1)  # Output: [10, 2, 3]

print("----------------------------------------------------------------------------------")
try:
    tuple2[0] = 10  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

print("----------------------------------------------------------------------------------")
# To "append" to a tuple, you can convert it to a list, modify the list, and convert it back to a tuple
list2 = list(tuple2)
list2.append(6)
tuple2 = tuple(list2)
print(tuple2)  # Output: (1, 2, 3, 4, 5, 6)

# Similarly, you can "remove" an element by converting to a list, modifying the list, and converting back to a tuple
list2.remove(3)
tuple2 = tuple(list2)
print(tuple2)  # Output: (1, 2, 4, 5, 6)
# Comparing sets
print({2, 1} == {1, 2})  # True, because sets are unordered collections of unique elements
print({2, 1} == {1, 2, 2})  # True, because duplicates are removed in sets


# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("----------------------------------------------------------------------------------")

# Union
print(set_a | set_b)  # {1, 2, 3, 4, 5}

print("----------------------------------------------------------------------------------")

# Intersection
print(set_a & set_b)  # {3}

print("----------------------------------------------------------------------------------")

# Difference
print(set_a - set_b)  # {1, 2}
print(set_b - set_a)  # {4, 5}

print("----------------------------------------------------------------------------------")

# Symmetric difference
print(set_a ^ set_b)  # {1, 2, 4, 5}
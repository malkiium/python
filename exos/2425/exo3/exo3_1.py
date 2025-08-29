import random

def ver1(numbs: list):
    """Find the maximum value in the list."""
    hinum = 0
    for x in range(len(numbs)):
        if hinum < numbs[x]:
            hinum = numbs[x]
    return hinum

def ver2(numbs: list):
    """Find the index of the last occurrence of the maximum value."""
    hinum = ver1(numbs)  # Get the maximum value first
    for i in range(len(numbs)-1, -1, -1):  # Start from the end to find the last occurrence
        if numbs[i] == hinum:
            return i
    return -1  # If not found

def ver3(numbs: list):
    """Find the index of the first occurrence of the maximum value."""
    hinum = ver1(numbs)  # Get the maximum value first
    for i in range(len(numbs)):
        if numbs[i] == hinum:
            return i
    return -1  # If not found

def ver4(numbs: list):
    """Find all occurrences of the maximum value and their indices."""
    hinum = ver1(numbs)  # Get the maximum value first
    occurrences = []
    for i in range(len(numbs)):
        if numbs[i] == hinum:
            occurrences.append(i)
    return occurrences

# Test the functions with the predefined list
ll = [4, 7, 5, 7, 3]

# Assertions to check if the function outputs match the expected results
assert(ver1(ll) == 7)   # The maximum value is 7
assert(ver2(ll) == 3)   # The last occurrence of 7 is at index 3
assert(ver3(ll) == 1)   # The first occurrence of 7 is at index 1
assert(ver4(ll) == [1, 3])  # Both occurrences of 7 are at indices [1, 3]

print("All tests passed! ✅")

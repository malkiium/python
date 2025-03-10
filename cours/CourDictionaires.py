# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values in the dictionary
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 25

print("----------------------------------------------------------------------------------")
# Adding a new key-value pair to the dictionary
my_dict["email"] = "alice@example.com"
print("Updated dictionary:", my_dict)

print("----------------------------------------------------------------------------------")
# Updating an existing value in the dictionary
my_dict["age"] = 26
print("Updated age:", my_dict["age"])

print("----------------------------------------------------------------------------------")
# Removing a key-value pair from the dictionary
del my_dict["city"]
print("Dictionary after deletion:", my_dict)

print("----------------------------------------------------------------------------------")
# Using .get() to access values safely
print("Phone:", my_dict.get("phone", "Key not found"))

print("----------------------------------------------------------------------------------")
# Removing a key-value pair using .pop()
removed_value = my_dict.pop("age", "Key not found")
print("Removed value:", removed_value)
print("Dictionary after pop:", my_dict)

print("----------------------------------------------------------------------------------")
# Iterating through keys in the dictionary
for key in my_dict:
    print("Key:", key)

print("----------------------------------------------------------------------------------")
# Iterating through values in the dictionary
for value in my_dict.values():
    print("Value:", value)

print("----------------------------------------------------------------------------------")
# Iterating through key-value pairs in the dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print("----------------------------------------------------------------------------------")
# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name is a key in the dictionary")

print("----------------------------------------------------------------------------------")
# Getting the length of the dictionary
print("Length of dictionary:", len(my_dict))

print("----------------------------------------------------------------------------------")
# Using .keys() and .values() as lists
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
print("Keys:", keys_list)
print("Values:", values_list)

print("----------------------------------------------------------------------------------")
# Copying a dictionary (.copy())
new_dict = my_dict.copy()
print("Copied dictionary:", new_dict)

print("----------------------------------------------------------------------------------")
# Merging dictionaries (.update())
another_dict = {"country": "USA", "age": 27}
my_dict.update(another_dict)
print("Updated dictionary after merging:", my_dict)

print("----------------------------------------------------------------------------------")
# Clearing all elements (.clear())
my_dict.clear()
print("Cleared dictionary:", my_dict)

print("----------------------------------------------------------------------------------")
# Using dict() constructor
new_dict = dict(name="Bob", age=30, city="San Francisco")
print("New dictionary:", new_dict)

print("----------------------------------------------------------------------------------")
# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print("Squared numbers dictionary:", squared_numbers)

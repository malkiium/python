# CourDictionaires.py

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values in the dictionary
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 25

# Adding a new key-value pair to the dictionary
my_dict["email"] = "alice@example.com"
print("Updated dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# Updating an existing value in the dictionary
my_dict["age"] = 26
print("Updated age:", my_dict["age"])  # Output: 26

# Removing a key-value pair from the dictionary
del my_dict["city"]
print("Dictionary after deletion:", my_dict)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# Iterating through keys in the dictionary
for key in my_dict:
    print("Key:", key)  # Output: name, age, email

# Iterating through values in the dictionary
for value in my_dict.values():
    print("Value:", value)  # Output: Alice, 26, alice@example.com

# Iterating through key-value pairs in the dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Output: Key: name, Value: Alice; Key: age, Value: 26; Key: email, Value: alice@example.com

# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name is a key in the dictionary")  # Output: Name is a key in the dictionary

# Getting the length of the dictionary
print("Length of dictionary:", len(my_dict))  # Output: 3
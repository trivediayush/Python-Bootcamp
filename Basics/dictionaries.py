my_dict = {
    "name": "ayush",
    "age": 21,
    "location": "india"
}

print("Original dictionary:", my_dict)
print("Type:", type(my_dict))

# Accessing values by key
name = my_dict["name"]
print('my_dict["name"]:', name)

age = my_dict.get("age")
print('my_dict.get("age"):', age)

# Adding or updating key-value pairs
my_dict["email"] = "ayush@example.com"
print('After adding "email":', my_dict)

my_dict["age"] = 22
print('After updating "age":', my_dict)

# Removing elements
removed_value = my_dict.pop("location")
print('After pop("location"), removed:', removed_value)
print("Dictionary now:", my_dict)

# Remove and return an arbitrary item (popitem removes last inserted)
key, value = my_dict.popitem()
print(f"After popitem(), removed: ({key}, {value})")
print("Dictionary now:", my_dict)

# Keys, values, and items
keys = list(my_dict.keys())
print("Keys:", keys)

values = list(my_dict.values())
print("Values:", values)

items = list(my_dict.items())
print("Items:", items)

# Check if key exists
has_name = "name" in my_dict
print('Is "name" in dictionary?:', has_name)

# Clear dictionary
my_dict.clear()
print("After clear():", my_dict)

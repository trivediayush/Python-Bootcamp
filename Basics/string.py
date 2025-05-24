mystring = "Hello, World!"

print("Original string:", mystring)
print("Type:", type(mystring))

# Slicing examples
a = mystring[1:5]      # Characters from index 1 to 4
print("mystring[1:5]:", a)

b = mystring[:5]       # First 5 characters
print("mystring[:5]:", b)

c = mystring[-6:-1]    # Characters from 6th last to 2nd last
print("mystring[-6:-1]:", c)

d = mystring[-1:]      # Last character as a string
print("mystring[-1:]:", d)

e = mystring[1:]       # All characters from index 1 to end
print("mystring[1:]:", e)

f = mystring[1::3]     # From index 1, every 3rd character
print("mystring[1::3]:", f)

# Additional common string methods:

# Convert to uppercase
upper_str = mystring.upper()
print("upper():", upper_str)

# Convert to lowercase
lower_str = mystring.lower()
print("lower():", lower_str)

# Strip whitespace from both ends
stripped = mystring.strip()
print("strip():", stripped)

# Replace substring
replaced = mystring.replace("World", "Python")
print("replace('World', 'Python'):", replaced)

# Find substring index (-1 if not found)
index_o = mystring.find("o")
print("find('o'):", index_o)

# Count occurrences of substring
count_l = mystring.count("l")
print("count('l'):", count_l)

# Check if string starts with substring
starts_hello = mystring.startswith("Hello")
print("startswith('Hello'):", starts_hello)

# Check if string ends with substring
ends_excl = mystring.endswith("!")
print("endswith('!'):", ends_excl)

# Split string by delimiter (default whitespace)
split_str = mystring.split(", ")
print("split(', '):", split_str)

# Join list of strings
joined_str = "-".join(["Python", "is", "fun"])
print("join(['Python', 'is', 'fun']):", joined_str)

# String length
length = len(mystring)
print("len():", length)


my_string = "12345"
my_string2 = "   "
my_string3 = "Hello123"
my_string4 = "HELLO"
my_string5 = "hello"
my_string6 = "Hello World"
my_string7 = "2023"

print("Original strings:")
print(f"my_string: '{my_string}'")
print(f"my_string2: '{my_string2}'")
print(f"my_string3: '{my_string3}'")
print(f"my_string4: '{my_string4}'")
print(f"my_string5: '{my_string5}'")
print(f"my_string6: '{my_string6}'")
print(f"my_string7: '{my_string7}'")
print()

# Checks if all characters are numeric (digits)
print("isnumeric():")
print(f"my_string.isnumeric(): {my_string.isnumeric()}")
print(f"my_string3.isnumeric(): {my_string3.isnumeric()}")
print()

# Checks if all characters are digits (similar to isnumeric but slightly different)
print("isdigit():")
print(f"my_string.isdigit(): {my_string.isdigit()}")
print(f"my_string3.isdigit(): {my_string3.isdigit()}")
print()

# Checks if all characters are whitespace
print("isspace():")
print(f"my_string2.isspace(): {my_string2.isspace()}")
print(f"my_string.isspace(): {my_string.isspace()}")
print()

# Checks if all characters are alphabetic
print("isalpha():")
print(f"my_string4.isalpha(): {my_string4.isalpha()}")
print(f"my_string5.isalpha(): {my_string5.isalpha()}")
print(f"my_string3.isalpha(): {my_string3.isalpha()}")
print()

# Checks if all characters are alphanumeric (letters or numbers)
print("isalnum():")
print(f"my_string3.isalnum(): {my_string3.isalnum()}")
print(f"my_string4.isalnum(): {my_string4.isalnum()}")
print(f"my_string6.isalnum(): {my_string6.isalnum()}  # contains space")
print()

# Checks if string is lowercase
print("islower():")
print(f"my_string5.islower(): {my_string5.islower()}")
print(f"my_string4.islower(): {my_string4.islower()}")
print()

# Checks if string is uppercase
print("isupper():")
print(f"my_string4.isupper(): {my_string4.isupper()}")
print(f"my_string5.isupper(): {my_string5.isupper()}")
print()

# Checks if string is title case (first letter uppercase, rest lowercase)
print("istitle():")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")
print(f"my_string6.istitle(): {my_string6.istitle()}")
print()

# Checks if string is decimal (only decimal digits)
print("isdecimal():")
print(f"my_string.isdecimal(): {my_string.isdecimal()}")
print(f"my_string3.isdecimal(): {my_string3.isdecimal()}")
print()

# Checks if string is printable
print("isprintable():")
print(f"my_string.isprintable(): {my_string.isprintable()}")
print(f"'Hello\\nWorld'.isprintable(): {'Hello\nWorld'.isprintable()}")

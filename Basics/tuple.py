my_tup = (1, 2, 3, 4, 5, 6, 7, 5, 4, 3)

print("Original tuple:", my_tup)
print("Type:", type(my_tup))

# Access elements by index
print("my_tup[0]:", my_tup[0])
print("my_tup[-1]:", my_tup[-1])

# Slicing 
a = my_tup[1:4]      # Elements at index 1 to 3
print("my_tup[1:4]:", a)

b = my_tup[:3]       # First three elements
print("my_tup[:3]:", b)

c = my_tup[-4:-1]    # From 4th last to 2nd last element
print("my_tup[-4:-1]:", c)

d = my_tup[-1:]      # Last element as a tuple
print("my_tup[-1:]:", d)

e = my_tup[1:]       # Elements from index 1 to end
print("my_tup[1:]:", e)

f = my_tup[1::3]     # From index 1, every 3rd element
print("my_tup[1::3]:", f)

# Tuple methods

# Count occurrences of an element
count_3 = my_tup.count(3)
print("count(3):", count_3)

# Find index of an element
index_5 = my_tup.index(5)
print("index(5):", index_5)

# Tuples are immutable, so no append, insert, or remove methods
# But you can concatenate tuples:
extended_tup = my_tup + (8, 9)
print("After concatenation:", extended_tup)

# Length of tuple
length = len(my_tup)
print("len():", length)

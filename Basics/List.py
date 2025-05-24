mylist = [1, 2, 3, 4, 5, 6, 7]

print("Original list:", mylist)
print("Type:", type(mylist))

# Slicing examples
a = mylist[1:3]      # Elements at index 1 and 2
print("mylist[1:3]:", a)

b = mylist[:3]       # First three elements (index 0 to 2)
print("mylist[:3]:", b)

c = mylist[-4:-1]    # From 4th last to 2nd last element
print("mylist[-4:-1]:", c)

d = mylist[-1:]      # Last element as a list
print("mylist[-1:]:", d)

e = mylist[1:]       # All elements from index 1 to end
print("mylist[1:]:", e)

f = mylist[1::3]     # From index 1, every 3rd element
print("mylist[1::3]:", f)

# Additional common list methods:

# Append an element to the end
mylist.append(8)
print("After append(8):", mylist)

# Insert element at a specific position (index 2)
mylist.insert(2, 99)
print("After insert(2, 99):", mylist)

# Remove first occurrence of element 3
mylist.remove(3)
print("After remove(3):", mylist)

# Pop element at index 4 (default is last element)
popped = mylist.pop(4)
print("After pop(4), popped element:", popped)
print("List now:", mylist)

# Find index of element 6
index_6 = mylist.index(6)
print("Index of 6:", index_6)

# Count occurrences of element 7
count_7 = mylist.count(7)
print("Count of 7:", count_7)

# Sort the list
mylist.sort()
print("After sort():", mylist)

# Reverse the list
mylist.reverse()
print("After reverse():", mylist)

# Iteration using for loop
print("Iterating through list:")
for item in mylist:
    print(item, end=" ")
print()

# Iteration with index
print("Iterating with index:")
for i, val in enumerate(mylist):
    print(f"Index {i}: Value {val}")

# List comprehensions

# Square of each element
squares = [x**2 for x in mylist]
print("Squares:", squares)

# Filter even numbers
evens = [x for x in mylist if x % 2 == 0]
print("Even numbers:", evens)

# Add 10 to each element
plus_ten = [x + 10 for x in mylist]
print("Each element +10:", plus_ten)

# Create a list of strings
as_strings = [str(x) for x in mylist]
print("As strings:", as_strings)

# Clear all elements
mylist.clear()
print("After clear():", mylist)

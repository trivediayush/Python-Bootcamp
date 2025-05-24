my_fset = frozenset([1, 2, 3, 4, 5])

print("Original frozenset:", my_fset)
print("Type:", type(my_fset))

# frozenset is immutable, so no add(), remove(), update(), pop(), etc.

# Membership test
print("Is 3 in frozenset?:", 3 in my_fset)
print("Is 10 in frozenset?:", 10 in my_fset)

# Length
print("Length of frozenset:", len(my_fset))

# Iteration
print("Iterating through frozenset:")
for item in my_fset:
    print(item, end=" ")
print()

# Set operations
other = frozenset([3, 4, 5, 6, 7])

union = my_fset.union(other)
print("Union:", union)

intersection = my_fset.intersection(other)
print("Intersection:", intersection)

difference = my_fset.difference(other)
print("Difference (my_fset - other):", difference)

symmetric_diff = my_fset.symmetric_difference(other)
print("Symmetric Difference:", symmetric_diff)

# Subset, Superset, Disjoint checks
print("Is my_fset subset of other?:", my_fset.issubset(other))
print("Is my_fset superset of other?:", my_fset.issuperset(other))
print("Is my_fset disjoint with other?:", my_fset.isdisjoint(other))

# Conversion to set (if mutation needed)
mutable_set = set(my_fset)
mutable_set.add(99)
print("Converted to set and added 99:", mutable_set)

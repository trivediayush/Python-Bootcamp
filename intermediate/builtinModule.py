print("=== Module Examples ===")

# Import entire module
import math
print("math.sqrt(16):", math.sqrt(16))
print("math.pi:", math.pi)

# Import specific functions
from random import randint, choice
print("randint(1, 100):", randint(1, 100))
print("choice(['a', 'b', 'c']):", choice(['a', 'b', 'c']))

# Import with alias
import datetime as dt
now = dt.datetime.now()
print("Current datetime:", now)

# Use dir() to explore module attributes
print("Attributes in math module:", dir(math)[:5])  # Display first 5 attributes

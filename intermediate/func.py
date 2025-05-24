# Function definitions and usage in Python

print("=== Function Examples ===")

# 1. Basic function
def greet():
    print("Hello, welcome to the function demo.")

greet()

# 2. Function with parameters
def add(a, b):
    return a + b

print("add(5, 3):", add(5, 3))

# 3. Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print("power(3):", power(3))  # Uses default exponent
print("power(2, 5):", power(2, 5))

# 4. Function with keyword arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Ayush")

# 5. Function with variable positional arguments (*args)
def total_sum(*args):
    return sum(args)

print("total_sum(1, 2, 3, 4):", total_sum(1, 2, 3, 4))

# 6. Function with variable keyword arguments (**kwargs)
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Profile:")
profile(name="Ayush", location="India", age=21)

# 7. Function returning multiple values
def stats(x, y):
    return x + y, x * y, x / y

sum_, product, division = stats(10, 2)
print("Sum:", sum_)
print("Product:", product)
print("Division:", division)

# 8. Lambda function
square = lambda x: x * x
print("square(6):", square(6))

# 9. Nested functions
def outer(a):
    def inner(b):
        return b * 2
    return inner(a) + 1

print("outer(5):", outer(5))

# 10. Function with type hints
def subtract(x: int, y: int) -> int:
    return x - y

print("subtract(10, 3):", subtract(10, 3))

# 11. Using map() with a function
nums = [1, 2, 3, 4]
def double(n):
    return n * 2

doubled = list(map(double, nums))
print("Doubled list using map():", doubled)

# 12. Using filter() with a lambda
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter():", evens)

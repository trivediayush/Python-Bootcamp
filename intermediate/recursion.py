print("=== Recursion Examples ===")

# 1. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("factorial(5):", factorial(5))  # 120

# 2. Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(7):", fibonacci(7))  # 13

# 3. Sum of first n numbers
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print("recursive_sum(10):", recursive_sum(10))  # 55

# 4. Reverse a string using recursion
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print("reverse_string('ayush'):", reverse_string("ayush"))

# 5. Greatest Common Divisor (GCD) using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("gcd(48, 18):", gcd(48, 18))  # 6

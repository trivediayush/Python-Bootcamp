a = 5
b = 5

# Arithmetic Operators
print('Arithmetic Operators')
print(f'Sum = {a} + {b} = {a + b}')
print(f'Subtraction = {a} - {b} = {a - b}')
print(f'Multiplication = {a} * {b} = {a * b}')
print(f'Division (float) = {a} / {b} = {a / b}')
print(f'Floor Division = {a} // {b} = {a // b}')
print(f'Exponentiation = {a} ** {b} = {a ** b}')
print(f'Modulus = {a} % {b} = {a % b}')

# Comparison (Relational) Operators
print('Comparison (Relational) Operators')
print(f'{a} == {b} → {a == b}')
print(f'{a} != {b} → {a != b}')
print(f'{a} > {b} → {a > b}')
print(f'{a} < {b} → {a < b}')
print(f'{a} >= {b} → {a >= b}')
print(f'{a} <= {b} → {a <= b}')

# Assignment Operators
print('Assignment Operators')
a = 5
print(f'Initial a = {a}')
a += 1
print(f'a += 1 → {a}')
a -= 1
print(f'a -= 1 → {a}')
a *= 2
print(f'a *= 2 → {a}')
a /= 2
print(f'a /= 2 → {a}')
a //= 2
print(f'a //= 2 → {a}')
a **= 2
print(f'a **= 2 → {a}')
a %= 3
print(f'a %= 3 → {a}')

# Logical Operators
print('Logical Operators')
x = True
y = False
print(f'{x} and {y} → {x and y}')
print(f'{x} or {y} → {x or y}')
print(f'not {x} → {not x}')

# Bitwise Operators (on integers)
a = 5  # binary: 0b0101
b = 3  # binary: 0b0011
print('Bitwise Operators')
print(f'{a} & {b} → {a & b}')    # Bitwise AND
print(f'{a} | {b} → {a | b}')    # Bitwise OR
print(f'{a} ^ {b} → {a ^ b}')    # Bitwise XOR
print(f'~{a} → {~a}')            # Bitwise NOT
print(f'{a} << 1 → {a << 1}')    # Left Shift
print(f'{a} >> 1 → {a >> 1}')    # Right Shift

# Identity Operators
print('Identity Operators')
a = 5
b = 5
print(f'{a} is {b} → {a is b}')
print(f'{a} is not {b} → {a is not b}')

# Membership Operators
print('Membership Operators')
lst = [1, 2, 3, 4, 5]
print(f'{a} in {lst} → {a in lst}')
print(f'{a} not in {lst} → {a not in lst}')

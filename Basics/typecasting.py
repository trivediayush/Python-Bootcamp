# exp = eval(input("enter.."))
# print(exp)

a = 4
b = "22"
name = "rahul"

# Convert string 'b' to float
d = float(b)

print(d)              # Output: 22.0
print(type(d))        # Output: <class 'float'>

# Convert integer 'a' to string
a_str = str(a)
print(a_str)          # Output: "4"
print(type(a_str))    # Output: <class 'str'>

# Concatenate name with converted values
print(name + " " + a_str + " " + str(d))  # Output: rahul 4 22.0

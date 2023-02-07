def print_variables(a, b, msg=""):
    print(msg, "a =", a, ", b =", b)

a = 10
b = 20
print_variables(a, b, "Original values:")

#using a temporary variable
x = a
a = b
b = x
print_variables(a, b, "After swap using temporary variable:")

#without using a temporary variable
a = 10
b = 20
a, b = b, a
print_variables(a, b, "After swap without using temporary variable:")

#using arithmetic operations
a = a + b
b = a - b
a = a - b
print_variables(a, b, "After swap without using add/subtract:")

a = 77
b = 13
a = a * b
b = a / b
a = a / b
print_variables(a, b, "After swap without using multiply/divide:")
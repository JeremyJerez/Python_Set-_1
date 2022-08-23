#Problem set 01
"""
this it's my solution to the math interpreter problem
"""
a = input("Expression: ")
x, y, z = a.split(" ")
x2 = float(x)
z2 = float(z)
if y == "+":
    print(x2 + z2)
elif y == "-":
    print(x2 - z2)
elif y == "*":
    print(x2 * z2)
elif y == "/":
    print(x2 / z2)
else:
    print("NOT AN ARITMETIC EXPRESSION")

#Font1 : https://www.geeksforgeeks.org/type-conversion-python/
#Font2 : https://www.w3schools.com/python/python_casting.asp

print("Type Conversion")
print()

print("#Implicit Type Conversion")
x = 10
print("x is of type", type(x))
y = 10.6
print("x is of type", type(y))
x = x + y
print(x)
print("x is of type:", type(x))
print()

print("#Explicit Type Conversion")

print("#int")
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
print()

print("#float")
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
print()

print("#string")

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

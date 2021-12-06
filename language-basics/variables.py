# Font : https://www.w3schools.com/python/python_variables.asp

print("#creating variables")
x = 5
y = "John"  # Same as 'John'
print(x)
print(y)
print()

print("#same variables but diferent types")
x = 4
x = "Sally"
print(x)
print()

print("#casting")
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
print()

print("#casting")
x = 5
y = "John"
print(type(x))
print(type(y))
print(z)
print()

print("##A will not overwrite a (case sensitive)")
a = 4
A = "Sally"
print()

print("#variable naming")
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print()

print("#illegal variable names")
print("# 2myvar = 'John'")
print("# my-var = 'John'")
print("# my var = 'John'")
print()

print("#assigning multiple values")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print()

print("# One value to multiple variables")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print()

print("#unpacking collection")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print()

print("#unpacking tuple")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

print("#output variables")
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z = x + y
print(z)
print()

print("#output variables - sum")
x = 5
y = 10
print(5 + 10)
print()

print("#illegal sum string with value")
print("# x = 5")
print("# y = 'John'")
print("# print(x + y)")
print()

print("#globa Variable")
x = "awesome"

def myFunc():
    print("Python is " + x)

myFunc()

x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x)
print()

print("#global scope")
def myFunc():
    global x
    x = "Fantastic"

myFunc()

print("Python is " + x)

x = "awesome"

def myFunc():
    global x
    x = "fantastic"

myFunc()

print("Python is " + x)
print()

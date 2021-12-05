x = 5
y = "John"  # Same as 'John'
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

a = 4
A = "Sally"
#A will not overwrite a (case sensitive)

# variable naming

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Assigning multiple values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Output variables

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(5 + 10)

# illegal sum string with value

# x = 5
# y = "John"
# print(x + y)

# Globa Variable
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

# Global scope

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
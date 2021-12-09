#Font: https://www.w3schools.com/python/python_functions.asp

print("Functions")
print()

print("No Args")
def my_function():
    print("Hello from a function")

my_function()
print()

print("One Arg")
def my_function(fname):
    print(fname + " Refsnes")
    
my_function("Anderson")
my_function("Carl")
print()

print("Two Arg")
def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Emil", "Refsnes")
print()

print("Passing wrong number of args")
#my_function("Emil")
print()

print("Arbitrary Arguments *args")

def my_function(*kids): # Will receive a tuple of arguments
    print("The youngest child is " + kids[2])
    
my_function("Emil", "Tobias", "Linus")
print()

print("Keyword Arguments")

def my_function(child3, child2, child1): # we define a key as the variable name (key = value). This way inside the function, we can use the variable that will match the key = value defined
    print("The youngest child is " + child1)
    
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print()

print("Arbitrary Keyword Arguments **kwargs")

def my_function(**kid):# Will receive a dictionary of key = value
    print("His last name is " + kid["fname"])
    
my_function(fname = "Tobias", lname = "Refsnes")
print()

print("Default Parameter Value")

def my_function(country = "Norway"): # We can define a default value to variable if no arguments is provided
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print()

print("Passing a List as an Argument")

def my_function(food):
    for x in food:
        print(x)
        
fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print()

print("Return Values")

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(1))

print()

print("Recursion")

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
    
print("\n\nRecursion Example Results")

tri_recursion(6)

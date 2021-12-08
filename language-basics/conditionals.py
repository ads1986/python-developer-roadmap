#Font1: https://www.w3schools.com/python/python_conditions.asp
#Font2: https://www.pythontutorial.net/python-basics/python-boolean/

print("Conditionals")
print()

print("#If-Elif-Else")

x = 2
y = 2
w = 5

if x == w:
    print("X is equal W")
else:
    print("X is not equal W")

if x == w:
    print("X is equals W")
elif x != y:
    print("X is not equals y")
else:
    print("X is equals Y")
    
if x < w:
    print("X less than W")
    
if x <= w:
    print("X less than or equal to W")
    
if w > x:
    print("W greater thant X")
    
if w >= x:
    print("W greater than or equal to X")
print()

print("#Falsy")

x = 0

if not x:
    print("X == 0 is Falsy")
    
x = ""

if not x:
    print("X == '' is Falsy")

x = None

if not x:
    print("X == None is Falsy")
    
x = []

if not x:
    print("X == [] is Falsy")
    
x = ()

if not x:
    print("X == () is Falsy")
    
x = {}

if not x:
    print("X == {} is Falsy")
    
print("#Truthy")

x = 1

if x:
    print("X == 1 is Truthy")
    
x = "A"

if x:
    print("X == 'A' is Truthy")
 
x = ["Test1"]

if x:
    print("X == ['Test1'] is Truthy")
    
x = ("Test1")

if x:
    print("X == ('Test1') is Truthy")
    
x = {"name":"Test1"}

if x:
    print("X == {'name':'Test1'} is Truthy")

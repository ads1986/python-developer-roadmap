#Font1: https://www.w3schools.com/python/python_ref_functions.asp
#Font2: https://www.tutorialsteacher.com/python/callable-method

print("Functions")
print()

print("abs()")
x = 10.5
print(abs(x))
print()

print("all()")
x = ["apple", "mango"]
print(all(x))
print()

print("any()")
x = [True, None]
print(any(x))
print()

print("ascii()")
x = ["apple", "mango"]
print(ascii(x))
print()

print("bin()")
print(bin(10))
print()

print("bool()")
x = "123"
print(bool(x))
print()

print("bytearray()")
print(bytearray(4))
print()

print("bytes()")
print(bytes(4))
print()

print("callable()") # Means that the calling will return a new instance
print("Is str callable?", callable(str))
print("Is len callable?", callable(len))
print("Is list callable?", callable(list))
num = 10
print("Is variable callable?", callable(num))
print()

print("chr()")
print(chr(195))
print()

print("classmethod()") # Converts a method into a class method
print(chr(195))
print()

print("compile()")
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
print()

print("complex()")
x = complex(3,5)
print(x)
print()

print("delattr()")

class Person:
    name = "John"
    age = 36
    country = "Norway"

delattr(Person, 'age')
print()

print("dict()") # create a dictionary 
x = dict(name = "John", age = 36, country = "Norway")
print(x)
print()

print("dir()")
print(dir(Person))
print()

print("divmod()")
print(divmod(8, 3))
print()

print("enumerate()") # returns as an enumerable object
x = ("apple", "mango")
y = enumerate(x)
print(list(y))
print()

print("eval()")
x = 'print(55)'
eval(x)
print()

print("exec()")
x = 'name = "John"\nprint(name)'
exec(x)
print()

print("filter()")
ages = [5,12,17,18,24,32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages) # Filter an iterable object based on defined criterias

for x in adults:
    print(x)
    
print()

print("float()")
print(float(1))
print()

print("format()") 
print(format(0.5, '%')) # Format a value based on a list of formats that could fit in specific situations
print()

print("frozenset()")
x = ["apple", "orange"]
print(frozenset(x))
print()

print("getattr()")
x = getattr(Person, 'name')
print(x)
print()

print("globals()")
print(globals())
print()

print("hasattr()")
print(hasattr(Person, 'age'))
print()

print("hash()")
print(hash(Person))
print()

print("help()")
print(help(Person))
print()

print("hex()")
print(hex(1000))
print()

print("id()")
print(id(Person))
print()

print("id()")
print(id(Person))
print()

print("input()")
#x = input() # Allow user input
#print('Hello' + x)
print()

print("input()")
#x = input() # Allow user input
#print('Hello' + x)
print()

print("int()")
print(int(1.0))
print()

print("isinstance()")
print(isinstance(5, int))
print()

print("issubclass()")

class Doctor(Person):
    pass
print(issubclass(Doctor, Person))
print()

print("iter()")
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
print()

print("len()")
print(len("apple"))
print()

print("list()")
print(list(("apple", "banana", "cherry")))
print()

print("isinstance()")
x = locals()
print(x)
print()

print("map()")

def myFunc1(n):
    return len(n)

x = map(myFunc1, ('apple', 'banana', 'cherry'))
print(list(x))
print()

print("max()")
print(max('apple', 'banana', 'cherry'))
print()

print("memoryview()")
x = memoryview(b"Hello")
print(x[0])
print()

print("min()")
print(min('apple', 'banana', 'cherry'))
print()

print("next()")
x = iter(['apple', 'banana', 'cherry'])
print(next(x))
print()

print("object()")
x = object()
print(type(x))
print()

print("oct()")
print(oct(10))
print()

print("open()")
#f = open("demofile.txt", "r")
#print(f.read())
print()

print("ord()")
print(ord("h"))
print()

print("pow()")
print(pow(4,3)) # Same as 4 * 4 * 4
print()

print("print()")
print("Hey")
print()

print("property()")
#print(property(Person))
print()

print("range()")
x = range(6)
for n in x:
    print(n)
print()

print("repr()")
print(repr(Person))
print()

print("reversed()")
x = ['apple', 'banana', 'cherry']
print(list(reversed(x)))
print()

print("round()")
print(round(1.1))
print()

print("set()")
x = ['apple', 'banana', 'cherry']
print(set(x))
print()

print("setattr()")
setattr(Person, 'country', 'USA')
x = getattr(Person, 'country')
print(x)
print()

print("round()")
print(round(1.1))
print()

print("slice()")
a = ('a', 'b', 'c', 'd')
x = slice(2)
print(a[x])
print()

print("round()")
print(round(1.1))
print()

print("set()")
x = ['apple', 'banana', 'cherry']
print(set(x))
print()

print("sorted()")
x = ['apple', 'banana', 'cherry']
print(list(sorted(x)))
print()

print("staticmethod()") # Converts a mehtod into a static method
print()

print("str()")
print(str(1))
print()

print("sum()")
x = [2, 2, 2]
print(sum(x))
print()

print("super()") # Returns an object that represents the parent class
print()

print("tuple()")
x = ['apple', 'banana', 'cherry']
print(tuple(x))
print()

print("type()")
x = ['apple', 'banana', 'cherry']
print(type(tuple(x)))
print()

print("vars()")
x = vars(Person)
print(x)
print()

print("zip()")
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(list(x))
print()

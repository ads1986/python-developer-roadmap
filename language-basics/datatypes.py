Font : https://www.w3schools.com/python/python_datatypes.asp

#int
x = 5
print(type(x))
print()

#string
x = "Hello World"
print(type(x))
print()

#float
x = 20.5
print(type(x))
print()

#complex
x = 1j
print(type(x))
print()

#dict
z = {"fruit" : "mango", "price" : 5.0}
print(type(x))
print()

#list
x = ["apple", "banana", "cherry"]
print(type(x))
x[1] = "mango"
x.append("lemon")
print(x)
print(x.__sizeof__())
print()

#tuple
x = ("apple", "banana", "cherry")
print(type(x))
print(id(x))
x += ("lemon",) # We can't update an element, but we can add
print(x.__sizeof__()) # tuples size is smaller than list
print(id(x)) # here a new tuple object will be created
print(x)
z[x] = "fruits list" # We can't use list as key in a dictionary, only typle 
print(z)
print()

#range
x = range(6)
print(type(x))
print(list(x))
print()

#set
x = {"apple", "banana", "cherry"}
print(type(x))
x.add("mango")
print(x)
print()

#frozenset
x = frozenset({"apple", "banana", "cherry"}) # The set become immutable
print(type(x))
print(x)
print()

#bool
x = True
print(type(x))
x = False
print(x)
print()

#bytes
x = b"Hello"
print(type(x))
print(x)


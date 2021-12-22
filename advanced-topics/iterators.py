#Font: https://www.w3schools.com/python/python_iterators.asp

print("#Iterators") # Object which implements the iterator protocol (consists of metods __iter__() and __next__())
print()

print("#Iterator vs Iterable") # Lists, tuples, dictionaries and sets are iterable objects (all have iter())

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print()

print("#Strings are iterable too")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print()

print("#Loop Through an Iterator")

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

print()

print("#Iterable characters of a String")

mystr = "banana"

for x in mystr:
    print(x)

print()

print("#Create an Iterator")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
        
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print()

print("#StopIteration")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
      if self.a <= 20:  
        x = self.a
        self.a += 1
        return x
      else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
    
print()

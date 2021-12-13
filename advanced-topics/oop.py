#Font: https://www.w3schools.com/python/python_classes.asp

print("#Creating a Class")

class MyClass:
    x = 5
print()

print("#Creating an Object")

p1 = MyClass()
print(p1.x)
print()

print("#__init__()")

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print()

print("#methods")

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("John", 36)
p1.myfunc()
print()

print("#self")

class Person:
    def __init__(mysillyobject, name,age): # We can use any name, but neet to be the first param
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)
        
p1 = Person("John", 36)
p1.myfunc()
print()

print("#Modify Object Properties")

p1 = Person("John", 36)
p1.name = "Paul"
p1.myfunc()
print()

print("#Delete Object Properties")

x = "hello"

del x

#print(x)

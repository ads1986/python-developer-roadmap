#Font: https://www.w3schools.com/python/python_inheritance.asp

print("#Creating a Parent Class")

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John","Doe")
x.printname()
print()

print("#Creating a Child Class")

class Student(Person):
    pass

y = Student("John","Doe")
y.printname()

print()

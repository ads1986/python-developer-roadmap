#Font: https://www.geeksforgeeks.org/polymorphism-in-python/

print("#Polimorfirsm")

print("#Using Classes")
class Bird:
    def intro(self):
        print("Bird: There are many types of birds.")
        
    def flight(self):
        print("Bird: Most of the birds can fly but some cannot.")
        
class Sparrow(Bird):
    def flight(self):
        print("Sparrow: Sparrows can fly.")
        
class Ostrich(Bird):
    def flight(self):
        print("Ostrich: Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()
print()

obj_spr.intro()
obj_spr.flight()
print()

obj_ost.intro()
obj_ost.flight()
print()

print("#Using Classes and a Method")

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
        
    def language(self):
        print("Hindi is the most widely spoken language of India.")
        
    def type(self):
        print("India is a developing country.")
        
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
        
    def language(self):
        print("English is the primary language in USA.")
        
    def type(self):
        print("USA is a developed country.")
        
def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)

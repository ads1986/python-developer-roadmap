#Font: https://www.w3schools.com/python/python_modules.asp

print("#Create a module")
print()

def greeting(name):
    print("Hello, " + name)

import module_custom

module_custom.greeting("Anderson")

print()

print("#Variables in module")
print()

    
person1 = {
    "name" : "John",
    "age" : 36,
    "country" : "Norway"
}
    
a = module_custom.person1["age"]
print(a)

print()

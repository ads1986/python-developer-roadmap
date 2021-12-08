#Font1: https://www.w3schools.com/python/python_for_loops.asp
#Font2: https://www.w3schools.com/python/python_while_loops.asp

print("Loops")
print()

print("#Foor Loops")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print()

print("#Looping Through a String")
for x in "banana":
    print(x)
print()

print("#Break Statement")

for x in fruits:
    print(x) 
    if x == "banana":
      break
       
print()

print("#Break Statement")
for x in fruits:
    if x == "banana":
      break
    print(x)    
print()

print("#Continue Statement")

for x in fruits:
    if x == "banana":
      continue
    print(x) 

print()

print("#Range Function")      

for x in range(6):
    print(x)
print()

for x in range(2,6):
    print(x)
print()

for x in range(2,30,3):
    print(x)
print()

print("#Else in For Loop")      

for x in range(3):
    print(x)
else:
    print("Finally finished!")
    
print()

print("#Nested Loops")      

adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x,y)
    
print()

print("#Pass Statement")      

for x in [0, 1, 2]:# We can use 'pass' when a loop, method or other, no have a content and we want to avoid an error
    pass
    
print()

#Font: https://www.geeksforgeeks.org/functional-programming-in-python/

print("#Functional Programming")
print()

print("#Pure Function")

def pure_func(List):
    
    New_List = []
    
    for i in List:
        New_List.append(i**2)
        
    return New_List
    
Original_List = [1,2,3,4]
Modified_List = pure_func(Original_List)

print("Original List:", Original_List)
print("Modified List: ", Modified_List)

print()

print("#Recursion")

def Sum(L, i, n, count):

    if n <= i:
        return count
    
    count += L[i]
    
    count = Sum(L, i + 1, n, count)
    
    return count
    
L = [1,2,3,4,5]
count = 0
n = len(L)
print(Sum(L, 0, n, count))    

print()

print("#First-Class Functions")

def shout(text):
    return text.upper()
    
def whisper(text):
    return text.lower()
    
def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am create by a function passed as an argument")
    print(greeting)
    
greet(shout)
greet(whisper)

print()

print("#Built-in Higher-order functions")

print("#Map")

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
results = map(addition, numbers)

print(results)

for result in results:
    print(result, end = " ")

print()

print("#Filter")

def fun(variable):

    letters = ['a', 'e', 'i', 'o', 'u']
    
    if (variable in letters):
        return True
    else:
        return False
        
sequence = ['g', 'e', 'e', 'e', 'j', 'k', 's']

filtered = filter(fun, sequence)

print('The filtered letters are:')

for s in filtered:
    print(s)

print()

print("#Lambda")

cube = lambda x: x*x*x
print(cube(7))

L = [1,3, 2, 4, 5, 6]
is_even = [x for x in L if x % 2 == 0]

print(is_even)

print()

#immutable[1] = 'K'

print()

print("#Immutability")

immutable = "GeeksforGeeks"

#immutable[1] = 'K'

print()

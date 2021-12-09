#Font1: https://www.w3schools.com/python/python_ref_exceptions.asp
#Font2: https://www.w3schools.com/python/python_try_except.asp

print("Exception Handling")
try:
    x = 1 / 0
except:
    print("An exception ocurred")
print()

print("Many Exceptions")
try:
    print(x)
except NameError:
    print("NameError : Variable x is not defined")
except:
    print("Something else went wrong")
print()

print("Else")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print()

print("Finally")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("Nothing went wrong")
print()

print("Finally (Trying open a File)")
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
print()

print("Raise an Exception")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
    
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

print()

print("Getting type of Exception")
try:
    x = 1 / 0
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
print()

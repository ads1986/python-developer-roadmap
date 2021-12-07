#Font1 : https://www.w3schools.com/python/python_numbers.asp
#Font2 : https://www.w3schools.com/python/python_operators.asp
#Font3 : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators
#Font4 : https://techvidvan.com/tutorials/python-operator-precedence/

print("Numbers")
print()

print("#int") # Whole number, positive or negative, without decimals of unlimited length
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
print()

print("#float") # Positive or negative, containing one or more decimals
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
print()

print("#float2") # Can be scientific number with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print()

print("Operators")
print()

print("Addition")
x = 2 + 3
print(x)
print()

print("Subtraction")
x = 3 - 2
print(x)
print()

print("Multiplication")
x = 3 * 2
print(x)
print()

print("Division")
x = 6 / 2
print(x)
print()

print("Modulus")
x = 6 % 2 # calculate the remainder of the division
print(x)
print()

print("Exponentiation")
x = 2 ** 2
print(x)
print()

print("Floor division")
x = 7.5 / 2 # Round the result to floor
print(x)
print()

print("Assignment Operators")
print()

print("=")
x = 10
print(x)
print()

print("+= 1")
x += 1
print(x)
print()

print("-= 1")
x -= 1
print(x)
print()

print("*= 2")
x *= 2
print(x)
print()

print("/= 2")
x /= 2 # Even dividing int numbers, the result will be a float
print(x)
print()

print("%= 2")
x %= 2
print(x)
print()

print("= 7")
x = 7
print(x)
print("//= 2")
x //= 2
print(x)
print()

print("**= 2")
x **= 2
print(x)
print()

print("Bitwise - Is a level of operations that involves working with individual bits")
print()

print("= 5")
x = 5
print("&= 3")
x &= 3 # Do a bitwise AND operation using the binary representation of both numbers
print(x)
print()

print("= 5")
x = 5
print("|= 3")
x |= 3 # Do a bitwise OR operation using the binary representation of both numbers
print(x)
print()

print("= 5")
x = 5
print("|= 3")
x |= 3 # Do a bitwise OR operation using the binary representation of both numbers
print(x)
print()

print("= 5")
x = 5
print("^= 3")
x ^= 3 # Do a bitwise XOR operation using the binary representation of both numbers
print(x)
print()

print("= 5")
x = 5
print(">>= 3")
x >>= 3 # Right shift assiment operator that moves the specified amount of bit to the right and assigns the result to the variable
print(x)
print()

print("= 5")
x = 5
print("<<= 3")
x >>= 3 # Left shift assiment operator that moves the specified amount of bit to the right and assigns the result to the variable
print(x)
print()

print("Membership Operators")
print()

print("'apple' in y")
z = ["apple", "banana"]
print("apple" in z)
print()

print("'mango' not in y")
z = ["apple", "banana"]
print("mango" not in z)
print()

print("Bitwise Operators") # used to compare (binary) numbers
print()

x = 5
print("x = 5")
y = 5
print("y = 5")
print()

print("y & x")
print(y & x) # AND
print()

print("y | x")
print(y | x) # OR
print()

print("y ^ x")
print(y ^ x) # XOR
print()

#print("y ~ x")
#print(y ~ x) # NOT
#print()

print("y << x")
print(y << x) # Zero fill left shift
print()

print("y << x")
print(y << x) # Signed right shift
print()

print("Comparison Operators")
print()

x = 5
print("x = 5")
y = 5
print("y = 5")
print()

print("y == x")
print(x == x)
print()

print("y != x")
print(x != x)
print()

print("y > x")
print(x > x)
print()

print("y < x")
print(x < x)
print()

print("y >= x")
print(x >= x)
print()

print("y <= x")
print(x >= x)
print()

print("Identity Operators")
print()

a = ["apple", "banana"]
b = ["apple", "banana"]

print("a is b") # Compare only if is the same  object, with se same memory localtion. To compare the object content we use ==
print(a is b)
print()

print("a is not b") # Compare only if is the same object, with se same memory localtion. To compare the object content we use ==
print(a is b)
print()

print("Operators Precedence")
print()

print("Example")
x = ((((6+4)*2)-10)//2)-4*2
print(x)

print("Precedence Rule - PEMDAS")

print("(6+4) = 10")
print("(10*2) = 20")
print("(20-10) = 10")
print("(10//2) = 5")
print("4*2 = 8")
print("5-8 = -3")

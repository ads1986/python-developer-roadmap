#Font1: https://www.w3schools.com/python/python_file_handling.asp
#Font2: https://www.w3schools.com/python/python_file_open.asp
#Font3: https://www.w3schools.com/python/python_file_write.asp
#Font4: https://www.w3schools.com/python/python_file_remove.asp

print("#File I/O")
print()

print("#Create a New File")

f = open("myfile.txt", "a") # x - Create, returns error if file exists | a - create if not exist | x - create if not exists

print()

print("#Write to an Existing file")

f.write("")
f.write("Now the file has more content!")
f.close()

print()

print("#Reading a file")

f = open("myfile.txt", "r")
print(f.read())

print()

print("#Reading only Parts of the File")

f = open("myfile.txt", "r")
print(f.read(5))

print()

print("#Delete a File")

import os

f.close()
os.remove("myfile.txt")

print()

#Font: https://www.geeksforgeeks.org/working-with-the-python-debugger/

print("#Debugging")
print()

import pdb

print("#PDB")

pdb.set_trace()

n=5
for x in range(1,11):
    print(n, '*', x, '=', n*x)

print()

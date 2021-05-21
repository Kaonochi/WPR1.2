import re
import sys
import os

name = None
path = None
abs1 = None
some_directory = (sys.argv[1] if len(sys.argv) > 1 else ".")
i = 2
while i < len(sys.argv):
    x = sys.argv[i]
    if x == "-name":
        name = re.compile(sys.argv[i + 1])
        i += 1
    i += 1;



def iteracja(directory):
    ls = []
    for j in os.listdir(directory):
        j = os.path.join( directory, j)
        ls.append(j)

        if os.path.isdir(j):
            ls.extend(iteracja(j))
    return ls

a = iteracja(some_directory)


for each in a:
    if not name.search(each):
        continue
    print(each)




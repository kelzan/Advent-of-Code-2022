import re

header = True
numstacks = 0
stacks = []

def find_marker(m):
    mstart = 0
    for c in range(len(m)):
        mset = set(m[c:c+14])
        #print (m[c:c+4],mset)
        if (len(mset) == 14): # all unique
            mstart = c+14
            break
    return(mstart)

with open('day6a_input.txt', 'r') as fp:
    for line in fp:
        start = find_marker(line.strip())
        print(f"Marker start: {start}")
        
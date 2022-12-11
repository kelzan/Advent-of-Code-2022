def get_priority(x):
    if (x.islower()):
        p = abs(ord("a") - ord(x) - 1)
    else:
        p = abs(ord("A") - ord(x) - 27)
 #   print(f"{x}: {p}")
    return(p)

myfile = open('day3a_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

tally = 0

for i in range(0,len(lines),3):
    first = set(lines[i].strip())
    second = set(lines[i+1].strip())
    third = set(lines[i+2].strip())

    common = ''.join(set(first).intersection(set(second)))
    common = ''.join(set(common).intersection(set(third)))

    p = get_priority(common)
    tally += p
    print(f"{i} - common: {common}, priority: {p}, tally: {tally}")




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
game = 0

for line in lines:
    line = line.strip()
    index = len(line)//2
    #print (index)
    first = line[0:index]
    second = line[index:]
    #print(line, len(line), index, first, second)
    common = ''.join(set(first).intersection(set(second)))
    p = get_priority(common)
    tally += p
    print(f"common: {common}, priority: {p}, tally: {tally}")

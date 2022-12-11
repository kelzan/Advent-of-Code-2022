print ("Hello World")

myfile = open('day1a_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

tally = 0
elfnum = 1
elflist = []

for i in range(len(lines)):
    line = lines[i].strip()
    if (line == ""):
        print(f"elfnum {elfnum} has {tally}")
        elfnum += 1
        elflist.append(tally)
        tally = 0
    else:
        tally += int(line)

elflist.sort(reverse=True)
print(elflist[0:3])
#print(elflist)
print (f"sum: {sum(elflist[0:3])}")
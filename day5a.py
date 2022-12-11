import re

header = True
numstacks = 0
stacks = []

def print_stacks():
    tallest = max([len(i) for i in stacks])
    for row in range(tallest-1,-1,-1):
        for stack in range(numstacks):
            #print(f"[{stack}][{row}]")
            if (row < len(stacks[stack])):
                print(f"[{stacks[stack][row]}]",end="")
            else:
                print("   ",end="")
        print()
    for row in range(numstacks):
        print(f" {row+1} ",end="")
    print()

with open('day5a_input.txt', 'r') as fp:
    for line in fp:
        if (header):
            if (numstacks == 0):
                numstacks = len(line)//4
                print(f"Stacks found: {numstacks}")
                for i in range(numstacks):
                    stacks.append([])
            boxes = line[1::4]
            #print(boxes)
            if (boxes.isdigit()):
                header = False
                print_stacks()
            else:
                for i in range(len(boxes)):
                    if (boxes[i] != ' '):
                        #stacks[i].append(boxes[i])
                        stacks[i].insert(0,boxes[i])


        else:
            match = re.search(r"^move (.*) from (.*) to (.*)", line.strip())
            if match:
                #print(f"found! {match.group(0)} {match.group(1)} {match.group(2)}")
                num = int(match.group(1))
                src = int(match.group(2))
                dst = int(match.group(3))
                print(f"moving {num} boxes from {src} to {dst}")
                for n in range(num):
                    stacks[dst-1].append(stacks[src-1].pop())
                    print_stacks()
                #print(elf1, elf2)
            #else:
            #    print(f"Bad input: {line}")

#print(stacks)
print_stacks()
top = ''.join([i[len(i)-1] for i in stacks])
print (top)
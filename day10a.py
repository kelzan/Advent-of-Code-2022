ops = []
X = 1
cycle = 0
update = False
tot_ss = 0

def print_status():
    print(f"cycle: {cycle}, X: {X}, {opcode} {arg}")

def increment_cycle():
    global cycle
    global tot_ss

    cycle += 1
    print_status()
    #if (cycle%20 == 0):
    if (cycle in [20, 60, 100, 140, 180, 220]):
        ss = cycle * X
        tot_ss += ss
        print(f"Signal Strength: {ss}, Total: {tot_ss}")

with open('day10a_input.txt', 'r') as fp:
    for line in fp:
        os = line.strip().split(" ")
        if (len(os)>1):
            ops.append([os[0], int(os[1])])
        else:
            ops.append([os[0],0])

print(ops)

for opcode,arg in ops:
    increment_cycle()

    if (opcode == "addx"):
        increment_cycle()
        X+=arg

print(f"Signal Strength: {tot_ss}")
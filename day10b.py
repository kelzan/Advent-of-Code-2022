ops = []
X = 1
cycle = 0
update = False
screen_line = ""
screen = []

def print_status():
    print(f"cycle: {cycle}, X: {X}, {opcode} {arg}")

def get_pixel():
    column = (cycle-1)%40
    if ((column >= X-1) and (column <= X+1)):
        return('#')
    else:
        return('.')

def increment_cycle():
    global cycle
    global tot_ss
    global screen_line
    global screen

    cycle += 1
    #print_status()
    screen_line += get_pixel()
    #print(f"column: {(cycle-1)%40}, X: {X}, sprite: {X-1}-{X+1}, pixel: {screen_line[-1]}")
    #print(screen_line)
    if ((cycle-1)%40 == 39):
        screen.append(screen_line)
        screen_line = ""


with open('day10a_input.txt', 'r') as fp:
    for line in fp:
        os = line.strip().split(" ")
        if (len(os)>1):
            ops.append([os[0], int(os[1])])
        else:
            ops.append([os[0],0])

#print(ops)

for opcode,arg in ops:
    increment_cycle()

    if (opcode == "addx"):
        increment_cycle()
        X+=arg

for i in range(len(screen)):
    print(screen[i])


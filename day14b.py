import numpy as np
import sys


structure = []

def print_map():
    global map
    #print(map)
    for row in map:
        for col in row:
            print(col,end="")
        print()
    print()

# Parse input file
with open('day14a_exam.txt', 'r') as fp:
    for line in fp:
        moves = line.strip().split(' -> ')
        #print(moves)
        newrow = []
        for move in moves:
            pair = move.split(',')
            if (len(pair) != 2):
                print(f"BAD LINE {move} {pair}")
                sys.exit()
            
            newrow.append((int(pair[0]),int(pair[1])))
        structure.append(newrow)

#print(structure)

# Now figure out what size the overal map data structure should be
max_x = -1
min_x = -1
max_y = -1
min_y = -1

for s in structure:
    for move in s:
        if ((max_x < 0) or (move[0] > max_x)):
            max_x = move[0]
        if ((min_x < 0) or (move[0] < min_x)):
            min_x = move[0]
        if ((max_y < 0) or (move[1] > max_y)):
            max_y = move[1]
        if ((min_y < 0) or (move[1] < min_y)):
            min_y = move[1]

x_dim = max_x - min_x + 3
x_offset = min_x - 1
y_dim = max_y + 3

if ((500-x_offset) < y_dim):
    adjust = y_dim - (500-x_offset) + 1
    x_dim += adjust
    x_offset -= adjust

if ((x_dim - (500-x_offset)) < y_dim):
    adjust= (y_dim - (x_dim - (500-x_offset))) + 1
    x_dim += adjust

print(max_x,min_x,max_y,min_y, x_dim, y_dim, x_offset)
#print(structure)

# Create the data structure

map = np.full(((y_dim,x_dim)),".",dtype=np.str)

map[0,500-x_offset] = '+'
#print_map()

# Now 'paint' in the structural features
for s in structure:
    curpoint = s[0]
    for moves in s:
        if (curpoint[1]<=moves[1]):
            y_step = 1
        else:
            y_step = -1
        if (curpoint[0]<=moves[0]):
            x_step = 1
        else:
            x_step = -1
        for row in range(curpoint[1],moves[1]+y_step,y_step):
            for col in range(curpoint[0],moves[0]+x_step,x_step):
                #print(f"Move: {row},{col}")
                map[row,col-x_offset] = '#'
        curpoint = moves

# Paint in the floor
for col in range(0,x_dim):
    map[y_dim-1,col] = '#'
print_map()
#sys.exit()

filled = False
sand_cnt = 0

# Now start dropping sand particles, and tracking where they'll end up
while not filled:
    sand_x = 500 - x_offset
    sand_y = 0

    falling = True
    while (falling):
        if (map[sand_y+1,sand_x] == '.'): # clear below
            sand_y += 1
        elif (map[sand_y+1,sand_x-1] == '.'):
            sand_y += 1
            sand_x -= 1
        elif (map[sand_y+1,sand_x+1] == '.'):
            sand_y += 1
            sand_x += 1
        else:
            map[sand_y,sand_x] = 'o'
            sand_cnt += 1
            falling = False
        if (sand_y == 0):
            print("FILLED!")
            filled = True
            falling = False
    #print_map()

print_map()
print(f"Sand count: {sand_cnt}")        
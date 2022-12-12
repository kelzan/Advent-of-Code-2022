import sys

map = []
map_x = 0
map_y = 0
start_x = 0
end_x = 0
start_y = 0
end_y = 0

lowlands = []

cur_minimum = 1000000

class node:
    def __init__(self, elevation):
        self.elevation = elevation
        self.path_to_here = []
        self.end = False
        self.start = False
        self.coord = ((0,0))

        if (self.elevation == 'S'):
            self.start = True
            self.elevation = 'a'
        if (self.elevation == 'E'):
            self.end = True
            self.elevation = 'z'

    def pchar(self):
        if (self.start):
            return('S')
        elif (self.end):
            return('E')
        else:
            return(self.elevation)

    def try_all_moves(path):
        None

    def can_move(self,src,dest):
        if (ord(dest) <= ord(src)+1):
            return(True)
        else:
            return(False)

    def try_moves(self,path):
        if ((len(self.path_to_here) > 0) and (len(path)+1>=len(self.path_to_here))):
            return

        self.path_to_here = path.copy()
        self.path_to_here.append(self.coord)

        #print("Try moves:",self.coord,path)
        # Stop now if at end
        if (self.end):
            return

        if (len(self.path_to_here) > cur_minimum):
            return

        # Right
        if (self.coord[1] < map_x-1):
            if (self.can_move(self.elevation, map[self.coord[0]][self.coord[1]+1].elevation)):
                map[self.coord[0]][self.coord[1]+1].try_moves(self.path_to_here)
        # Down
        if (self.coord[0] < map_y-1):
            if (self.can_move(self.elevation, map[self.coord[0]+1][self.coord[1]].elevation)):
                map[self.coord[0]+1][self.coord[1]].try_moves(self.path_to_here)
        # Left
        if (self.coord[1] > 0):
            if (self.can_move(self.elevation, map[self.coord[0]][self.coord[1]-1].elevation)):
                map[self.coord[0]][self.coord[1]-1].try_moves(self.path_to_here)
        # Up
        if (self.coord[0] > 0):
            if (self.can_move(self.elevation, map[self.coord[0]-1][self.coord[1]].elevation)):
                map[self.coord[0]-1][self.coord[1]].try_moves(self.path_to_here)

def print_map():
    for row in range(len(map)):
        for col in range(len(map[row])):
            print(map[row][col].pchar(),end='')
        print()
    print()

def clear_map():
    for row in range(len(map)):
        for col in range(len(map[row])):
            map[row][col].path_to_here = []

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
with open('day12a_input.txt', 'r') as fp:
    for line in fp:
        line = line.strip()
        newrow = []
        for c in line:
            newrow.append(node(c))
        map.append(newrow)

for row in range(len(map)):
    for col in range(len(map[row])):
        map[row][col].coord = ((row,col))
        if (map[row][col].end):
            end_x = col
            end_y = row
        if (map[row][col].start):
            start_x = col
            start_y = row
        if (map[row][col].elevation == 'a'):
            lowlands.append((row, col))

map_x = len(map[0])
map_y = len(map)

print(f"map_x: {map_x}, map_y: {map_y}, start: ({start_y},{start_x}), end: ({end_y},{end_x})")
print_map()

total_locs = len(lowlands)
print(f"Checking {total_locs} starting locations")

steps = []
numloc = 1

for sloc in lowlands:
    print(f"Checking {numloc}/{total_locs} ({(float(numloc)/total_locs):.0%}): {sloc}...")
    numloc += 1
    map[sloc[0]][sloc[1]].try_moves([])
    #print("Path to end:",map[end_y][end_x].path_to_here)
    numsteps = len(map[end_y][end_x].path_to_here)-1
    print(f"Steps: {numsteps}, current minimum: {cur_minimum}")
    if (numsteps > 0):
        steps.append(numsteps)
        if (numsteps < cur_minimum):
            cur_minimum = numsteps
    clear_map()

steps.sort()
print(steps)
print(f"Shortest path: {steps[0]}")
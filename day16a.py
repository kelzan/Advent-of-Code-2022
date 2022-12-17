import re
import sys
import time
import itertools

valves = {}
start = ""
num_minutes = 30
active_valves = []
num_active_valves = 0
max_pressure = 0
finish_mask = 0

class valve:
    def __init__(self, name, flow, cons):
        self.name = name
        self.flow = flow
        self.cons = cons
        self.open = False
        self.explored = False
        self.parent = None
        self.index = None
        self.distances = {}
        
    def show_it(self):
        #cnames = [x.name for x in self.cons]
        print(f"Valve {self.name}, Flow: {self.flow}, Cons: {self.cons}")

def set_bit(num, position):
    """Sets the bit at the given position in num to 1.
    
    Args:
    num: An integer.
    position: An integer representing the position of the bit to set. The
        least significant bit is at position 0.
    
    Returns:
    An integer with the bit at the given position set to 1.
    """
    # Create a mask with all bits set to 0 except for the bit at the given position
    mask = 1 << position
    # OR the mask with the number to set the bit at the given position to 1
    return num | mask

def is_bit_set(num, position):
    """Returns True if the bit at the given position in num is set to 1, False otherwise.
    
    Args:
    num: An integer.
    position: An integer representing the position of the bit to check. The
        least significant bit is at position 0.
    
    Returns:
    A boolean indicating whether the bit at the given position is set to 1.
    """
    # Shift the number right by the given position, and check if the least significant bit is set to 1
    return (num >> position) & 1 == 1

def clear_valves():
    for k,v in valves.items():
        v.explored = False
        v.parent = None

def distance(start, finish):
    clear_valves()
    Q = []
    valves[start].explored = True
    Q.append(start)
    while(len(Q)):
        v = Q.pop()
        #print(f"Processing {v}")
        if (v == finish):
            #print(f"FOUND Path")
            cur_name = v
            dist = 0
            while (cur_name != start):
                #print(f"{cur_name} -> ",end="")
                cur_name = valves[cur_name].parent
                dist += 1
            #print(start)
            #print(f"Distance: {dist}")
            return(dist)
        for path in valves[v].cons:
            if (not valves[path].explored):
                valves[path].explored = True
                valves[path].parent = v
                Q.append(path)

def calculate_pressure(start,path):
    prev_position = start
    total_p = 0
    ppm = 0
    minutes = 0
    for v in path:
        d = distance(prev_position,v)
        minutes += d + 1
        total_p += ppm*(d+1)
        ppm += valves[v].flow
        #print(f"{prev_position}->{v}, minutes: {minutes}, dist: {d}, ppm: {ppm}, total_p: {total_p}")
        prev_position = v
    total_p += ppm*(num_minutes-minutes)
    #print(f"total_p: {total_p}")
    return(total_p)

tries = 0
def move_it(start, end, minutes, ppm, total_p, valve_map, path):
    global max_pressure
    global valves
    global tries

    if (start != None): # Is this the very beginning?
        distance = valves[start].distances[end]
        total_p += ppm*(distance+1)
        minutes += (distance + 1)
        ppm += valves[end].flow
        print(f"Moved {start} to {end} (d:{distance}), minutes: {minutes}, total_p: {total_p}, ppm: {ppm}")
    else:
        print("STARTING")
    moved = False
    for k,v in valves[end].distances.items():
        if (minutes+v+1)>30: # Don't go if not enough time
            continue
        if (is_bit_set(valve_map, valves[k].index)): # Don't go if already set
            continue
        new_map = set_bit(valve_map, valves[k].index)
        new_path = path.copy()
        new_path.append(k)
        move_it(end, k, minutes, ppm, total_p, new_map, new_path)
        moved = True
    if not moved:
        total_p += ppm * (30-minutes)
        print(f"Finished Journey ({30-minutes} minutes more) at {end}, total_p: {total_p}")
        if (tries>5):
            sys.exit()
        tries += 1
        if (total_p > max_pressure):
            max_pressure = total_p
            print(f"New max: {max_pressure} {path}")
            #sys.exit()




with open('day16a_input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^Valve (.*) has flow rate=(.*); tunnel[s]* lead[s]* to valve[s]* (.*)", line.strip())
        if (match):
            name = match.group(1)
            cons = match.group(3).split(', ')
            v = valve(name, int(match.group(2)), cons)
            valves[name] = v
            if (v.flow):
                active_valves.append(name)
#            if (start == ""):
#                start = name
#                if start not in active_valves:
#                    active_valves.append(start)
        else:
            print(f"BAD INPUT {line}")
            sys.exit()

start = "AA"

print(f"Active valves: {active_valves}")

for v in valves.values():
    v.show_it()

# for x in valves.keys():
#     for y in valves.keys():
#         print(f"Distance from {x} to {y} is {distance(x,y)}")
        #distance(x,y)

# Precalculate all distances

for v in valves.keys():
    for dest_v in active_valves:
        valves[v].distances[dest_v] = distance(v,dest_v)
    print(f"{v}",valves[v].distances)

i_cnt = 0
for av in active_valves:
    i_cnt += 1
    valves[av].index = i_cnt
    #print(f"Distance from {start} to {av} is {distance(start,av)}")

num_active_valves = len(active_valves)
finish_mask = (1 << num_active_valves)-1
print(f"active valve number: {len(active_valves)} finish_mask: {finish_mask}")

move_it(None, start, 0, 0, 0, 0, [])

print(f"max_pressure: {max_pressure}")

import re
import sys
import time
import itertools

valves = {}

class valve:
    def __init__(self, name, flow, cons):
        self.name = name
        self.flow = flow
        self.cons = cons
        self.open = False
        self.explored = False
        self.parent = None
        
    def show_it(self):
        #cnames = [x.name for x in self.cons]
        print(f"Valve {self.name}, Flow: {self.flow}, Cons: {self.cons}")

start = ""
max_pressure = 0
num_minutes = 30

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



active_valves = []
max_pressure = 0

with open('day16_input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^Valve (.*) has flow rate=(.*); tunnel[s]* lead[s]* to valve[s]* (.*)", line.strip())
        if (match):
            name = match.group(1)
            cons = match.group(3).split(', ')
            v = valve(name, int(match.group(2)), cons)
            valves[name] = v
            if (start == ""):
                start = name
            if (v.flow):
                active_valves.append(name)
        else:
            print(f"BAD INPUT {line}")
            sys.exit()

print(f"Active valves: {active_valves}")

for v in valves.values():
    v.show_it()

# for x in valves.keys():
#     for y in valves.keys():
#         print(f"Distance from {x} to {y} is {distance(x,y)}")
        #distance(x,y)

for av in active_valves:
    print(f"Distance from {start} to {av} is {distance(start,av)}")
sys.exit()
permies = (list(itertools.permutations(active_valves)))
print("total permutations: {len(permies)}")
#test = ('DD', 'BB', 'JJ', 'HH', 'EE', 'CC')
#for t in test:
#    print(t)

pcnt = 0
for p in permies:
    pressure = calculate_pressure(start,p)
    if (pressure>max_pressure):
        max_pressure = pressure
    pcnt += 1
    if (pcnt%100 == 0):
        print(pcnt)

print(f"max_pressure: {max_pressure}")

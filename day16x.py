import re
import sys
import time

valves = {}

class valve:
    def __init__(self, name, flow, cons):
        self.name = name
        self.flow = flow
        self.cons = cons
        self.open = False
        
    def show_it(self):
        #cnames = [x.name for x in self.cons]
        print(f"Valve {self.name}, Flow: {self.flow}, Cons: {self.cons}")

start = ""
max_pressure = 0

def move_it(valve, minute, ppm, ptot, vopen):
    global max_pressure
    minute += 1
    print(f"== Minute {minute} ==")

    ptot += ppm

    if (vopen == active_valves):
        ptot += (30-minute)*ppm
        minute = 30

    if (minute == 30):
        if (ptot > max_pressure):
            max_pressure = ptot
            print(f"New max: {max_pressure}")

    else:
        if ((valve.flow) and not valve.open):
            valve.open = True
            vopen += 1
            ppm += valve.flow
            move_it(valve, minute, ppm, ptot, vopen)
            for move in valve.cons:
                move_it(valves[move], minute, ppm, ptot, vopen)
            valve.open = False
            vopen -= 1
            ppm -= valve.flow
        for move in valve.cons:
            move_it(valves[move],minute, ppm, ptot, vopen)

    # Try setting and moving, then not setting and moving, both are legal



active_valves = 0
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
with open('day16a_exam.txt', 'r') as fp:
    for line in fp:
        #print(line.strip())
        match = re.search(r"^Valve (.*) has flow rate=(.*); tunnel[s]* lead[s]* to valve[s]* (.*)", line.strip())
        if (match):
            name = match.group(1)
            cons = match.group(3).split(', ')
            v = valve(name, int(match.group(2)), cons)
            valves[name] = v
            if (start == ""):
                start = name
            if (v.flow):
                active_valves += 1
        else:
            print(f"BAD INPUT {line}")
            sys.exit()

print(f"Active valves: {active_valves}")

for v in valves.values():
    v.show_it()

move_it(valves[start],1,0,0,0)


import copy

map = []

with open('day8a_input.txt', 'r') as fp:
    for line in fp:
        row = [int(x) for x in line.strip()]
        map.append(row)

print(map)
#sys.exit()
xd = len(map[0])
yd = len(map)
print(f"dimensions: {xd},{yd}")
#sys.exit()

vmap = copy.deepcopy(map)

for ya in range(yd):
    for xa in range(xd):
        vmap[ya][xa] = 0
        if ((xa == 0) or (ya == 0) or (xa == xd-1) or (ya == yd-1)):
            vmap[ya][xa] = 1
        else:
            # Check left
            for x in range(xa-1,-1,-1):
                #print(f"For [{ya},{xa}] {map[ya][xa]} checking left [{ya},{x}] {map[ya][x]}")
                path = True
                if (map[ya][x] >= map[ya][xa]):
                    #print("Blocked!")
                    path = False
                    break
            # Check right 
            if (not path):
                path = True
                for x in range(xa+1,xd):
                    #print(f"For [{ya},{xa}] checking right [{ya},{x}]")
                    if (map[ya][x] >= map[ya][xa]):
                        #print("Blocked!")
                        path = False
                        break
            # Check up
            if (not path):
                path = True
                for y in range(ya-1,-1,-1):
                    #print(f"For [{ya},{xa}] checking up [{y},{xa}]")
                    if (map[y][xa] >= map[ya][xa]):
                        #print("Blocked!")
                        path = False
                        break
            # Check down
            if (not path):
                path = True
                for y in range(ya+1,yd):
                    #print(f"For [{ya},{xa}] checking down [{y},{xa}]")
                    if (map[y][xa] >= map[ya][xa]):
                        path = False
                        #print("Blocked!")
                        break
            if (path):
                #print(f"Path found for [{ya}][{xa}]")
                vmap[ya][xa] = 1                    

print(map)
print(vmap)
print(f"visible: {sum(sum(vmap,[]))}")
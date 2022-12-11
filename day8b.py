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
        score_left = 0
        score_right = 0
        score_up = 0
        score_down = 0
        # Check left
        for x in range(xa-1,-1,-1):
            score_left += 1
            #print(f"For [{ya},{xa}] {map[ya][xa]} checking left [{ya},{x}] {map[ya][x]}")
            if (map[ya][x] >= map[ya][xa]):
                #print("Blocked!")
                break
            #print(f"score_left: {score_left}")
        # Check right 
        for x in range(xa+1,xd):
            score_right += 1
            #print(f"For [{ya},{xa}] checking right [{ya},{x}]")
            if (map[ya][x] >= map[ya][xa]):
                #print("Blocked!")
                break
        # Check up
        for y in range(ya-1,-1,-1):
            score_up += 1
            #print(f"For [{ya},{xa}] checking up [{y},{xa}]")
            if (map[y][xa] >= map[ya][xa]):
                #print("Blocked!")
                break
        # Check down
        for y in range(ya+1,yd):
            score_down += 1
            #print(f"For [{ya},{xa}] checking down [{y},{xa}]")
            if (map[y][xa] >= map[ya][xa]):
                #print("Blocked!")
                break

        #print(f"[{ya}][{xa}] - left: {score_left} right: {score_right} up: {score_up} down: {score_down}")
        vmap[ya][xa] = score_left * score_right * score_up * score_down                   

print(map)
print(vmap)
maxval = 0
for y in range(yd):
    for x in range(xd):
        if (vmap[y][x] > maxval):
            maxval = vmap[y][x]
print(f"max val: {maxval}")
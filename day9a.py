
locs = set()
moves = []

curposx = 0
curposy = 0
headx = 0
heady = 0
tailx = 0
taily = 0

def printpos():
    print(f"Head: ({headx},{heady}), Tail: ({tailx},{taily})")
    

with open('day9a_input.txt', 'r') as fp:
    for line in fp:
        dir, steps = line.strip().split(" ")
        moves.append([dir, int(steps)])

print(moves)

locs.add((curposx,curposy))
printpos()

for dir,steps in moves:
    #print(dir,steps)

    for m in range(steps):
        #first move head
        if (dir=='R'):
            headx += 1
        elif (dir=='L'):
            headx -= 1
        elif (dir=='U'):
            heady += 1
        elif (dir=='D'):
            heady -= 1
        else:
            print("BAD DIRECTION")
        #printpos()

        # Now move tail
        xdiff = headx-tailx
        ydiff = heady-taily
        #print(f"xdiff:{xdiff} ydiff:{ydiff}")
        if (((abs(xdiff)>=2) and (ydiff != 0)) or ((abs(ydiff)>=2) and (xdiff != 0))): # Two direction adjustment
            if (xdiff>=2):
                tailx+=1
                taily+=ydiff
            elif (xdiff<=-2):
                tailx-=1
                taily+=ydiff
            elif (ydiff>=2):
                taily+=1
                tailx+=xdiff
            elif (ydiff<=-2):
                taily-=1
                tailx+=xdiff   
        else: # One direction adjustment
            if (xdiff>=2):
                tailx+=1
            elif (xdiff<=-2):
                tailx-=1
            elif (ydiff>=2):
                taily+=1
            elif (ydiff<=-2):
                taily-=1

        #printpos()

        # Now log current position
        locs.add((tailx, taily))

print(locs)
print(f"Num locations: {len(locs)}")


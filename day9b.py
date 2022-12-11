
locs = set()
moves = []
knots =  []

def update_pos(head, tail):
    # Now move tail
    xdiff = head[0]-tail[0]
    ydiff = head[1]-tail[1]
    #print(head,tail)
    #print(f"xdiff:{xdiff} ydiff:{ydiff}")
    if (((abs(xdiff)>=2) and (ydiff != 0)) or ((abs(ydiff)>=2) and (xdiff != 0))): # Two direction adjustment
        if (xdiff>=2):
            tail[0]+=1
            if (ydiff>0):
                tail[1]+=1
            else:
                tail[1]-=1
        elif (xdiff<=-2):
            tail[0]-=1
            if (ydiff>0):
                tail[1]+=1
            else:
                tail[1]-=1
        elif (ydiff>=2):
            tail[1]+=1
            if (xdiff>0):
                tail[0]+=1
            else:
                tail[0]-=1
        elif (ydiff<=-2):
            tail[1]-=1
            if (xdiff>0):
                tail[0]+=1
            else:
                tail[0]-=1   
    else: # One direction adjustment
        if (xdiff>=2):
            tail[0]+=1
        elif (xdiff<=-2):
            tail[0]-=1
        elif (ydiff>=2):
            tail[1]+=1
        elif (ydiff<=-2):
            tail[1]-=1

    #print(head,tail)

def printpos():
    #print(f"Head: ({knots[0][0]},{knots[0][1]}), Tail: ({knots[9][0]},{knots[9][1]})")
    print(knots)
    

with open('day9a_input.txt', 'r') as fp:
    for line in fp:
        dir, steps = line.strip().split(" ")
        moves.append([dir, int(steps)])

print(moves)

# knots 0 is the head, knots 9 is the tail
for x in range(10):
    knots.append([0,0])

locs.add((knots[9][0], knots[9][1]))
#printpos()

for dir,steps in moves:
    #print(dir,steps)

    for m in range(steps):
        #first move head
        if (dir=='R'):
            knots[0][0] += 1
        elif (dir=='L'):
            knots[0][0] -= 1
        elif (dir=='U'):
            knots[0][1] += 1
        elif (dir=='D'):
            knots[0][1] -= 1
        else:
            print("BAD DIRECTION")
        #printpos()

        for k in range(9):
            update_pos(knots[k],knots[k+1])

        #printpos()

        # Now log current position
        locs.add((knots[9][0], knots[9][1]))

print(locs)
print(f"Num locations: {len(locs)}")


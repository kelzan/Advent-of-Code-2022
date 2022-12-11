myfile = open('day2a_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

tally = 0
game = 0

for line in lines:
    x = line.strip().split(" ")
    theirs = x[0]
    mine = x[1]
    score = 0
    game += 1
    #print(theirs,mine)
    if (theirs == "A"):
        if (mine == "X"):
            score = 3
        elif (mine == "Y"):
            score = 6
        elif (mine == "Z"):
            score = 0
    elif (theirs == "B"):
        if (mine == "X"):
            score = 0
        elif (mine == "Y"):
            score = 3
        elif (mine == "Z"):
            score = 6
    elif (theirs == "C"):
        if (mine == "X"):
            score = 6
        elif (mine == "Y"):
            score = 0
        elif (mine == "Z"):
            score = 3
    #print(score, ord("Z"), ord(mine))
    score += abs((ord("X") - ord(mine) - 1))
    tally += score
    print(f"Game {game}: Score {score}, total: {tally}")
    



"""
    direction = x[0]
    amount = int(x[1])
    print(f"d: {direction}, a: {amount}, {horz} {vert}")
    if (direction == "forward"):
        horz += amount
    elif (direction == "down"):
        vert += amount
    elif (direction == "up"):
        vert -= amount
    else:
        print (f"Problem with line: {line}")
answer = horz * vert
print(f"horizontal: {horz}, vertical: {vert}, product: {answer}")
"""
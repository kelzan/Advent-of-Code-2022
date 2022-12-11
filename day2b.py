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

    # rock: 1, paper: 2, scissors: 3
    # lose: 0, draw: 3, win: 6

    if (theirs == "A"): # rock
        if (mine == "X"): # lose - scissors
            score = 3
        elif (mine == "Y"): # draw - rock
            score = 4
        elif (mine == "Z"): # win - paper
            score = 8
    elif (theirs == "B"): # paper
        if (mine == "X"): # lose - rock
            score = 1
        elif (mine == "Y"): # draw - paper
            score = 5
        elif (mine == "Z"): # win - scissors
            score = 9
    elif (theirs == "C"): # scissors
        if (mine == "X"): # lose - paper
            score = 2
        elif (mine == "Y"): # draw - scissors
            score = 6
        elif (mine == "Z"): # win - rock
            score = 7
    #print(score, ord("Z"), ord(mine))

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
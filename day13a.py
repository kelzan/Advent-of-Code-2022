import sys

# -1 wrong, 1 right, 0 dunno
def compare(left, right, level=0):
    pad = ' '*level
    level += 2

    print(f"{pad}- Compare {left} vs {right}")

    if (len(left) == 0):
        if (len(right) == 0):
            return(0)
        else:
            print(f"{pad}- Left side ran out of items, so inputs are in the right order")
            return(1)

    for i in range(len(left)):
        if (i >= len(right)):
            print(f"{pad}- Right side ran out of items, so inputs are not in the right order")
            return(-1)
        print(f"{pad}- Compare {left[i]} vs {right[i]}")
        if (type(left[i]) is int):
            if (type(right[i]) is int): # both int
                if (left[i] == right[i]):
                    continue
                elif (left[i] > right[i]):
                    print(f"{pad}- Left side is larger, so inputs are not in right order")
                    return(-1)
                else:
                    print(f"{pad}- Right side is smaller, so inputs are in right order")
                    return(1)
            else: # left is int, right is list
                left[i] = [left[i]]
                print(f"{pad}- Mixed types; convert left to {left[i]} and retry comparison")
                retval = compare(left[i], right[i], level)
                if (retval != 0):
                    return(retval)
        elif (type(left[i]) is list):
            if (type(right[i]) is list): # Both list
                retval = compare(left[i], right[i], level)
                #print(f"retval: {retval}")
                if (retval != 0):
                    return(retval)
            else: # Left is list, right is int
                right[i] = [right[i]]
                print(f"{pad}- Mixed types; convert right to {right[i]} and retry comparison")                
                retval = compare(left[i], right[i], level)
                if (retval != 0):
                    return(retval)
    
    if (len(left) < len (right)):
        print(f"{pad}- Left side ran out of items, so inputs are in the right order")
        return(1)

    return(0)

myfile = open('day13a_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

pairnum = 0
numcorrect =[]
numwrong =[]
trouble = 0

for i in range(0,len(lines),3):
    arg1 = eval(lines[i].strip())
    arg2 = eval(lines[i+1].strip())
    #print(arg1)
    #print(arg2)
    pairnum += 1

    print(f"== Pair {pairnum} ==")
    correct = compare(arg1, arg2)
    if (correct == 1):
        numcorrect.append(pairnum)
    elif (correct == -1):
        numwrong.append(pairnum)
    else:
        print("TROUBLE")
        trouble += 1
    print()

print(numcorrect)
print(f"correct: {len(numcorrect)} - sum: {sum(numcorrect)}, wrong: {len(numwrong)}, trouble: {trouble}")


import sys
import copy

# -1 wrong, 1 right, 0 dunno
def compare(left, right, level=0):
    pad = ' '*level
    level += 2

    #print(f"{pad}- Compare {left} vs {right}")

    if (len(left) == 0):
        if (len(right) == 0):
            return(0)
        else:
            #print(f"{pad}- Left side ran out of items, so inputs are in the right order")
            return(1)

    for i in range(len(left)):
        if (i >= len(right)):
            #print(f"{pad}- Right side ran out of items, so inputs are not in the right order")
            return(-1)
        #print(f"{pad}- Compare {left[i]} vs {right[i]}")
        if (type(left[i]) is int):
            if (type(right[i]) is int): # both int
                if (left[i] == right[i]):
                    continue
                elif (left[i] > right[i]):
                    #print(f"{pad}- Left side is larger, so inputs are not in right order")
                    return(-1)
                else:
                    #print(f"{pad}- Right side is smaller, so inputs are in right order")
                    return(1)
            else: # left is int, right is list
                left[i] = [left[i]]
                #print(f"{pad}- Mixed types; convert left to {left[i]} and retry comparison")
                retval = compare(left[i], right[i], level)
                if (retval != 0):
                    return(retval)
        elif (type(left[i]) is list):
            if (type(right[i]) is list): # Both list
                retval = compare(left[i], right[i], level)
                if (retval != 0):
                    return(retval)
            else: # Left is list, right is int
                right[i] = [right[i]]
                #print(f"{pad}- Mixed types; convert right to {right[i]} and retry comparison")                
                retval = compare(left[i], right[i], level)
                if (retval != 0):
                    return(retval)
    
    if (len(left) < len (right)):
        #print(f"{pad}- Left side ran out of items, so inputs are in the right order")
        return(1)

    return(0)

myfile = open('day13a_input.txt', 'r')
lines = myfile.readlines()
myfile.close()

pairnum = 0
numcorrect =[]
numwrong =[]
trouble = 0

signals = []

for i in range(0,len(lines),3):
    signals.append(eval(lines[i].strip()))
    signals.append(eval(lines[i+1].strip()))
signals.append([[2]])
signals.append([[6]])

for loop in range(len(signals)):
#for loop in range(1):
    print(f"------------- Iteration: {loop} -------------------")
    for i in range(0,len(signals)-1,1):
        arg1 = copy.deepcopy(signals[i])
        arg2 = copy.deepcopy(signals[i+1])

        pairnum += 1

        #print(f"== Pair {pairnum} ==")
        correct = compare(arg1, arg2)
        if (correct == -1):
            #print(f"Swapping {arg1} with {arg2}")
            temp = signals[i]
            signals[i] = signals[i+1]
            signals[i+1] = temp
        #print()

#for signal in signals:
#    print(signal)

# Find the dividers
for signal in range(len(signals)):
    if (signals[signal] == [[2]]):
        div1 = signal+1
    if (signals[signal] == [[6]]):
        div2 = signal+1

# Calculate decoder value
decoder = div1*div2
print(f"decoder = {div1} * {div2} = {decoder}")

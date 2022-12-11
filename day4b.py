import re

def has_overlap(t1, t2):
    if (((t1[0] >= t2[0] and t1[0] <= t2[1])) or ((t1[1] >= t2[0] and t1[1] <= t2[1])) or \
        ((t2[0] >= t1[0] and t2[0] <= t1[1])) or ((t2[1] >= t1[0] and t2[1] <= t1[1]))):
        olap = True
        print(f"FOUND!", t1, t2)
    else:
        olap = False

    return(olap)

tally = 0

with open('day4a_input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^(.*)-(.*),(.*)-(.*)", line.strip())
        if match:
            #print(f"found! {match.group(0)} {match.group(1)} {match.group(2)}")
            elf1 = (int(match.group(1)), int(match.group(2)))
            elf2 = (int(match.group(3)), int(match.group(4)))
            #print(elf1, elf2)
            if (has_overlap(elf1, elf2)):
                tally += 1
        else:
            print(f"Bad input: {line}")

print(f"Total overlaps: {tally}")

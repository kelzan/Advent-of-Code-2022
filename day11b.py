import re

def show_monkeys(marray):
    for monkey in marray:
        monkey.showit()
        print()
  
class monkey:
    def __init__(self, name):
        self.name = name
        self.mlist = []
        self.items = []
        self.operation = ""
        self.operand1 = 0
        self.operand2 = 0
        self.test_div = 0
        self.test_true = 0
        self.test_false = 0
        self.inspected = 0

    def showit(self):
        print(f"Monkey {self.name}:")
        print(f"  Starting items: {self.items}")
        print(f"  Operation: new = {self.operand1} {self.operation} {self.operand2}")
        print(f"  Test: divisible by {self.test_div}")
        print(f"     If True: throw to monkey {self.test_true}")
        print(f"     If false: throw to monkey {self.test_false}")
        print(f"  Inspected: {self.inspected}")

    def take_turn(self):
        num_items = len(self.items)
        #print(f"Monkey {self.name} Turn:")
        for i in range(num_items):
            item = self.items.pop(0)
            self.inspected += 1
            #print(f"  Item {i} ({item}):")
            if (self.operand1 == 0):
                op1 = item
            else:
                op1 = self.operand1
            if (self.operand2 == 0):
                op2 = item
            else:
                op2 = self.operand2
            if (self.operation == "*"):
                newval = op1 * op2
            else:
                newval = op1 + op2
            #print(f"    worry: {newval}")
            #newval = newval // 3
            #print(f"    bored: {newval}")
            worrytest = (newval%self.test_div == 0)
            #print(f"    test: {worrytest}")
            if (worrytest):
                dest = self.test_true
            else:
                dest = self.test_false
            #print(f"    Throwing to monkey {dest}")
            self.mlist[dest].items.append(newval)
        #print()

    def normalize(self, lcm):
        for i in range(len(self.items)):
            self.items[i] = self.items[i]%lcm
            



curmonkey = None
monkeys = []
numrounds = 10000

with open('day11a_input.txt', 'r') as fp:
    for line in fp:
        match = re.search(r"^Monkey (.*):", line.strip())
        if (match):
            curmonkey = monkey(match.group(1))
            monkeys.append(curmonkey)
            curmonkey.mlist = monkeys
        match = re.search(r"Starting items: (.*)",line.strip())
        if (match):
            aitems = match.group(1).split(",")
            curmonkey.items = [int(i) for i in aitems]
        match = re.search(r"Operation: new = (.*) (.*) (.*)",line.strip())
        if (match):
            curmonkey.operation = match.group(2)
            if (match.group(1) != "old"):
                curmonkey.operand1 = int(match.group(1))
            if (match.group(3) != "old"):
                curmonkey.operand2 = int(match.group(3))
        match = re.search(r"Test: divisible by (.*)",line.strip())
        if (match):
            curmonkey.test_div = int(match.group(1))
        match = re.search(r"If true: throw to monkey (.*)",line.strip())
        if (match):
            curmonkey.test_true = int(match.group(1))        
        match = re.search(r"If false: throw to monkey (.*)",line.strip())
        if (match):
            curmonkey.test_false = int(match.group(1))

show_monkeys(monkeys)
lcm = 1
for monkey in monkeys:
    lcm = lcm * monkey.test_div

print(f"lcm: {lcm}")

for round in range(numrounds):
    for monkey in monkeys:
        monkey.take_turn()
    if (round%20 == 0):
        print(f"Round: {round}")
        for monkey in monkeys:
            monkey.normalize(lcm)

#show_monkeys(monkeys)
inspections = [i.inspected for i in monkeys]
print(inspections)
inspections.sort(reverse=True)
print(f"Shenanigans: {inspections[0]*inspections[1]}")
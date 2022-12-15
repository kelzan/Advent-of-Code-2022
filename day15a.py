import re
import sys


sensors = []

class sensor:
    def __init__(self, sx, sy, bx, by):
        self.s_loc=((sy,sx))
        self.b_loc=((by,bx))
        self.mdist = self.get_man_dist(self.s_loc,self.b_loc)
        
    def show_it(self):
        print(f"Sensor coord: {self.s_loc}, beacon coord: {self.b_loc}, mdist: {self.mdist}")

    def get_man_dist(self, c1, c2):
        return(abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]))

    def get_row_extent(self,row):
        if ((row < self.s_loc[0]-self.mdist) or (row > self.s_loc[0]+self.mdist)):
            return(None)
        ex1 = self.mdist - abs(self.s_loc[0]-row)
        #print(row,self.s_loc[0]-self.mdist,self.s_loc[0]+self.mdist,ex1)
        return((self.s_loc[1]-ex1, self.s_loc[1]+ex1))

with open('day15a_input.txt', 'r') as fp:
    for line in fp:
        #print(line.strip())
        match = re.search(r"^Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line.strip())
        if (match):
            newsensor = sensor(int(match.group(1)),int(match.group(2)),int(match.group(3)),int(match.group(4)))
            #newsensor.show_it()
            sensors.append(newsensor)
        else:
            print("BAD INPUT")
            sys.exit()

sset = set()
target_row = 2000000

for sensor in sensors:
    extent = sensor.get_row_extent(target_row)
    if (extent != None):
        sensor.show_it()
        #print(extent)
        newset = set(range(extent[0],extent[1]+1))
        #print(newset)
        sset = sset.union(newset)

for sensor in sensors:
    if (sensor.b_loc[0] == target_row):
        if (sensor.b_loc[1] in sset):
            sset.remove(sensor.b_loc[1])
            print(f"Removed: {sensor.b_loc[1]}")

#print(sset)
print(f"number of locations: {len(sset)}")



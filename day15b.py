import re
import sys
import time

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

def collapse_ranges(r):
    working = True
    #print(r)
    while (working):
        collapsed = False
        working = True
        #print("== Top of loop ==")
        #print(r)
        for first in range(len(r)-1):
            for second in range(first+1,len(r)):
                #print(f"{first}-{second} {r[first]} and {r[second]}")
                if ((r[first][1]+1 < r[second][0]) or (r[first][0] > r[second][1]+1)): # No overlap
                    #print(f"no overlap")
                    None
                elif ((r[first][0] >= r[second][0]) and (r[first][1] <= r[second][1])): # First contained inside second
                    #print(f"first contained inside second")
                    del r[first]
                    collapsed = True
                    break               
                elif ((r[second][0] >= r[first][0]) and (r[second][1] <= r[first][1])): # Second contained inside first
                    #print(f"second contained inside first")
                    del r[second]
                    collapsed = True
                    break
                elif ((r[first][1]+1 >= r[second][0]) and (r[first][1] <= r[second][1])): # End of first overlaps onto beginning of second
                    #print(f"End of first overlaps onto beginning of second")
                    r[first] = ((r[first][0],r[second][1]))
                    del r[second]
                    collapsed = True
                    break
                elif ((r[second][1]+1 >= r[first][0]) and (r[second][1] <= r[first][1])): # End of second overlaps onto beginning of first
                    #print(f"End of second overlaps onto beginning of first")
                    r[first] = ((r[second][0],r[first][1]))
                    del r[second]
                    collapsed = True
                    break
                else:
                    print(f"PANIC: {r[first]}{r[second]}")
                    sys.exit()
                               
            if (collapsed == True):
                #print("Bottom")
                #print(r)
                working = True
                break
        #print("Hit bottom, setting working False")
        if (not collapsed):
            working = False
    #print(f"working: {working}")

start = time.time()

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

row_low = 0
row_high = 4000000

c_ranges = []
for row in range(row_low,row_high+1):
    ranges = []
    for sensor in sensors:
        extent = sensor.get_row_extent(row)
        if (extent != None):
            #sensor.show_it()
            ranges.append(extent)
    #print(f"Collapsing {row}")
    collapse_ranges(ranges)
    #c_ranges.append(ranges)
    if (row%100000 == 0):
        print(row)
    if (len(ranges) > 1):
        print(f"{row} - {ranges}")
        freq = ((max(ranges[0][0],ranges[1][0])-1)*4000000) + row
        print(f"freq: {freq}")
        c_ranges.append(ranges)

end = time.time()
print(f"found: {len(c_ranges)}")
print(f" Elapsed time: {end-start}")



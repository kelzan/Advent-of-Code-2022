import re

class file:
    def __init__(self, name):
        self.name = name
        self.contents = []
        self.parent = None
        self.is_directory = False
        self.filesize = 0
        self.totsize = 0
 
    def showit(self):
        print(f"--Name: {self.name}, size: {self.filesize}, is_directory: {self.is_directory}")

    def add_file(self,_name,_size):
        newfile = file(_name)
        #print(f"Adding file {_name} size {_size} to {self.name}")
        newfile.filesize = _size
        newfile.name = _name
        newfile.parent = self
        self.contents.append(newfile)

    def add_dir(self,_name):
        newfile = file(_name)
        #print(f"Adding directory {_name} to {self.name}")
        newfile.is_directory = True
        newfile.parent = self
        #newfile.showit()
        self.contents.append(newfile)

    def dir_size(self):
        size = 0
        if (not self.is_directory):
            print("Not a directory")
            return(0)
        for entry in self.contents:
            if (entry.is_directory):
                size += entry.dir_size()
            else:
                size += entry.filesize
        return(size)

    def calc_totsize(self, totlist=[]):
        size = 0
        if (not self.is_directory):
            print("Not a directory")
            return(0)
        for entry in self.contents:
            if (entry.is_directory):
                size += entry.dir_size()
                entry.calc_totsize(totlist)
            else:
                size += entry.filesize
        self.totsize = size
        totlist.append(tuple((self.name, self.totsize)))


    def small_size(self):
        size = 0
        tally = 0
        if (not self.is_directory):
            print("Not a directory")
            return(0)
        for entry in self.contents:
            if (entry.is_directory):
                size += entry.small_size()
                tally += entry.dir_size()
            else:
                tally += entry.filesize
        if (tally < 100000):
            print(f"directory {self.name} adds {tally} to total {size}")
            size += tally
        return(size)

    def print_dir(self,pad=0):
        #print(f"Printing {len(self.contents)} entries in {self.name}")
        if (self.name == "/"):
            print("/")
            pad += 2
        for entry in self.contents:
            if (entry.is_directory):
                print(f"{' '*pad}dir {entry.name}")
                entry.print_dir(pad+2)
            else:
                print(f"{' '*pad}{entry.filesize} {entry.name}")

    def get_dir(self,dirname):
        if (not self.is_directory):
            print(f"{self.name} Not a directory for get_dir")
            return("")
        for entry in self.contents:
            if (entry.is_directory):
                if (dirname == entry.name):
                    return(entry)
        print(f"{dirname} not a directory of {self.name}")
        return(None)

root = None
curdir = None

with open('day7a_input.txt', 'r') as fp:
    for line in fp:
        #print(f"COMMAND: {line.strip()}")
        match = re.search(r"^\$ cd (.*)", line.strip())
        if match: # cd command
            dir = match.group(1)
            #print(f"cd to {dir}")
            listing = False
            if (dir == "/"): # Root
                root = file("/")
                root.is_directory = True
                curdir = root
                #root.print_dir()
            elif (dir == ".."):
                curdir = curdir.parent
            else:
                curdir = curdir.get_dir(dir)
            continue
        match = re.search(r"^\$ ls", line.strip())
        if match: # ls command
            #print("listing")
            listing = True
            continue
        match = re.search(r"^dir (.*)", line.strip())
        if match: # directory listing
            dirname = match.group(1)
            #print(f"-- Dir {dirname}")
            curdir.add_dir(dirname)
            #curdir.print_dir()
            continue
        match = re.search(r"^(\d*) (.*)", line.strip())
        if match: # file listing
            fname = match.group(2)
            fsize = int(match.group(1))
            #print(f"-- file {fname} {fsize}")
            curdir.add_file(fname,fsize)
            #curdir.print_dir()
            continue
        else:
            print("BAD COMMAND")

root.print_dir()
tt = []
root.calc_totsize(tt)
print(tt)

freespace = 70000000 - root.totsize
shortfall = 30000000 - freespace
print(f"used: {root.totsize}, free: {freespace}, short: {shortfall}")
#result = filter(lambda x: x[1]>shortfall, tt)
result = [x for x in tt if x[1]>shortfall]
s = min(result, key = lambda t: t[1])
print(result)
print(s)
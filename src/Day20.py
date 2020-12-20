from copy import copy, deepcopy
from enum import Enum

class Side(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

class Tile:
    def __init__(self,tid,img):
        self.tid = tid
        self.img = img
    def sides(self):
        top = copy(self.img[0])
        bottom = copy(self.img[-1])
        left = []
        right = []
        for i in range(len(self.img[0])):
            right.append(self.img[i][-1])
            left.append(self.img[i][0])

        return [top,right,list(reversed(bottom)),list(reversed(left))]
    def rotate_quarter(self):
        new_img = deepcopy(self.img)  
        for i in range(len(new_img)):
            new_img[i] = [self.img[len(new_img)-1-j][i] for j in range(len(self.img))]  
        return Tile(self.tid,new_img)
    
    def flip(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = list(reversed(new_img[i]))
        return Tile(self.tid,new_img)

def matches(match_tile,tiles):
    count = 0
    matches = []
    for (i,match_side) in enumerate(tiles[match_tile].sides()): 
        #print(match_side)
        for tile in [t for t in tiles if t!=match_tile]:
            for side in tiles[tile].sides(): 
                rev = list(reversed(side))
                if match_side == side or match_side ==rev:
                    count+=1
                    matches.append((i,tile))
    print("%i has %i matches"%(match_tile,count))
    print(matches)
    return count
        
parts = list(open("inputs/input20.txt", "r").read().replace(".","0").replace("#","1").split("\n\n"))
print(parts)
tiles = {}
for part in parts:
    lines = part.splitlines()
    tid = int(lines[0][4:9])
    image = list(map(lambda l: list(l),lines[1:]))
    print(tid)
    tiles[tid] = Tile(tid,image)
prod = 1
for tid in tiles:
    c = matches(tid,tiles)
    if c==2:
        prod*=tid
print(prod)

from copy import copy, deepcopy
from enum import Enum
from math import sqrt

class Tile:
    def __init__(self, tid, img,flipped,rot):
        self.tid = tid
        self.img = img
        self.flipped = flipped
        self.rot = rot

    def gen_index(self,i):
        if self.flipped:
            return (-i+self.rot)%4
        else:
            return (i-self.rot)%4

    def inv_index(self,i):
        if self.flipped:
            return (-i-self.rot)%4
        else:
            return (i+self.rot)%4
    def gen_indices(self):
        return list(map(lambda i: self.gen_index(i),[0,1,2,3]))
    def inv_indices(self):
        return list(map(lambda i: self.inv_index(i),[0,1,2,3]))

    def sides(self):
        top = copy(self.img[0])
        bottom = copy(self.img[-1])
        left = []
        right = []
        for i in range(len(self.img[0])):
            right.append(self.img[i][-1])
            left.append(self.img[i][0])

        return [top, right, list(reversed(bottom)), list(reversed(left))]

    def rotate_quarter(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = [
                self.img[len(new_img) - 1 - j][i] for j in range(len(self.img))
            ]
        return Tile(self.tid, new_img,self.flipped,self.rot+1)

    def flip(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = list(reversed(new_img[i]))
        return Tile(self.tid, new_img,not self.flipped,self.rot)

tile = Tile(42,[[8,0,8],[3,8,1],[8,2,8]],False,0)
flip = tile.flip()
indices = [0,1,2,3]
print(flip.rotate_quarter().gen_indices()) 
print(flip.gen_indices()) 
print(tile.gen_indices()) 
print(tile.rotate_quarter().gen_indices())

print(flip.rotate_quarter().inv_indices()) 
print(flip.inv_indices()) 
print(tile.inv_indices()) 
print(tile.rotate_quarter().inv_indices())

def matches(match_tile, tiles):
    count = 0
    mtchs = {}
    for (i, match_side) in enumerate(tiles[match_tile].sides()):
        j = (i + 2) % 4
        for tile in [t for t in tiles if t != match_tile]:
            tile_cpy = deepcopy(tiles[tile])
            flip_cpy = tile_cpy.flip()
            for rot_id in range(4):
                norm_side = list(reversed(tile_cpy.sides()[j]))
                flip_side = list(reversed(flip_cpy.sides()[j]))
                if match_side == norm_side:
                    count += 1
                    mtchs[i] = tile
                    tiles[tile] = tile_cpy
                    break
                if match_side == flip_side:
                    count += 1
                    mtchs[i] = tile
                    tiles[tile] = flip_cpy
                    break
                tile_cpy = tile_cpy.rotate_quarter()
                flip_cpy = flip_cpy.rotate_quarter()
    #print("%i has %i matches" % (match_tile, count))
    #print(mtchs)
    return mtchs
def get_key(val,d):
    for k, v in d.items():
         if val == v:
             return k
    return -1 


parts = list(
    open("inputs/input20.txt", "r")
    .read()
    .replace(".", "0")
    .replace("#", "1")
    .split("\n\n")
)
tiles = {}
for part in parts:
    lines = part.splitlines()
    tid = int(lines[0][4:9])
    image = list(map(lambda l: list(l), lines[1:]))
    tiles[tid] = Tile(tid, image,False,0)
prod = 1
covered = set()
current_tid = list(tiles.keys())[0]
print("Center: %i"%(current_tid))
center = current_tid
queue = [current_tid]
topleft = -1
edges = {}
corners = set()
while queue:
    current_tid = queue.pop(0)
    if current_tid not in covered:
        covered.add(current_tid)
        mtchs = matches(current_tid, tiles)
        edges[current_tid] = mtchs
        queue.extend([v for v in mtchs.values() if not v in covered])
        if len(mtchs) == 2:
            if 1 in mtchs and 2 in mtchs:
                topleft = current_tid
            prod *= current_tid
            corners.add(current_tid)
assert tiles[center].rot==0
assert tiles[center].flipped==False
print(edges)    
print("Part 1: "+str(prod))
side = round(sqrt(len(tiles)))
layout = [[-1 for j in range(side)] for i in range(side)]
placed = set()
layout[0][0] = topleft 
placed.add(topleft)
print(topleft)
prev = topleft
right,down = tuple(edges[topleft].values())
layout[0][1] = right
layout[1][0] = down
x = 1
y = 1
for i in range(side-2):
    e = edges[right]
    new_key = (get_key(prev,e)+2)%4
    prev = right
    right = e[new_key] 
    x+=1
    layout[0][x] = right 
    print(right)
prev = topleft 
for i in range(side-2):
    e = edges[down]
    new_key = (get_key(prev,e)+2)%4
    prev = down
    down = e[new_key] 
    y+=1
    layout[y][0] = down 
    print(down)
   
print(right,down)
print(layout)
print(placed)



rec_image = [[deepcopy(tiles[topleft].img) for j in range(side)] for i in range(side)]
# print(rec_image)

from copy import copy, deepcopy

class Tile:
    def __init__(self,tid,top,right,bottom,left):
        self.tid = tid
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

parts = list(open("inputs/input20.txt", "r").read().replace(".","0").replace("#","1").split("\n\n"))
print(parts)
tiles = []
for part in parts:
    lines = part.splitlines()
    tid = int(lines[0][4:9])
    image = list(map(lambda l: list(l),lines[1:]))
    border = image[0]
    top = copy(image[0])
    bottom = copy(image[-1])
    left = []
    right = []
    for i in range(len(image[0])):
        right.append(image[i][-1])
        left.append(image[i][0])
    print(tid)
    print("Top: {}\nRight: {}\nBottom: {}\nLeft: {}".format(top,right,bottom,left))
    tiles.append(Tile(tid,top,right,bottom,left))
target_tile = tiles[0]
target_side = target_tile.right
for t in tiles[1:]:
    for side in [t.top,t.right,t.bottom,t.left]:
        print("Side: {}".format(side))
        mirr = list(reversed(side[len(side)//2:]))
        print(mirr)
        mirr.extend(reversed(side[:len(side)//2]))
        print(mirr)
        print(side)
        if target_side == side or target_side ==reversed(side) or target_side == mirr:
            print("A match! A match!")

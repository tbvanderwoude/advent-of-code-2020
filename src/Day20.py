from copy import copy, deepcopy

class Tile:
    def __init__(self,tid,top,right,bottom,left):
        self.tid = tid
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

parts = list(open("inputs/input20.txt", "r").read().split("\n\n"))
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
print(tiles)


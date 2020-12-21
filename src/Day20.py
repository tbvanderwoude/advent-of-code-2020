from copy import copy, deepcopy
from enum import Enum
from math import sqrt


class Side(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3


class Tile:
    def __init__(self, tid, img):
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

        return [top, right, list(reversed(bottom)), list(reversed(left))]

    def rotate_quarter(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = [
                self.img[len(new_img) - 1 - j][i] for j in range(len(self.img))
            ]
        return Tile(self.tid, new_img)

    def flip(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = list(reversed(new_img[i]))
        return Tile(self.tid, new_img)


def match_side(i, match_side, tiles):
    # print(match_side)
    j = (i + 2) % 4
    for tile in [t for t in tiles if t != match_tile]:
        tile_cpy = deepcopy(tiles[tile])
        flip_cpy = tile_cpy.flip()
        for rot_id in range(4):
            norm_side = tile_cpy.sides()[j]
            flip_side = flip_cpy.sides()[j]
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


def matches(match_tile, tiles):
    count = 0
    mtchs = {}
    for (i, match_side) in enumerate(tiles[match_tile].sides()):
        # print(match_side)
        j = (i + 2) % 4
        for tile in [t for t in tiles if t != match_tile]:
            tile_cpy = deepcopy(tiles[tile])
            flip_cpy = tile_cpy.flip()
            for rot_id in range(4):
                norm_side = tile_cpy.sides()[j]
                flip_side = flip_cpy.sides()[j]
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
    print("%i has %i matches" % (match_tile, count))
    print(mtchs)
    return mtchs


parts = list(
    open("inputs/input20.txt", "r")
    .read()
    .replace(".", "0")
    .replace("#", "1")
    .split("\n\n")
)
print(parts)
tiles = {}
for part in parts:
    lines = part.splitlines()
    tid = int(lines[0][4:9])
    image = list(map(lambda l: list(l), lines[1:]))
    print(tid)
    tiles[tid] = Tile(tid, image)
prod = 1
covered = set()
current_tid = list(tiles.keys())[0]
queue = [current_tid]
print(queue)
topleft = -1
edges = {}
while queue:
    current_tid = queue.pop(0)
    covered.add(current_tid)
    mtchs = matches(current_tid, tiles)
    edges[current_tid] = mtchs
    queue.extend([v for v in mtchs.values() if not v in covered and not v in queue])
    if len(mtchs) == 2:
        if 1 in mtchs and 2 in mtchs:
            topleft = current_tid
        prod *= current_tid

print(prod)
print(topleft)
side = round(sqrt(len(tiles)))
it = topleft
i = 0
while 2 in edges[it]:
    print(it, edges[it])
    it = edges[it][2]
    i += 1
    j = 0
    inner_it = it
    while 1 in edges[inner_it]:
        j += 1
        print(inner_it)
        inner_it = edges[inner_it][1]
print(edges[topleft])
print(edges[edges[topleft][1]])
rec_image = [[deepcopy(tiles[topleft].img) for j in range(side)] for i in range(side)]
# print(rec_image)

from copy import copy, deepcopy
from enum import Enum
from math import sqrt


class Tile:
    def __init__(self, tid, img, flipped, rot):
        self.tid = tid
        self.img = img
        self.flipped = flipped
        self.rot = rot

    def gen_index(self, i):
        if self.flipped:
            return (-i + self.rot) % 4
        else:
            return (i - self.rot) % 4

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
        return Tile(self.tid, new_img, self.flipped, self.rot + 1)

    def flip(self):
        new_img = deepcopy(self.img)
        for i in range(len(new_img)):
            new_img[i] = list(reversed(new_img[i]))
        return Tile(self.tid, new_img, not self.flipped, self.rot)


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
    return mtchs


def get_key(val, d):
    for k, v in d.items():
        if val == v:
            return k
    return -1


parts = list(open("inputs/input20.txt", "r").read().strip().split("\n\n"))
tiles = {}
tile_width = -1
for part in parts:
    lines = part.splitlines()
    tid = int(lines[0][4:9])
    image = list(map(lambda l: list(l), lines[1:]))
    tile_width = len(image)
    tiles[tid] = Tile(tid, image, False, 0)
prod = 1
covered = set()
current_tid = list(tiles.keys())[0]
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
assert tiles[center].rot == 0
assert tiles[center].flipped == False
print("Part 1: " + str(prod))
side = round(sqrt(len(tiles)))
layout = [[-1 for j in range(side)] for i in range(side)]
layout[0][0] = topleft

placed = set()

for i in range(side):
    if i == 0:
        corner = topleft
        right, down = tuple(edges[corner].values())
    elif i == side - 1:
        r_set = set(edges[right].values())
        d_set = set(edges[down].values())
        corner = list(filter(lambda v: v not in placed, r_set.intersection(d_set)))[0]
        layout[i][i] = corner
        placed.add(corner)
        break
    else:
        r_set = set(edges[right].values())
        d_set = set(edges[down].values())
        corner = list(filter(lambda v: v not in placed, r_set.intersection(d_set)))[0]
        v1, v2 = tuple(filter(lambda v: v not in placed, edges[corner].values()))
        if not v1 in r_set:
            right, down = v1, v2
        else:
            right, down = v2, v1
    layout[i][i] = corner
    layout[i][i + 1] = right
    layout[i + 1][i] = down
    placed.add(corner)
    placed.add(right)
    placed.add(down)
    x = i + 1
    y = i + 1
    r_it = right
    d_it = down
    prev = corner
    for j in range(side - 2 - i):
        e = edges[r_it]
        new_key = (get_key(prev, e) + 2) % 4
        prev = r_it
        r_it = e[new_key]
        x += 1
        layout[i][x] = r_it
        placed.add(r_it)
    prev = corner
    for j in range(side - 2 - i):
        e = edges[d_it]
        new_key = (get_key(prev, e) + 2) % 4
        prev = d_it
        d_it = e[new_key]
        y += 1
        layout[y][i] = d_it
        placed.add(d_it)
s = ""

for tile_row in range(side):
    for row in range(1, tile_width - 1):
        l = ""
        for tile_col in range(side):
            tid = layout[tile_row][tile_col]
            img = tiles[tid].img
            for col in range(1, tile_width - 1):
                l += img[row][col]
        s += l + "\n"
lines = s.splitlines()
image = list(map(lambda l: list(l), lines))
tile_width = len(image)
img_tile = Tile(-1, image, False, 0)
img_size = len(image)
sea_monster = [
    (0, 1),
    (1, 0),
    (4, 0),
    (5, 1),
    (6, 1),
    (7, 0),
    (10, 0),
    (11, 1),
    (12, 1),
    (13, 0),
    (16, 0),
    (17, 1),
    (18, 2),
    (18, 1),
    (19, 1),
]
# draws the sea monster
monster_str = ""
for row in range(3):
    l = ""
    for col in range(20):
        if (col, row) in sea_monster:
            l += "x"
        else:
            l += "."
    monster_str += l + "\n"

tile_cpy = deepcopy(img_tile)
for rot_id in range(4):
    img = tile_cpy.img
    for x in range(img_size - 20 + 1):
        for y in range(img_size - 3 + 1):
            is_monster = True
            for (dx, dy) in sea_monster:
                if img[y + dy][x + dx] == ".":
                    is_monster = False
                    break
            if is_monster:
                for (dx, dy) in sea_monster:
                    img[y + dy][x + dx] = "O"
    tile_cpy = tile_cpy.rotate_quarter()
tile_cpy = tile_cpy.flip()
for rot_id in range(4):
    img = tile_cpy.img
    for x in range(img_size - 20 + 1):
        for y in range(img_size - 3 + 1):
            is_monster = True
            for (dx, dy) in sea_monster:
                if img[y + dy][x + dx] == ".":
                    is_monster = False
                    break
            if is_monster:
                for (dx, dy) in sea_monster:
                    img[y + dy][x + dx] = "O"
    tile_cpy = tile_cpy.rotate_quarter()
roughness = 0
for i in range(img_size):
    for j in range(img_size):
        if tile_cpy.img[i][j] == "#":
            roughness += 1
print("Part 2: %i" % (roughness))

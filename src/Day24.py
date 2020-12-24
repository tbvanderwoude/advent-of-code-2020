import re
from copy import copy, deepcopy
from functools import reduce


def get_neighs(c, dir_map):
    return set(map(lambda x: (x[0] + c[0], x[1] + c[1]), dir_map.values()))


coords = open("inputs/input24.txt", "r").read().splitlines()
dir_map = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1),
}
ex = "|".join(dir_map.keys())
r = re.compile(ex)
blacks = set()
for coord in coords:
    deltas = list(map(dir_map.get, r.findall(coord)))
    hex_coord = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), deltas)
    if hex_coord in blacks:
        blacks.remove(hex_coord)
    else:
        blacks.add(hex_coord)
print("Number of starting black tiles: %i" % len(blacks))
days = 100
for day in range(days):
    active = copy(blacks)
    for blk in blacks:
        active = active.union(get_neighs(blk, dir_map))
    new_blacks = copy(blacks)
    for act in active:
        neigh = get_neighs(act, dir_map)
        n_blk = len(blacks.intersection(neigh))
        if act in blacks:
            if n_blk == 0 or n_blk > 2:
                new_blacks.remove(act)
        else:
            if n_blk == 2:
                new_blacks.add(act)
    blacks = new_blacks
print("Number of black tiles facing up after %i days: %i" % (days, len(blacks)))

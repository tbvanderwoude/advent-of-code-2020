from copy import deepcopy


def enum_neigh(x, y, z, w):
    neigh = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                        neigh.add((x + dx, y + dy, z + dz, w + dw))
    return neigh


def count_active(x, y, z, w, active):
    return len(list(filter(lambda x: x in active, enum_neigh(x, y, z, w))))


def gen_to_check(active):
    neigh = deepcopy(active)
    for coord in active:
        neigh = neigh.union(enum_neigh(*coord))
    return neigh


ls = open("inputs/input17.txt", "r").read().strip().splitlines()
print(len(enum_neigh(0, 0, 0, 0)))
active = set()
for (x, l) in enumerate(ls):
    for (y, c) in enumerate(list(l)):
        if c == '#':
            active.add((x, y, 0, 0))
print(active)
for i in range(6):
    to_check = gen_to_check(active)
    new_active = deepcopy(active)
    for coord in to_check:
        c = count_active(*coord, active)
        if coord in active:
            if not (c == 2 or c == 3):
                new_active.remove(coord)
        else:
            if c == 3:
                new_active.add(coord)
    active = new_active
    print(len(active))

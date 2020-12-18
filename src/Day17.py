from copy import deepcopy, copy


def comp_rel(n):
    origin = tuple([0] * n)
    rs = [origin]
    for i in range(n):
        new_rs = []
        for rel in rs:
            for d in [-1, 0, 1]:
                n_alt = list(rel)
                n_alt[i] += d
                new_rs.append(tuple(n_alt))
            rs = new_rs
    neigh = set(rs)
    neigh.remove(origin)
    return neigh


def enum_neigh(c,rel_list):
    return list(map(lambda d: tuple(map(lambda x: x[0]+x[1],zip(list(c),list(d)))),rel_list))


def count_active(c, active,rel_list):
    return len(list(filter(lambda x: x in active, enum_neigh(c,rel_list))))


def gen_to_check(active,rel_list):
    neigh = deepcopy(active)
    for coord in active:
        neigh = neigh.union(enum_neigh(coord,rel_list))
    return neigh


def simulate_state(ls, n):
    # global state. At least it is somewhat faster
    rel_list = comp_rel(n)
    active = set()
    for (x, l) in enumerate(ls):
        for (y, c) in enumerate(list(l)):
            if c == '#':
                coord = [x, y]
                coord.extend([0] * (n - 2))
                active.add(tuple(coord))
    for i in range(6):
        to_check = gen_to_check(active,rel_list)
        new_active = copy(active)
        for coord in to_check:
            c = count_active(coord, active,rel_list)
            if coord in active:
                if not (c == 2 or c == 3):
                    new_active.remove(coord)
            else:
                if c == 3:
                    new_active.add(coord)
        active = new_active
    return len(active)

ls = open("inputs/input17.txt", "r").read().strip().splitlines()
print(simulate_state(ls, 3))
print(simulate_state(ls, 4))

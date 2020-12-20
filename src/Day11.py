from copy import deepcopy


def trace(rs, x, y, dx, dy, w, h):
    if (
        rs[y][x] == "L"
        or rs[y][x] == "#"
        or (x + dx < 0 or x + dx >= w)
        or (y + dy < 0 or y + dy >= h)
    ):
        return rs[y][x]
    else:
        return trace(rs, x + dx, y + dy, dx, dy, w, h)


def trace_neigh(rs, x, y, w, h):
    neigh = []
    if x < w - 1:
        neigh.append(trace(rs, x + 1, y, 1, 0, w, h))
        if y > 0:
            neigh.append(trace(rs, x + 1, y - 1, 1, -1, w, h))
        if y < h - 1:
            neigh.append(trace(rs, x + 1, y + 1, 1, 1, w, h))
    if x > 0:
        neigh.append(trace(rs, x - 1, y, -1, 0, w, h))
        if y > 0:
            neigh.append(trace(rs, x - 1, y - 1, -1, -1, w, h))
        if y < h - 1:
            neigh.append(trace(rs, x - 1, y + 1, -1, 1, w, h))
    if y > 0:
        neigh.append(trace(rs, x, y - 1, 0, -1, w, h))
    if y < h - 1:
        neigh.append(trace(rs, x, y + 1, 0, 1, w, h))
    return neigh


def get_neigh(rs, x, y, w, h):
    neigh = []
    if x < w - 1:
        neigh.append(rs[y][x + 1])
        if y > 0:
            neigh.append(rs[y - 1][x + 1])
        if y < h - 1:
            neigh.append(rs[y + 1][x + 1])
    if x > 0:
        neigh.append(rs[y][x - 1])
        if y > 0:
            neigh.append(rs[y - 1][x - 1])
        if y < h - 1:
            neigh.append(rs[y + 1][x - 1])
    if y > 0:
        neigh.append(rs[y - 1][x])
    if y < h - 1:
        neigh.append(rs[y + 1][x])
    return neigh


ls = open("inputs/input11.txt", "r").read().strip().splitlines()
rs = list(map(lambda s: list(s.strip()), ls))
w = len(rs[0])
h = len(rs)
change = True
i = 0
while change:
    change = False
    print("State %i" % (i))
    ns = deepcopy(rs)
    # for r in rs:
    #     print(r)
    for x in range(w):
        for y in range(h):
            neigh = trace_neigh(rs, x, y, w, h)
            # print(neigh)
            cv = rs[y][x]
            if cv == "L" and len(list(filter(lambda t: t == "#", neigh))) == 0:
                ns[y][x] = "#"
                change = True
            if cv == "#" and len(list(filter(lambda t: t == "#", neigh))) >= 5:
                ns[y][x] = "L"
                change = True
    i += 1
    rs = ns
empty_count = sum(map(lambda r: len(list(filter(lambda t: t == "#", r))), rs))
print(empty_count)
print("The grid is %ix%i" % (w, h))

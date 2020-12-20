import re
from functools import reduce

ls = open("inputs/input16.txt", "r").read().split("\n\n")
e = re.compile(r"(\w+\s*\w+): (\d+)-(\d+) or (\d+)-(\d+)")
fs = {}
for l in ls[0].splitlines():
    gs = e.match(l).groups()
    fs[gs[0]] = (int(gs[1]), int(gs[2]), int(gs[3]), int(gs[4]))
ts = list(
    map(lambda l: list(map(lambda e: int(e), l.split(","))), ls[2].splitlines()[1:])
)
err_r = 0
t_valids = []
field_sets = [set() for i in range(len(ts[0]))]
for t in ts:
    t_valid = True
    for (i, v) in enumerate(t):
        valid = False
        for f in fs:
            (l1, u1, l2, u2) = fs[f]
            if (l1 <= v <= u1) or (l2 <= v <= u2):
                valid = True
                break
        if not valid:
            t_valid = False
            err_r += v
        else:
            field_sets[i].add(v)
    t_valids.append(t_valid)
print("Part 1: %i" % (err_r))
# print(t_valids)
ts = [t for (t, v) in zip(ts, t_valids) if v]
# print(field_sets)
matching_fields = [set() for i in range(len(ts[0]))]
for (i, field_set) in enumerate(field_sets):
    for f in fs:
        matched = True
        for v in field_set:
            (l1, u1, l2, u2) = fs[f]
            if (l1 <= v <= u1) or (l2 <= v <= u2):
                valid = True
            else:
                matched = False
                break
        if matched:
            matching_fields[i].add(f)
matching_fields = sorted(enumerate(matching_fields), key=lambda x: len(x[1]))
field_names = []
for i in range(20):
    mf = matching_fields[i][1]
    assert len(mf) == 1
    name = mf.pop()
    field_names.append((matching_fields[i][0], name))
    for j in range(20):
        if j != i and name in matching_fields[j][1]:
            matching_fields[j][1].remove(name)
my_ticket = list(map(lambda e: int(e), ls[1].splitlines()[1].split(",")))
prod = 1
for (i, n) in field_names:
    if "departure" in n:
        prod *= my_ticket[i]
print("Part 2: %i" % (prod))

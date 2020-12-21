from copy import copy

lines = list(open("inputs/input21.txt", "r").read().strip().splitlines())
split = list(map(lambda s: tuple(s.split(" (contains ")), lines))
list_pairs = []
set_pairs = []
all_ingrs = set()
al_ingr_mp = {}
all_alrgns = set()
for (a, b) in split:
    ingrs = set(a.split(" "))
    alrgns = set(b[: len(b) - 1].split(", "))
    for al in alrgns:
        if al not in al_ingr_mp:
            al_ingr_mp[al] = ingrs
        else:
            al_ingr_mp[al] = al_ingr_mp[al].intersection(ingrs)
    set_pairs.append((ingrs, alrgns))
    all_ingrs = all_ingrs.union(ingrs)
    all_alrgns = all_alrgns.union(alrgns)
safe_ingr = copy(all_ingrs)
for al in al_ingr_mp:
    safe_ingr -= al_ingr_mp[al]
c = 0
for (a, b) in set_pairs:
    c += len(safe_ingr.intersection(a))
print("Part 1: " + str(c))
ls = list(al_ingr_mp.items())
unsorted_dang = []
while ls:
    min_len = min(ls, key=lambda x: len(x[1]))
    assert len(min_len[1]) == 1
    ls.remove(min_len)
    ingr = list(min_len[1])[0]
    unsorted_dang.append((min_len[0], ingr))
    for (a, b) in ls:
        if ingr in b:
            b.remove(ingr)
dang_list = sorted(unsorted_dang)
s = dang_list[0][1]
for i in dang_list[1:]:
    s += "," + i[1]
print("Part 2: " + s)

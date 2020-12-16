import re
ls = open("inputs/input16.txt", "r").read().split("\n\n")
e = re.compile(r"(\w+\s*\w+): (\d+)-(\d+) or (\d+)-(\d+)")
fs = {}
for l in ls[0].splitlines():
    gs = e.match(l).groups()
    fs[gs[0]] = (int(gs[1]),int(gs[2]),int(gs[3]),int(gs[4]))
print(fs)
ts = map(lambda l: list(map(lambda e: int(e),l.split(","))),ls[2].splitlines()[1:])
err_r = 0
for t in ts:
    for v in t:
        valid = False
        for f in fs:
            (l1,u1,l2,u2) = fs[f]
            if (l1 <= v <= u1) or (v >= l2 and v <= u2):
                valid = True
                break
        if not valid:
            err_r+=v
print(err_r)
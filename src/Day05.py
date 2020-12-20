ls = open("inputs/input05.txt", "r").read().splitlines()
tbl = {"F": "0", "B": "1", "L": "0", "R": "1"}
ps = list(
    sorted(
        map(lambda line: int("".join(list(map(lambda char: tbl[char], line))), 2), ls)
    )
)
print(max(ps))
print(
    list(filter(lambda x: x[1] - x[0] == 2, zip(ps[: len(ps) - 1], ps[1 : len(ps)])))[
        0
    ][0]
    + 1
)

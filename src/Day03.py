from functools import reduce

f = open("inputs/input03.txt", "r").read().splitlines()
ds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
c = list(
    map(
        lambda d: sum(
            map(
                lambda y: int(f[y][(y * d[0] // d[1]) % len(f[0])] == "#"),
                filter(lambda y: y % d[1] == 0, range(0, len(f))),
            )
        ),
        ds,
    )
)
print(c, reduce(lambda x, r: x * r, c))

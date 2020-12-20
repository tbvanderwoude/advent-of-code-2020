def last_index(ns, e):
    return (len(ns) - 1) - list(reversed(ns)).index(e)


def solve_slow(ns):
    while len(ns) < 2020:
        front = ns[: len(ns) - 1]
        last = ns[len(ns) - 1]
        if last in front:
            ix = last_index(front, last)
            ns.append((len(ns) - 1) - ix)
        else:
            ns.append(0)
    print("The final list of numbers is")
    print(ns)
    print(ns[-1])


# perhaps I should start with this type of solution anyway?
def solve_faster(ns):
    spoken = dict(map(lambda x: (x[1], x[0]), enumerate(ns[:-1])))
    last = ns[-1]
    n = 30000000
    for i in range(len(ns) - 1, n - 1):
        if last in spoken:
            ix = spoken[last]
            spoken[last] = i
            last = i - ix
        else:
            spoken[last] = i
            last = 0
    print("The last spoken number is")
    print(last)


ls = open("inputs/input15.txt", "r").read().splitlines()
solve_slow(list(map(lambda s: int(s), ls[0].split(","))))
solve_faster(list(map(lambda s: int(s), ls[0].split(","))))

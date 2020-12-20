from math import ceil
from functools import reduce


def chinese_remainder(n, a):
    N = reduce(lambda x, y: x * y, n)
    s = 0
    for i in range(len(n)):
        Ni = N // n[i]
        Mi = mul_inv(Ni, n[i])
        s += a[i] * Ni * Mi
    return s % N


# modified extended euclidean algorithm for modular multiplicative inverse
def mul_inv(a, n):
    t = 0
    r = n
    newt = 1
    newr = a
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        print("Inverse is not defined")
        return -1
    if r < 0:
        t += n
    return t


ls = open("inputs/input13.txt", "r").read().strip().splitlines()
arrival = int(ls[0])
buses = list(map(lambda s: int(s), filter(lambda s: s != "x", ls[1].split(","))))
earl = list(zip(map(lambda n: ceil(arrival / n) * n, buses), buses))
best_bus = min(earl)
print("Part1: %i" % ((best_bus[0] - arrival) * best_bus[1]))
seq = list(
    map(
        lambda s: (-s[0], int(s[1])),
        filter(lambda s: s[1] != "x", enumerate(ls[1].split(","))),
    )
)
(a, n) = list(zip(*seq))
print("Part2: %i" % (chinese_remainder(n, a)))

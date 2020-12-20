ls = open("inputs/input15.txt", "r").read().splitlines()
ns = list(map(lambda s: int(s), ls[0].split(",")))
print(ns)


def last_index(ns, e):
    return (len(ns) - 1) - list(reversed(ns)).index(e)


spoken = dict(map(lambda x: (x[1], x[0]), enumerate(ns[:-1])))

last = ns[-1]
n = 2019
for i in range(2, n):
    # print(last,spoken)
    if last in spoken:
        ix = spoken[last]
        # print("%i was spoken at %i"%(last,ix))
        spoken[last] = i
        last = i - ix
    else:
        # print("%i was not spoken yet"%(last))
        spoken[last] = i
        last = 0
    # print("%i is spoken\n"%(last))

print("The last spoken number is")
print(last)

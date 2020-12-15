ls = open("inputs/input15.txt", "r").read().splitlines()
ns = list(map(lambda s: int(s),ls[0].split(",")))
print(ns)
def last_index(ns,e):
    return (len(ns)-1)-list(reversed(ns)).index(e)
while len(ns)<30000000:
    front = ns[:len(ns)-1]
    last = ns[len(ns)-1]
    # print(front,last)
    if last in front:
        ix = last_index(front,last);
        # print(ix)
        ns.append((len(ns)-1)-ix)
    else:
        ns.append(0)
print("The final list of numbers is")
print(ns)
print(ns[-1])
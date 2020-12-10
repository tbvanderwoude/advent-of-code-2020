from collections import Counter
from functools import reduce
from itertools import permutations
import math


def gen_min(num):
    last = num[-1]
    min_l = [last]
    while min_l[-1] != num[0]:
        min_l.append(min([n for n in num if n < min_l[-1] and (min_l[-1] - n <= 3)]))
    return list(reversed(min_l))


ps = open("inputs/input10.txt", "r").read().strip().splitlines()
num = list(sorted(map(lambda x: int(x), ps)))
num.insert(0, 0)
num.append(max(num) + 3)
diff = list(map(lambda x: x[1] - x[0], zip(num[:len(num) - 1], num[1:len(num)])))
print(list(zip(num, diff)))
print(diff)
counts = Counter(diff)
p1 = counts[1] * counts[3]
print(p1)

ones = []
c = 0
dic = {1: 1, 2: 2, 3: 4, 4: 7}

for d in diff:
    if d == 1:
        c += 1
    else:
        if c > 0:
            ones.append(c)
        c = 0
print(ones)
mult = map(lambda x: dic[x], ones)
print(reduce(lambda x,y: x*y,mult))
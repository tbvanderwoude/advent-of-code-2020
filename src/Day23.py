from functools import reduce
from copy import deepcopy,copy
from collections import deque

def rot(ls,n):
    new_ls = []
    for i in range(len(ls)):
        new_ls.append(ls[(i+n)%len(ls)])
    return new_ls

def part1(input_str):
    labels = deque(map(int,list(input_str)))
    moves = 10
    c = labels[0]
    picked = []
    for i in range(moves):
        labels.rotate(-1) 
        for j in range(3):
            picked.append(labels.popleft())
        labels.rotate(1)
        dest = -1
        for sub in range(1,10):
            cand = (c-sub)%10
            # # print(cand)
            if cand in labels:
                dest = cand 
                break
        c = labels[1] 
        labels.rotate(-1)
        dest_index = labels.index(dest)
        labels.rotate(-dest_index-1)
        labels.extendleft(reversed(picked))
        labels.rotate(dest_index+1)
        picked = []
    onedex = labels.index(1)
    after_1 = rot(labels,onedex)
    after_1.remove(1)
    return "".join(map(str,after_1))

def part2(input_str):
    pass

# imagine 10 11 12 ... 10000000 at the end
blocks = "247819356"
print(part1(blocks))
print(part2(blocks))





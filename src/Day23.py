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
    moves = 100
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

def to_str(nxt,start):
    s = ""
    it = start
    for i in range(len(nxt)-1):
       s+= str(it)
       it = nxt[it]
    return s

    
def part2(input_str):
    labels = list(map(int,list(input_str)))
    n = 1000000 
    m = 10000000
    nxt = [0] * (n+1)
    for i in range(n+1):
        if i==0:
            nxt[0]=-1
        elif i>=1 and i<=8:
            nxt[labels[i-1]] = labels[i]
        elif i==9:
            nxt[labels[8]] = i+1 
        elif i==n:
            nxt[i] = labels[0] 
        else:
            nxt[i] = i+1
    current = labels[0]
    for i in range(m):
        p1 = nxt[current]
        p2 = nxt[p1]
        p3 = nxt[p2]
        nxt[current] = nxt[p3]
        p = [p1,p2,p3]
        dest  = current
        while dest in p or dest==current:
            if dest == 1:
                dest = n
            else:
                dest-=1
        nxt_new = nxt[dest]
        nxt[p3] = nxt_new
        nxt[dest] = p1
        current = nxt[current]
    n1 = nxt[1]
    n2 = nxt[n1]
    return n1*n2


# imagine 10 11 12 ... 10000000 at the end
blocks = "247819356"
print("Part 1: %s"%part1(blocks))
print("Part 2: %i"%part2(blocks))

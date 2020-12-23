from functools import reduce
from copy import deepcopy,copy

def rot(ls,n):
    new_ls = []
    for i in range(len(ls)):
        new_ls.append(ls[(i+n)%len(ls)])
    return new_ls

#blocks = open("inputs/input23.txt","r").read().strip()
# imagine 10 11 12 ... 10000000 at the end
blocks = "247819356"
labels = list(map(int,list(blocks)))
print(labels)
moves = 10000000
c = labels[0]
picked = []
for i in range(moves):
    picked = []
    for j in range(3):
        picked.append(labels.pop(1))
    # print("Picked up:")
    # print(picked)
    dest = -1
    # print(labels)
    for sub in range(1,10):
        cand = (c-sub)%10
        # print(cand)
        if cand in labels:
            dest = cand 
            break
    # print("Dest: %i"%dest)

    c = labels[1] 
    # print("New current: %i"%c)
    labels = rot(labels,1)
    dest_index = labels.index(dest)
    labels = labels[0:dest_index+1]+picked+labels[dest_index+1:]
    # print(labels)
print(labels)
onedex = labels.index(1)
after_1 = rot(labels,onedex)
after_1.remove(1)
print("".join(map(str,after_1)))





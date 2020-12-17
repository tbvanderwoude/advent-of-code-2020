from copy import deepcopy

def enum_neigh(x,y,z):
    neigh = set()
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                if not (dx==0 and dy==0 and dz==0):
                    neigh.add((x+dx,y+dy,z+dz))
    return neigh
def count_active(x,y,z,active):
    return len(list(filter(lambda x: x in active,enum_neigh(x,y,z))))
def gen_to_check(active):
    neigh = deepcopy(active)
    for coord in active:
        neigh = neigh.union(enum_neigh(*coord))
    return neigh

ls = open("inputs/input17.txt", "r").read().strip().splitlines()
print(len(enum_neigh(0,0,0)))
print(ls)
active = set()
for (x,l) in enumerate(ls):
    for (y,c) in enumerate(list(l)):
        # print(x,y,c)
        if c == '#':
            active.add((x,y,0))
print(active)
for i in range(6):
    to_check = gen_to_check(active)
    # print(to_check)
    new_active = deepcopy(active)
    for coord in to_check:
        c = count_active(*coord,active)
        if coord in active:
            if not (c == 2 or c==3):
                new_active.remove(coord)
        else:
            if c==3:
                new_active.add(coord)
    active=new_active
    print(len(active))
# rs = list(map(lambda s: list(s.strip()),ls))
# w = len(rs[0])
# h = len(rs)
# change = True
# i = 0
# while change:
#     change=False
#     print("State %i"%(i))
#     ns = deepcopy(rs)
#     # for r in rs:
#     #     print(r)
#     for x in range(w):
#         for y in range(h):
#             neigh = trace_neigh(rs,x,y,w,h)
#             # print(neigh)
#             cv = rs[y][x]
#             if cv=='L' and len(list(filter(lambda t: t=='#',neigh)))==0:
#                 ns[y][x] ='#'
#                 change=True
#             if cv=='#' and len(list(filter(lambda t: t=='#',neigh)))>=5:
#                 ns[y][x] ='L'
#                 change=True
#     i+=1
#     rs = ns
# empty_count = sum(map(lambda r:len(list(filter(lambda t: t=='#',r))),rs))
# print(empty_count)
# print("The grid is %ix%i"%(w,h))
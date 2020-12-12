from enum import IntEnum
class Dir(IntEnum):
    NORTH=0,
    EAST=1,
    SOUTH=2,
    WEST=3

deltamap = { Dir.NORTH: (0,1),Dir.EAST: (-1,0),Dir.SOUTH: (0,-1),Dir.WEST: (1,0)}
ls = open("inputs/input12.txt", "r").read().strip().splitlines()
ms = []
for l in ls:
    i = l[0]
    n = int(l[1:])
    ms.append((i,n))


x = 0
y = 0
dir = Dir.EAST
for (i,n) in ms:
    # print((i,n))
    # print(x,y)
    move_dir = dir
    if i == 'L':
        dir = Dir((int(dir)-n/90)%4)
    elif i == 'R':
        dir = Dir((int(dir)+n/90)%4)
    else:
        if i == 'N':
            move_dir = Dir.NORTH
        if i == 'S':
            move_dir = Dir.SOUTH
        if i == 'E':
            move_dir = Dir.EAST
        if i == 'W':
            move_dir = Dir.WEST
        if i == 'F':
            move_dir = dir
        (dx, dy) = deltamap[move_dir]
        x+=dx*n
        y+=dy*n

def rot(x,y,n):
    fx = x
    fy = y
    for i in n/90:
        t = fx
        fx = fy
        fy = -t
    return (fx,fy)



print(abs(x)+abs(y))
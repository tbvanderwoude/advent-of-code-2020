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
    s = 1
    if n<0:
        s = -1
        n = abs(n)
    for i in range(n//90):
        t = fx
        fx = fy*s
        fy = -t*s
    return (fx,fy)
print(rot(3,1,90))
print(rot(3,1,-90))


sx = 0
sy = 0
wx = -10
wy = 1
print("Ship: (%i,%i); Waypoint: (%i,%i)" % (sx, sy, wx, wy))
for (i,n) in ms:
    move_dir = -1
    if i == 'L':
        wx,wy = rot(wx,wy,n)
    elif i == 'R':
        wx,wy = rot(wx,wy,-n)
    elif i == 'F':
        sx += wx*n
        sy += wy*n
    else:
        if i == 'N':
            move_dir = Dir.NORTH
        if i == 'S':
            move_dir = Dir.SOUTH
        if i == 'E':
            move_dir = Dir.EAST
        if i == 'W':
            move_dir = Dir.WEST
        (dx, dy) = deltamap[move_dir]
        wx+=dx*n
        wy+=dy*n
    print("Instruction: (%c %i); Ship: (%i,%i); Waypoint: (%i,%i)"%(i,n,sx,sy,wx,wy))

print(abs(x)+abs(y))
print(abs(sx)+abs(sy))
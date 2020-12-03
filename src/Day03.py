from functools import reduce
forest = open("inputs/input03.txt", "r").read().splitlines()
directions = [(1,1),(3,1),(5,1),(7,1),(1,2)];
counts =list(map( lambda d:sum(map(lambda y:int(forest[y][(y*d[0]//d[1]) % len(forest[0])]=='#'), filter(lambda y: y%d[1]==0, range(0,len(forest))))), directions))

print(counts)
print(reduce(lambda x,r: x*r,counts))

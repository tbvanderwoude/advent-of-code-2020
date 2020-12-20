file1 = open("inputs/input01.txt", "r")
lines = list(map(lambda x: int(x), file1.readlines()))
part1 = [x * y for x in lines for y in lines if (x + y) == 2020][0]
part2 = [x * y * z for x in lines for y in lines for z in lines if (x + y + z) == 2020][
    0
]
print(part1)
print(part2)

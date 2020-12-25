def transform(n, loops):
    k = 1
    for l in range(loops):
        k = (k * n) % 20201227
    return k


def find_loop(n):
    k = 1
    i = 0
    while k != n:
        k = (k * 7) % (20201227)
        i += 1
    return i


door, card = tuple(map(int, open("inputs/input25.txt", "r").read().splitlines()))
door_loop, card_loop = find_loop(door), find_loop(card)
print(transform(door, card_loop))

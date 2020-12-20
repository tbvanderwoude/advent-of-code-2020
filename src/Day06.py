ps = list(
    map(
        lambda b: len(set.intersection(*map(lambda l: set(l), b.split("\n")))),
        open("inputs/input06.txt", "r").read().split("\n\n"),
    )
)
print(sum(ps))

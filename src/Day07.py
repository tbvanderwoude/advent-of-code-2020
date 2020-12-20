import re

ps = open("inputs/input07.txt", "r").read().strip().splitlines()
e1 = re.compile(r"^(\w+ \w+)")
e2 = re.compile(r"(\d+) (\w+ \w+)")
rules = {}
# what have we learned today? overcomplicating input processing causes bugs, once input is garbled
# nothing you do with it later can save it, not even implementing three variations of the same thing...
for s in ps:
    rules[e1.match(s)[0]] = list(map(lambda x: (int(x[0]), x[1]), e2.findall(s)))


def bags(root):
    if not rules[root]:
        return 1
    return 1 + sum([num * (bags(col)) for (num, col) in rules[root]])


def contains(root, leaf):
    if root == leaf:
        return True
    contain = False
    for (num, prod_color) in rules[root]:
        if prod_color != root and contains(prod_color, leaf):
            contain = True
            break
    return contain


print(sum([contains(key, "shiny gold") for key in rules]) - 1)
print(bags("shiny gold") - 1)

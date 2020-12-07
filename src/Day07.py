import re

ps = open("inputs/input07.txt", "r").read().splitlines()
e1 = re.compile(r'^(\w+ \w+)')
e2 = re.compile(r'(\d+) (\w+ \w+)')
rules = {}
# rules = {(b := ln.replace(" bags", "").replace(" bag", "").split(" contain "))[0]: {c[2::]: int(c[0]) for c in b[1].strip().replace(".", "").split(", ") if c != "no other"} for ln in open("inputs/input07.txt").readlines()}

for s in ps:
    if s:
        rules[e1.match(s)[0]] = list(map(lambda x: (int(x[0]),x[1]), e2.findall(s)))

print(rules)

# colors = ["shiny gold"]

# prev = {"shiny gold" : 1}
# bags = set()
# while len(prev) > 0:
#     prev = set(b for b in rules for p in prev if p in rules[b])
#     bags |= prev
# print(len(bags))
# new_color = True
#
# while new_color:
#     new_color = False
#     for (color, rule) in rules.items():
#         for (num,prod_color) in rule:
#             if prod_color in colors and color not in colors:
#                 # print("%s also works as it produces %s" % (color, prod_color))
#                 colors.append(color)
#                 new_color = True
#                 # print(colors)
def bags(root):
    if not rules[root]:
        return 1
    return 1+sum([num*(bags(col)) for (num,col) in rules[root]])

def contains(root, leaf):
    if root == leaf:
        return True
    contain = False
    for (num,prod_color) in rules[root]:
        if prod_color!=root and contains(prod_color, leaf):
            contain = True
    return contain

print(sum([contains(key,"shiny gold") for key in rules])-1)
print(bags("shiny gold")-1)

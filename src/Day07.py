import re

ps = open("inputs/input07.txt", "r").read().splitlines()
r = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
e1 = re.compile(r'(\w+ \w+) bags contain ((\d+) (\w+ \w+) bags*, )*((\d+) (\w+ \w+) bags*.)')
e2 = re.compile(r'(\w+ \w+) bags contain no other bags.')
rules = {}
for s in ps:
    matches = e1.match(s)
    if matches:
        grps = list(filter(lambda x: x, matches.groups()))
        # print(grps)
        if grps[0] in rules:
            print("This is already in there!")
        rules[grps[0]] = list(
            zip([int(grps[i]) for i in range(2, len(grps), 3)], [grps[i] for i in range(3, len(grps), 3)]))
        rules[grps[0]].append((1,grps[0]))
    matches2 = e2.match(s)
    if matches2:
        grps = matches2.groups()
        rules[grps[0]] = []
print(rules)

colors = ['shiny gold']

new_color = True
while new_color:
    new_color = False
    for (color, rule) in rules.items():
        for (prod_count, prod_color) in rule:
            if prod_color in colors and color not in colors:
                print("%s also works as it produces %s" % (color, prod_color))
                colors.append(color)
                new_color = True
                # print(colors)

print("Out of %s bag colors (excluding shiny gold), %s should contain gold bags" % (len(rules), len(colors) - 1))
# print(e1.match(ps[2]).groups())

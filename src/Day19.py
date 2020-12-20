from functools import reduce
import re

parts = list(open("inputs/input19.txt", "r").read().split("\n\n"))

print(parts)
rs = parts[0].splitlines()
msgs = parts[1].splitlines()
rules = dict(map(lambda t: (int(t[0]), t[1]), map(lambda l: tuple(l.split(":")), rs)))
print(rs)
print(rules)

cache = {}


def solve_rule(i, rules):
    if i in cache:
        return cache[i]
    else:
        j = 0
        rule = rules[i]
        s = ""
        while j < len(rule):
            if rule[j].isdigit():
                start = j
                while j < len(rule) and rule[j].isdigit():
                    j += 1
                end = j
                rid = int(rule[start:end])
                # print("RID: %i"%(rid))
                sub_s = solve_rule(rid, rules)
                s += "(" + sub_s + ")"
            elif rule[j] != '"' and rule[j] != " ":
                s += rule[j]
            j += 1
        cache[i] = s
        return s


# print(solve_rule(0,{0:"1 | 12",1:"\"a\"",12:"\"b\""}))
exp = solve_rule(0, rules)
r = re.compile(exp)
print(solve_rule(0, rules))
print(len(list(filter(r.fullmatch, msgs))))
cache = {}
print(rules[8], rules[11])
rules[8] = " 42 "
rules[11] = " 42 31 "
for i in range(2, 6):
    rules[8] += "|" + " 42 " * i
    rules[11] += "|" + " 42 " * i + " 31 " * i
exp = solve_rule(0, rules)
r = re.compile(exp)
print(solve_rule(0, rules))
print(len(list(filter(r.fullmatch, msgs))))

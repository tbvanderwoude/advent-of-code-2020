ls = list(map(lambda l: l.replace(" ",""),open("inputs/input18.txt", "r").read().strip().splitlines()))
found_bracket = False


def match_bracket(s, i):
    open_index = i
    closed_index = -1
    inner_c = 0
    for j in range(i + 1, len(s)):
        if s[j] == '(':
            inner_c += 1
        if s[j] == ')':
            if inner_c == 0:
                closed_index = j
                break
            else:
                inner_c -= 1
    return open_index, closed_index

def eval(s):
    r = 0
    op = lambda x: r + x
    i = 0
    while i != len(s):
        c = s[i]
        if c == '+':
            op = lambda x: r + x
        if c == '*':
            op = lambda x: r * x
        if c == '(':
            (open_index, closed_index) = match_bracket(s, i)
            v = eval(s[open_index + 1:closed_index])
            r = op(v)
            i = closed_index
        if c.isdigit():
            r = op(int(c))
        i += 1
    return r

part1 = sum(map(lambda l: eval(l), ls))
print(ls[0])
print(eval(ls[0]))

print(part1)
# print(part2)

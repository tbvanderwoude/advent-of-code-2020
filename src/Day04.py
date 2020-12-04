import re

ps = open("inputs/input04.txt", "r").read().split("\n\n")
r = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
exp = {"byr": re.compile('19[2-9]\\d|200[0-2]'),
       "iyr": re.compile('201\\d|2020'),
       "eyr": re.compile('202\\d|2030'),
       "hgt": re.compile('(15\\d|1[6-8]\\d|19[0-3])cm|(59|6\\d|7[0-6])in'),
       "hcl": re.compile('#[0-9|a-f]{6}'),
       "ecl": re.compile('amb|blu|brn|gry|grn|hzl|oth'),
       "pid": re.compile('\\d{9}')}
print(sum([int(r.issubset(set(map(lambda z: z[0], filter(lambda y: (y[0] not in exp) or exp[y[0]].fullmatch(y[1]), map(lambda x: x.split(":"), p.split())))))) for p in ps]))

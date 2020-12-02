import re
matches = re.findall( r'(\d+)-(\d+) (\w): (\w+)', open('inputs/input02.txt', 'r').read())
print(len ([x for x in matches if x[3].count(x[2])<=int(x[1]) and x[3].count(x[2])>=int(x[0])]))
print(len ([x for x in matches if (x[3][int(x[1])-1]==x[2]) != (x[3][int(x[0])-1]==x[2])]))

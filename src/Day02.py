import re
def check_password_policy_1(x):
     return x[3].count(x[2])<=int(x[1]) and x[3].count(x[2])>=int(x[0])
def check_password_policy_2(x):
    return (x[3][int(x[1])-1]==x[2]) != (x[3][int(x[0])-1]==x[2])

matches = re.findall( r'(\d+)-(\d+) (\w): (\w+)', open('inputs/input02.txt', 'r').read())
correct_passwords_1 = [x for x in matches if check_password_policy_1(x)]
correct_passwords_2 = [x for x in matches if check_password_policy_2(x)]

print (len(correct_passwords_1))
print (len(correct_passwords_2))

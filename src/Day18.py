ls = open("inputs/input18.txt", "r").read().strip().splitlines()
found_bracket = False
def eval(s):
    r = 0
    op = lambda x,y: x+y
    i = 0
    while i!=len(s):
        c = s[i]
        if c == '+':
            op = lambda x,y: x+y
        if c == '*':
            op = lambda x,y: x*y
        if c == '(':
            open_index = i
            closed_index = -1
            inner_c = 0
            for j in range(i+1,len(s)):
                if s[j]=='(':
                    inner_c+=1
                if s[j]==')':
                    if inner_c==0:
                        closed_index = j
                        break
                    else:
                        inner_c-=1
            v = eval(s[open_index+1:closed_index])
            print("Subexpression [%i,%i] evaluated to %i"%(open_index+1,closed_index,v))
            r = op(r,v)
            i = closed_index
        if c.isdigit():
            r = op(r,int(c))
        i+=1
    return r
part1 = sum(map(lambda l: eval(l),ls))
print(part1)
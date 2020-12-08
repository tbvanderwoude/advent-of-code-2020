import re

def sim(instr):
    progcount = 0
    progcounts = set()
    acc = 0
    while progcount not in progcounts:
        if progcount>=len(instr):
            return (True,acc)
        progcounts.add(progcount)
        (opcode, arg) = instr[progcount]
        if opcode == "jmp":
            progcount += arg
        elif opcode == "nop":
            progcount += 1
        elif opcode == "acc":
            acc += arg
            progcount += 1
    return (False,acc)

ps = open("inputs/input08.txt", "r").read().strip().splitlines()
e = re.compile(r'(nop|acc|jmp) ([+-]\d+)')
rules = {}
# what have we learned today? overcomplicating input processing causes bugs, once input is garbled
# nothing you do with it later can save it, not even implementing three variations of the same thing...
instr = []
for s in ps:
    groups = e.match(s).groups()
    opcode = groups[0]
    arg = int(groups[1])
    instr.append((opcode,arg))
    print("%s: %i"%(opcode,arg))

jmp_nop_indices = filter(lambda x: x[1][0]=="nop" or x[1][0]=="jmp",enumerate(instr))

for (i, (op,arg)) in jmp_nop_indices:
    # subs
    if op=="jmp":
        instr[i] = ("nop",arg)
        ret = sim(instr)
        if ret[0]:
            print(ret[1])
        instr[i]= ("jmp",arg)
    if op == "nop":
        instr[i] = ("jmp",arg)
        ret = sim(instr)
        if ret[0]:
            print(ret[1])
        instr[i] = ("nop",arg)

print(sim(instr))
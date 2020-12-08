import re

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

progcount = 0
progcounts = set()
acc = 0
while progcount not in progcounts:
    progcounts.add(progcount)
    (opcode, arg) = instr[progcount]
    if opcode=="jmp":
        progcount+=arg
    elif opcode=="nop":
        progcount+=1
    elif opcode=="acc":
        acc+=arg
        progcount+=1
print(acc)
import re

ls = open("inputs/input14.txt", "r").read().splitlines()
memory = {}
mask = {}
e1 = re.compile(r'mask = ([\d|X]+)')
e2 = re.compile(r'mem\[(\d+)\] = (\d+)')
for l in ls:
    mask_match = e1.match(l)
    write_match = e2.match(l)
    if mask_match:
        mask = {}
        for (i,mask_symbol) in enumerate(list(mask_match.groups()[0])):
            if mask_symbol!='X':
                mask[i] = mask_symbol
        print(mask)
    elif write_match:
        grps = write_match.groups()
        addr = int(grps[0])
        val = int(grps[1])
        bin_str_val = list(f'{val:036b}')
        for m in mask:
            bin_str_val[m] = mask[m]
        bin_str_val = "".join(bin_str_val)
        memory[addr] = int(bin_str_val,2)
    else:
        print("No match???")
# print(memory)
s = 0
for m in memory:
    s+=memory[m]
print("Part1: %i"%(s))
# print(ls)
# print(ls[1])
# mask = ls[0]
# writes = list(map(lambda xs: list(map(lambda x: (int(x[0]),int(x[1])), e2.findall(xs)))[0],ls[1:]))
# print(writes)
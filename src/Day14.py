import re

ls = open("inputs/input14.txt", "r").read().splitlines()
memory = {}
mask = {}
e1 = re.compile(r'mask = ([\d|X]+)')
e2 = re.compile(r'mem\[(\d+)\] = (\d+)')
# V1 protocol
for l in ls:
    mask_match = e1.match(l)
    write_match = e2.match(l)
    if mask_match:
        mask = {}
        for (i,mask_symbol) in enumerate(list(mask_match.groups()[0])):
            if mask_symbol!='X':
                mask[i] = mask_symbol
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
s = 0
for m in memory:
    s += memory[m]
print("Part1: %i" % (s))
def construct_addresses(str):
    h,t = str[:1],str[1:]
    if len(str)==1:
        if h == '0':
            return [0]
        if h == '1':
            return [1]
        if h == 'X':
            return [0,1]
    if h=='0':
        return list(map(lambda x: 0+2*x,construct_addresses(t)))
    if h=='1':
        return list(map(lambda x: 1+2*x,construct_addresses(t)))
    if h=='X':
        return list(map(lambda x: 0+2*x,construct_addresses(t)))+list(map(lambda x: 1+2*x,construct_addresses(t)))
    return []
# print(construct_addresses("0XX01"[::-1]))
memory = {}
#V2 protocol
for l in ls:
    mask_match = e1.match(l)
    write_match = e2.match(l)
    if mask_match:
        mask = mask_match.groups()[0]
        print("\nMask: "+mask)
    elif write_match:
        grps = write_match.groups()
        addr = int(grps[0])
        val = int(grps[1])
        bin_str_val = list(f'{addr:036b}')
        print("\nBefore: "+f'{addr:036b}')
        for (i,m) in enumerate(mask):
            if m=='1' or m=='X':
                bin_str_val[i] = m
        bin_str_val = "".join(bin_str_val)
        print("\nAfter: "+bin_str_val)
        addresses = construct_addresses(bin_str_val[::-1])
        for addr in addresses:
            memory[addr] = val
    else:
        print("No match???")
s = 0
for m in memory:
    s += memory[m]
print("Part2: %i" % (s))
ps = open("inputs/input09.txt", "r").read().strip().splitlines()
num = list(map(lambda x:int(x),ps))
pream = 25
# print(num[pream:])
p1 = 0
for (i,n) in enumerate(num[pream:],pream):
    sum_of = False
    # print(num[i-pream:i])
    for x in num[i-pream:i]:
        for y in num[i - pream:i]:
            if n==x+y:
                sum_of = True
    if not sum_of:
        p1 = n
        break
print(p1)

for (i,n) in enumerate(num[0:len(num)-1]):
    sum = 0
    l_ix = i
    h_ix = i
    for (j, m) in enumerate(num[i:],i):
        if sum>=p1:
            break
        else:
            h_ix = j
            sum += m
    if sum==p1 and h_ix!=l_ix:
        r = num[l_ix:h_ix+1]
        print("The range is indices (%i,%i), the sum: %i"%(l_ix,h_ix,min(r)+max(r)))
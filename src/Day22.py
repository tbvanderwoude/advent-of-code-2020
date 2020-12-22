from functools import reduce
blocks = open("inputs/input22.txt","r").read().split("\n\n")
print(blocks)

decks = list(map(lambda b: reversed(list(map(int,b.split(":\n")[1].splitlines()))),blocks))
p1 = list(decks[0])
p2 = list(decks[1])
while p1 and p2:
    p1_c = p1.pop()
    p2_c = p2.pop()
    if p1_c>p2_c:
        p1.insert(0,p1_c)
        p1.insert(0,p2_c)
    else:
        p2.insert(0,p2_c)
        p2.insert(0,p1_c)
if p1:
    mult_score = list(enumerate(list(p1),1))
    print(mult_score)
    score = sum(map(lambda x: x[0]*x[1],mult_score))
    print("Player 1 wins with %i points"%(score))
if p2:
    mult_score = list(enumerate(list(p2),1))
    print(mult_score)
    score = sum(map(lambda x: x[0]*x[1],mult_score))
    print("Player 2 wins with %i points"%(score))

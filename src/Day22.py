from functools import reduce
from copy import deepcopy,copy

def play_combat(p1,p2,rec):
    if rec:
        rec_game(1,p1,p2)
    else:
        game(p1,p2)
    if p1:
        print("Player 1 wins with %i points"%comp_score(p1))
    if p2:
        print("Player 2 wins with %i points"%comp_score(p2))

def rec_game(i,p1,p2):
    rounds = set()
    r = 1
    while p1 and p2:
        if tuple(p1+[-1]+p2) in rounds:
            return 1
        else:
            rounds.add(tuple(p1+[-1]+p2))
        p1_c = p1.pop()
        p2_c = p2.pop()
        winner = -1
        if p1_c<=len(p1) and p2_c<=len(p2):
            winner = rec_game(i+1,copy(p1[len(p1)-p1_c:]),copy(p2[len(p2)-p2_c:]))
        elif p1_c>p2_c:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1.insert(0,p1_c)
            p1.insert(0,p2_c)
        else:
            p2.insert(0,p2_c)
            p2.insert(0,p1_c)
        r+=1
    if p1:
        return 1
    else:
        return 2
def game(p1,p2):
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
        return 1
    else:
        return 2
    
def comp_score(cards):
    return sum(map(lambda x: x[0]*x[1],list(enumerate(list(cards),1))))

blocks = open("inputs/input22.txt","r").read().split("\n\n")

decks = list(map(lambda b: list(reversed(list(map(int,b.split(":\n")[1].splitlines())))),blocks))
play_combat(list(decks[0]),list(decks[1]),False)
play_combat(list(decks[0]),list(decks[1]),True)

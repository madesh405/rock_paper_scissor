'''rock paper scissor game with random'''
from random import choice

weapons=["rock","paper","scissor"]


def computer_choice(weapons:list) -> str:     #the choice of computer
    crps=choice(weapons)
    return crps


def player_choice(weapons:list) -> str:       #the players's choice
    print("\n\nwelcome to rock paper scissor game")
    print("pick 1 for Rock")
    print("pick 2 por Paper")
    print("pick 3 for Scissor")
    intprps=int(input("enter you choice 1, 2 or 3 : "))
    prps=weapons[intprps-1]
    return prps

'''             ***Rules of the game***

1.Rock beats scissor
2.Scissor beats paper
3.Paper beats rock

'''

def rules(crps:str,prps:str,weapons:list) -> int:
    if crps==prps:
        return [0,0]    #(computers point, players point)

    if crps==weapons[0]:
        if prps==weapons[1]:
            return [0,1]
        elif prps==weapons[2]:
            return [1,0]

    elif crps==weapons[1]:
        if prps==weapons[0]:
            return [1,0]
        elif prps==weapons[2]:
            return [0,1]

    elif crps==weapons[2]:
        if prps==weapons[0]:
            return [0,1]
        elif prps==weapons[1]:
             return [1,0]


#__main__

score=[0,0]
game=True
while game:
    crps=computer_choice(weapons)
    prps=player_choice(weapons)
    print("cmputer:",crps,"player:",prps,"\n\n")
    curscore=rules(crps,prps,weapons)
    score=[curscore[0]+score[0],curscore[1]+score[1]]
    cont=input("wanna continue? (y,n) ")
    if cont=="n":
        break

print("the scores are computer",score[0],"player",score[1])

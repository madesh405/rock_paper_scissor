'''rock paper scissor game with random'''
from random import choice

weapons=["rock","paper","scissor"]


def computer_choice(weapons:list) -> str:     #the choice of computer
    crps=choice(weapons)
    return crps



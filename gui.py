''' GUI for the Rock Paper Scissor game'''
import tkinter as tk
from random import choice

def crps():
    weapons=["rock","paper","scissor"]
    c=choice(weapons)
    return c

def prps(n:int) -> str:
    weapons=["rock","paper","scissor"]
    c=crps()
    print("player :",weapons[n],"\ncomputer :",c,"\n")



root=tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry('800x500')

r=tk.Button(root,text="Rock",command=lambda:prps(0))
p=tk.Button(root,text="Paper",command=lambda:prps(1))
s=tk.Button(root,text="Scissor",command=lambda:prps(2))
r.pack()
p.pack()
s.pack()




root.mainloop()

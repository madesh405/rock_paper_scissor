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
root.geometry('700x500')
photo1 = tk.PhotoImage(file = "rock.png")
photo2 = tk.PhotoImage(file = "paper.png")
photo3 = tk.PhotoImage(file = "scissor.png")
r=tk.Button(root,text="Rock",image=photo1,command=lambda:prps(0))
p=tk.Button(root,text="Paper",image=photo2,command=lambda:prps(1))
s=tk.Button(root,text="Scissor",image=photo3,command=lambda:prps(2))
r.grid(row=1,column=0)
p.grid(row=1, column=1)
s.grid(row=1,column=2)




root.mainloop()

''' GUI for the Rock Paper Scissor game'''
import tkinter as tk


def rock():
    prps(0)
def paper():
    prps(1)
def scissor():
    prps(2)

def prps(n:int) -> str:
    weapons=["rock","paper","scissor"]
    return weapons[n]



root=tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry('800x500')

r=tk.Button(root,text="Rock",command=rock)
p=tk.Button(root,text="Paper",command=paper)
s=tk.Button(root,text="Scissor",command=scissor)
r.pack()
p.pack()
s.pack()




root.mainloop()

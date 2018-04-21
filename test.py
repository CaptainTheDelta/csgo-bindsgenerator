import tkinter as tk

root = tk.Tk()

txt = tk.StringVar()
txt.set("e")

def change():
    print(k.get())

def bouton():
    for i in range(n-1):
        print(f"bind {keys[i].get()} '{cmds[i].get()}'")

f = tk.Frame(root)

key_label = tk.Label(f, text="Touche")
cmd_label = tk.Label(f, text="Commande")
key_label.grid(column=0,row=0)
cmd_label.grid(column=1,row=0)


keys = []
cmds = []
n = 1

for i in range(3):
    keys.append(tk.Entry(f, width=5))
    cmds.append(tk.Entry(f, width=30))

    keys[-1].grid(column=0,row=n)
    cmds[-1].grid(column=1,row=n)
    n += 1


valider = tk.Button(f, text="Valider", command=bouton)
valider.grid(row=n+1,column=1)

f.pack()

#def key(event):
#    print ("pressed",event.keysym_num)
#
#def callback(event):
#    frame.focus_set()
#    print ("clicked at", event.x, event.y)
#
#
#
#frame = Frame(root, width=150, height=100)
#frame.bind("<Key>", key)
#frame.bind("<Button-1>", callback)
#frame.pack()
#
root.mainloop()

class objet:
    def __init__(self,t):
        self.n = 0
        self.p(t)

    def p(self,t):
        print(self.n,t)
        self.n = 15

    def k(self):
        print(self.n)

e = objet(3)
e.k()

root = tk.Tk()

from random import randint

def rer():
    destroy.grid(row=randint(0,5),column=randint(0,5))

destroy = tk.Button(root, text="Kaboom", command=rer)
destroy.grid(row=randint(0,5),column=randint(0,5))


root.mainloop()

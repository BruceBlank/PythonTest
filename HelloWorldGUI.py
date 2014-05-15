#!/usr/bin/python

from Tkinter import Frame,Label,Button, TOP, LEFT, RIGHT, sys

def exitProgram(status):
    print "call exit"
    sys.exit(status)

def showDialog():
    win = Frame(padx=10, pady=10)
    win.pack()
    Label(win, text="Hallo Bruce!").pack(side=TOP)
    Button(win, text="Exit 0", command=(lambda: exitProgram(0))).pack(side=LEFT)
    Button(win, text="Exit 1", command=(lambda: exitProgram(1))).pack(side=RIGHT)
    win.mainloop()
    
showDialog()

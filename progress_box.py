from tkinter import *
from tkinter import ttk

win = Tk()

def func():
    import time
    prog['value'] = 20
    prog.update_idletasks()
    time.sleep(1)

    prog['value'] = 50
    prog.update_idletasks()
    time.sleep(1)

    prog['value'] = 100
    prog.update_idletasks()
    time.sleep(1)

win.title('Progress')
win.geometry('400x400')

prog = ttk.Progressbar(win,length=150,mode="determinate")
prog.pack()

btn = Button(win,text="start",command=func).pack()
win.mainloop()
from tkinter import *

win =  Tk()

def press(title):
    pass

win.title('photo')
win.geometry('500x300')

#only png format file accepted.
file =  PhotoImage(file="clock.png")

lbl = Label(win,image=file)
lbl.pack()

btn = Button(win,text="w",command= lambda : press('w')).pack()

win.mainloop()
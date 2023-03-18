from tkinter import *

win  = Tk()

win.title('List Box')
win.geometry('600x400')

def func():
    #anchor will delete the selected element.
    lst.delete(ANCHOR)

items = ['Apple','Banana','Mango','Strawberry','finchi','Maneche']

lst = Listbox(win,width=20)

for i in items:
    lst.insert(END,i)

lst.pack()

btn = Button(win,text="DELETE",command=func).pack()
win.mainloop()
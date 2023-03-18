from tkinter import *

win = Tk()

win.title('Menu Bar')
win.geometry('600x400')

My_menu = Menu(win)
win.config(menu=My_menu)

def func():
    pass

file_menu = Menu(My_menu)
My_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_cascade(label='new',command=func)
file_menu.add_cascade(label='open',command=func)

Edit_menu = Menu(My_menu)
My_menu.add_cascade(label='Edit',menu=Edit_menu)
Edit_menu.add_cascade(label='undo')
Edit_menu.add_separator()
Edit_menu.add_cascade(label='redo')

Help_menu = Menu(My_menu)
My_menu.add_cascade(label='Help',menu=Help_menu)

win.mainloop()

from tkinter import *
from tkinter import messagebox

wind = Tk()
wind.title('Message')
wind.geometry('500x300')

def func():
    if(vars.get() == ''):
        messagebox.showwarning('warning','Field must not be empty')
    else:
        messagebox.showinfo('success','Data inserted successfully')
        vars.set('')

vars = StringVar()
ent = Entry(textvariable=vars).pack()

btn = Button(text="submit",command=func).pack()

def ask():
    system =  messagebox.askyesno('Title','Do you want to exit ?')
    if(system == True):
        wind.destroy()

btns = Button(text="ask",command=ask).pack()
wind.mainloop()
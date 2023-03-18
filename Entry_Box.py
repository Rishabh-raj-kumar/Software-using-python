from tkinter import *

wind = Tk()

def func():
    ex = var.get()
    lb1.config(text=ex)

wind.title('Entry box')
wind.geometry('500x300')

lb1 = Label(wind,text="USERNAME",padx=4,pady=4,bg="red",fg="yellow")
lb1.place(x=10,y=10)

var = StringVar()
ent = Entry(wind,bd=3,textvariable=var)

ent.place(x=100,y=10,width=140,height=25)

btn = Button(text="submit",command=func)
btn.place(x=20,y=40)

wind.mainloop()
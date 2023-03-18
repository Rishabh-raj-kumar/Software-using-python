from tkinter import *

wind = Tk()

wind.title('label')
#size of window.
wind.geometry('400x400')

#bg -> background(background color of label) fg -> foreground(text color)
lab = Label(wind,text='USERNAME',bg="red",fg="yellow")
#if you will not use pack or grid or place it will give NAMING ERROR.
# lab.pack()
# lab.grid(row=1,column=1)
lab.place(x=10,y=100)

lab2 = Label(wind,text='PASSWORD',bg="green",fg="yellow",width=10)
lab2.place(x=10,y=130)

#giving some padings
lab3 = Label(wind,text="EMAIL",width=10,bg="black",fg="white",padx=8,pady=8)
lab3.place(x=10,y=160)

wind.mainloop()
from tkinter import *

wind = Tk()
wind.geometry('500x300')
wind.title('radio')

def passes():
    print(rd1.get())
    print(rd2.get())

rd1 = IntVar()
rd2 = IntVar()

#create two radio button with same variable
rdb1 = Radiobutton(wind,text='Male',value=1,variable=rd1).pack()
rdb1 = Radiobutton(wind,text="Female",value=0,variable=rd2).pack()

btn = Button(wind,text='submit',command=passes).pack()

wind.mainloop()
from tkinter import *

wind = Tk()
wind.title('checks')
wind.geometry('500x300')

def func():
    print(check1.get())
    print(check2.get())
    
check1 = IntVar()
check2 = IntVar()

ckb = Checkbutton(wind,text='Male',variable=check1,onvalue=1,offvalue=0)
ckb.pack()

ckb2 = Checkbutton(wind,text="Women",variable=check2,onvalue=1,offvalue=0)
ckb2.pack()

btn = Button(text="Get Data",command=func).pack()

wind.mainloop()
from tkinter import *

wind = Tk()
wind.title('Frame')
wind.geometry('500x300')

topHeader = Frame(wind)
topHeader.pack()

BottomHeader = Frame(wind)
BottomHeader.pack(side=BOTTOM)

label = Label(topHeader,text="This is a Header").pack()

label = Label(BottomHeader,text="This is a Footer").pack()
wind.mainloop()
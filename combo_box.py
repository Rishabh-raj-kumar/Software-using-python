from tkinter import *
from tkinter import ttk

win = Tk()

win.title('Combo Box')
win.geometry('500x300')

var  = StringVar()

com = ttk.Combobox(win,width=20)
com['values'] = ('January','February','March')
#select the first value as current.
com.current(0)
#but the problrem is that it is editable so set it readonly
com['state'] = 'readonly'

com.place(x=10,y=10)
win.mainloop()
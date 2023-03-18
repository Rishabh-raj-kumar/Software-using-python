#Basic starter pack
# from tkinter import *
# wind = Tk()
# #it will run like a loop.
# wind.mainloop()

from tkinter import *

wind = Tk()
wind.title('windows') #any title of your choice.
#to set the icon you need an ico file or image.
wind.iconbitmap('message.ico')

#sizes.
wind.minsize(width=400,height=400)
# wind.maxsize(width=300,height=300)

#it will run like a loop.
wind.mainloop()
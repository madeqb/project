from tkinter import *
from tkinter import colorchooser
def choose_color():
   color_code = colorchooser.askcolor(title='Choose color')
   print(color_code)
root = Tk()

button = Button ( root, text= 'Select color',
         command= choose_color ,
         fg= 'yellow', bg='blue',
         font= ('Times New Roman', 32),
         width= len ('Select color') + 10)

button.place(x=0, y=0)

root.geometry('540x90')

root.configure(background='lightblue')

root.mainloop()
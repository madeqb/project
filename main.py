from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk , Image

root = Tk ()
root.geometry ('1500x890')
root.title ('main title')

WelcomeL = Label (root , text='Lotfan Sabtenam Konid Ya Varede Hesabetan Shavid: ',
                        fg= 'white', bg='green',
                        font= ("Times New Roman",32),
                        width= len ('Lotfan Sabtenam Konid Ya Varede Hesabetan Shavid: ') + 10)
WelcomeL.pack ()                        
root.mainloop ()
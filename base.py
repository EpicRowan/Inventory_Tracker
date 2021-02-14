from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()

#Database
conn = sqlite3.connect('shrimp_data.db')
c = conn.cursor()

mainloop()
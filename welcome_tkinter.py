import math
import random
import abteil_constructor
from abteil_1 import *
from tkinter import *

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry("800x600+200+200")

# tkinter-Elemente erzeugen
frame = Frame(bd=3, relief="raised")
label_username = Label(frame, text="Gibt deinen Spieler*innen Namen an:")
text_username = Entry(frame)

label_urlaubsgeld = Label(frame)

frame.pack(pady=10)
label_username.pack(pady=10)
text_username.pack()

app.mainloop()
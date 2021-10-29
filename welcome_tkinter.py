import math
import random
import abteil_constructor
from abteil_1 import *
from tkinter import *

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry("800x600+200+200")


def welcome(e):
    urlaubsgeld = random.randrange(90, 110)
    abteil_1.assign_inventar(urlaubsgeld)
    text_username.pack_forget()


# tkinter-Elemente erzeugen
frame = Frame(bd=3, relief="raised", background="aquamarine")
label_username = Label(frame, text="Gib deinen Spieler*innen Namen an:")
text_username = Entry(frame, background="teal")
text_username.bind("<Return>", welcome)


label_welcome = Label(frame, text="")
label_urlaubsgeld = Label(frame)

frame.pack(pady=10)
label_username.pack(pady=10)
text_username.pack()
label_welcome.pack()

app.mainloop()

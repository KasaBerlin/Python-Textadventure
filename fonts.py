from tkinter import *
from tkinter import font

app = Tk()

font_list = list(font.families())
for font_one in font_list:
    print(font_one)
    font_one

label = Label(text=f"Hallo  {font_one}").pack()


app.mainloop()

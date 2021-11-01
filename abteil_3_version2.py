from tkinter import *
from tkinter import messagebox
import random
import time

app = Tk()
app.title("Reise im Bergland-Express")
app.geometry("1300x700+200+30")
app.resizable(0, 0)

label_instructions = Label(
    app,
    text="""Der Lokführer kommt panisch auf dich zugerannt und bittet um deine Hilfe.\n
    Durch die Kälte in den Bergen, ist die Bremse eingefroren...\n Der Lokführer kümmert sich schon darum,
    aber um den Zug auf den Schienen zu halten, musst du beim Lenken helfen.
    \nDrücke die Pfeiltaste in die angezeigte Richtung.""",
).pack(pady=20)

directions = ["Left", "Right", "Up", "Down"]
counter = 0


def right_direction(e):
    global counter
    key_press = e.keysym
    while counter < 50:
        counter += 1
        if key_press == label_direction["text"]:
            label_counter.config(text="Punkte:" + str(counter))
        label_direction.config(text=random.choice(directions))


label_direction = Label(app, text=random.choice(directions))
label_direction.pack(pady=20)

input_direction = Entry(app)
input_direction.pack(pady=20)

label_counter = Label(app, text="Punkte:" + str(counter))
label_counter.pack()

input_direction.bind("<Left>", right_direction)
input_direction.bind("<Right>", right_direction)
input_direction.bind("<Up>", right_direction)
input_direction.bind("<Down>", right_direction)

app.mainloop()

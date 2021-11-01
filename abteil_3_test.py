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
random_direction = random.choice(directions)
counter = 0


def update_label_directions(e):
    global random_direction
    global counter
    key_press = e.keysym
    print(key_press)
    while counter < 50:
        if key_press == label_direction["text"]:
            counter += 1
            print(counter)
            label_counter.config(
                text=f"Du hast {str(counter)} mal die richtige Richtung gedrückt."
            )
            label_direction.config(text=random.choice(directions))
        else:
            label_counter.config(text="Leider verloren!")
            label_direction.config(
                text="Du hast leider nicht richtig gedrückt.\nWillst du es nochmal versuchen?"
            )
    else:
        return


label_direction = Label(app, text=random_direction)
label_direction.pack(pady=20)

input_direction = Entry(app)
input_direction.pack(pady=20)

label_counter = Label(app, text="")
label_counter.pack()

input_direction.bind("<Left>", update_label_directions)
input_direction.bind("<Right>", update_label_directions)
input_direction.bind("<Up>", update_label_directions)
input_direction.bind("<Down>", update_label_directions)

app.mainloop()

"""
def counter():
    counter = 0
    while counter <= 50:
        counter += 1
        text_counter = f"Du hast {counter} mal die richtige Richtung gedrückt."
        label_counter.config(text=text_counter)
"""

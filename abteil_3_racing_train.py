from tkinter import *
from tkinter import messagebox
import abteil_constructor
from main_gui import *
import random
import time

directions = ["Left", "Right", "Up", "Down"]
entry_direction = Entry(app)


def racing_train(e):
    app.configure(background=theme[2]["abteil3_directions"])
    label_current.configure(font=font_texts_large)
    label_current.config(
        text=random.choice(directions),
        background=theme[2]["abteil3_directions"],
        fg=theme[1]["colors"]["abteil3_directions"],
        pady=30,
    )
    button_current_1.destroy()
    entry_direction.pack(pady=30)
    key_press = e.keysym

    if key_press == label_current["text"]:
        label_current.config(text=random.choice(directions))

    else:
        meldung = messagebox.askquestion(
            title="Leider verloren",
            message="Du hast leider nicht richtig gedrückt.\nWillst du es nochmal versuchen?",
        )
        if meldung == "no":
            label_current.config(
                text="Der Zug ist entgleist. Es gibt viele Tote und Verletzte..."
            )


entry_direction.bind("<Key>", racing_train)
"""
entry_direction.bind("<Left>", racing_train)
entry_direction.bind("<Right>", racing_train)
entry_direction.bind("<Up>", racing_train)
entry_direction.bind("<Down>", racing_train)
"""

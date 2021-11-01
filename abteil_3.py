from tkinter import *
from tkinter import messagebox
import abteil_constructor
from main_gui import *
import random
import time

directions = ["Left", "Right", "Up", "Down"]
entry_direction = Entry(app)
# entry_direction.pack()


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
    # entry_direction = Entry(app)
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


def streak_emergency():
    app.configure(background=theme[2]["abteil3_intro"])
    label_current.configure(font=font_texts_bold)
    text_emergency = """Der Lokführer kommt panisch auf dich zu gerannt und bittet um deine Hilfe.\n
    Durch die Kälte in den Bergen, ist die Bremse eingefroren...\n Der Lokführer kümmert sich schon darum,
    aber um den Zug auf den Schienen zu halten, musst du beim Lenken helfen.
    \n\nDrücke die Pfeiltasten in die angezeigte Richtung."""

    label_current.config(
        text=text_emergency,
        bg=theme[2]["abteil3_intro"],
        fg=theme[1]["colors"]["abteil3_intro"],
    )
    reassign_button(
        button_current_1,
        "Starten",
        theme[1]["colors"]["abteil3_buttons_intro"],
        abteil_constructor.abteil_3_obj.init_streak(2),
    )

    button_current_1.config(padx=400, height=2)
    button_current_2.destroy()

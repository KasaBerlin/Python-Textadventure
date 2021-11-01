from tkinter import *
from abteil_3 import racing_train
import abteil_constructor
from main_gui import *


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
        lambda: racing_train(2),
    )

    button_current_1.config(padx=400, height=2)
    button_current_2.destroy()

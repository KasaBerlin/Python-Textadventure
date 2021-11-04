from tkinter import messagebox
from main_gui import *
import random
import abteil_constructor

directions = ["Left", "Right", "Up", "Down"]
entry_direction = Entry(app)
label_counter = Label(app)

def racing_train_game(e):
    global entry_direction
    label_counter.config(
        text=f"Der Zug fährt {abteil_constructor.abteil_3_obj.geschwindigkeit} kmh."
    )
    abteil_constructor.abteil_3_obj.geschwindigkeit -= 7
    if abteil_constructor.abteil_3_obj.geschwindigkeit > 80:
        entry_direction.delete(0, END)
        if e.keysym == label_current["text"]:
            entry_direction.insert(0, e.keysym)
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
    else:
        label_current.config(text="Sehr gut. Der Zug fährt wieder normal")

def racing_train_starter():
    app.configure(background=bg["abteil3_directions"])
    entry_direction.pack(pady=30)
    label_counter.pack(pady=20)
    label_current.configure(font=font_texts_large)
    label_current.config(
        text=random.choice(directions),
        background=bg["abteil3_directions"],
        fg=color["abteil3_directions"],
        pady=30,
    )
    button_current_1.forget()


entry_direction.bind("<Left>", racing_train_game)
entry_direction.bind("<Right>", racing_train_game)
entry_direction.bind("<Up>", racing_train_game)
entry_direction.bind("<Down>", racing_train_game)


def streak_3_1():
    app.configure(background=bg["abteil3_intro"])
    label_current.configure(font=font_texts_bold)
    text_emergency = """Der Lokführer kommt panisch auf dich zu gerannt und bittet um deine Hilfe.\n
    Durch die Kälte in den Bergen, ist die Bremse eingefroren und der Zug fährt viel zu schnell.
    \n Der Lokführer kümmert sich schon darum, aber um den Zug auf den Schienen zu halten, musst du beim Lenken helfen.
    \n\nDrücke die Pfeiltasten in die angezeigte Richtung."""

    label_current.config(
        text=text_emergency,
        bg=bg["abteil3_intro"],
        fg=color["abteil3_intro"],
    )
    reassign_button(
        button_current_1,
        "Starten",
        color["abteil3_button_intro"],
        racing_train_starter
        # abteil_constructor.abteil_3_obj.init_streak(2),
    )
    button_current_1.config(padx=400, height=2)
    button_current_2.destroy()

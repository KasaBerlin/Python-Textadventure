from tkinter import messagebox
from main_gui import *
import random
import abteil_constructor

directions = ["Left", "Right", "Up", "Down"]
entry_direction = Entry(app)
label_speed = Label(app)


def racing_train_game(e):
    global entry_direction

    abteil_constructor.abteil_3_obj.geschwindigkeit -= 10
    if abteil_constructor.abteil_3_obj.geschwindigkeit > 100:
        label_speed.config(
            text=f"Der Zug fährt {abteil_constructor.abteil_3_obj.geschwindigkeit} kmh."
        )
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
                entry_direction.destroy
                label_speed.destroy
                reassign_button(button_current_1, "Beenden", app.destroy)
                button_current_1.grid(padx=60, row=3, column=2)
                button_current_1.config(height=2)

    else:
        current_image.configure(file="images/racing.png")
        label_current.config(text="Sehr gut. Der Zug fährt wieder normal")
        reassign_button(button_current_1, "Weiter", abteil_constructor.abteil_1_obj.init_streak(2))
        button_current_1.grid(padx=60, row=3, column=2)
        button_current_1.config(height=2)


def racing_train_starter():
    app.configure(background=bg["abteil3_racing"])
    entry_direction.grid(pady=30, row=2, column=2)
    label_speed.grid(
        pady=20,
        row=3,
        column=2,
    )
    label_speed.config(
        text=f"Der Zug fährt {abteil_constructor.abteil_3_obj.geschwindigkeit} kmh.",
        font=font_entry,
        bg=bg["abteil3_racing"],
    )
    label_current.configure(font=font_texts_large)
    label_current.config(
        text=random.choice(directions),
        background=bg["abteil3_racing"],
        fg=color["abteil3_racing"],
        pady=30,
    )
    button_current_1.grid_forget()


entry_direction.bind("<Left>", racing_train_game)
entry_direction.bind("<Right>", racing_train_game)
entry_direction.bind("<Up>", racing_train_game)
entry_direction.bind("<Down>", racing_train_game)


def streak_3_1():
    app.configure(background=bg["abteil3_intro"])
    current_image.configure(file="images/emergency.png")

    label_current.configure(font=font_texts)
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
        button_current_1, "Starten", racing_train_starter, color["abteil3_button_intro"]
    )
    button_current_1.grid(padx=60, row=3, column=2)
    button_current_1.config(width=20, height=2)
    button_current_2.destroy()

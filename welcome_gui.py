from tkinter import *
import random
from tkinter import font
from layout import theme
import abteil_constructor
from main_gui import *


def goodbye():
    app.configure(background=theme[2]["goodbye"])
    reassign_button(
        button_current_1,
        "Schließen",
        # theme[2]["goodbye_buttons"],
        theme[1]["colors"]["goodbye_buttons"],
        app.destroy,
    )
    button_current_1.config(padx=400, height=2)
    button_current_2.destroy()
    label_current.config(
        text="Schade...\nAuf Wiedersehen!",
        background=theme[2]["goodbye"],
        fg=theme[1]["colors"]["goodbye"],
    )
    current_image.configure(file="images/goodbye.png")


def streak_b():
    app.configure(background=theme[2]["exit"])
    text_streak_b = """Die beiden verlassen den Bahnhof.\n\nDu verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(
        text=text_streak_b,
        background=theme[2]["exit"],
        fg=theme[1]["colors"]["exit"],
        pady=56,
    )
    label_current.configure(font=font_texts)
    current_image.configure(file="images/exit.png")
    abteil_constructor.abteil_1_obj.inventar.clear()
    reassign_button(
        button_current_1,
        "Ja",
        # theme[2]["exit_buttons"],
        theme[1]["colors"]["exit_buttons"],
        welcome,
    )
    reassign_button(
        button_current_2,
        "Nein",
        # theme[2]["exit_buttons"],
        theme[1]["colors"]["exit_buttons"],
        goodbye,
    )


def welcome(e=None):
    app.configure(background=theme[2]["welcome"])
    urlaubsgeld = random.randrange(90, 110)
    abteil_constructor.abteil_1_obj.assign_inventar(urlaubsgeld)
    text_welcome = f"""Herzlichen Glueckwunsch!\n{entry_current.get()}, du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\n\nDeine Reise beginnt am Bahnsteig Nummer 12, wo du auf ein seltsames 
      Paar aufmerksam wirst.\nWas tust du?"""
    entry_current.forget()
    label_current.config(
        text=text_welcome,
        background=theme[2]["welcome"],
        fg=theme[1]["colors"]["welcome"],
        pady=0,
    )
    label_current.configure(font=font_gratulations)
    current_image.configure(file="images/welcome.png")

    reassign_button(
        button_current_1,
        "Beobachten",
        # theme[2]["welcome_buttons"],
        theme[1]["colors"]["welcome_buttons"],
        streak_b,
    )
    reassign_button(
        button_current_2,
        "Ignorieren",
        # theme[2]["welcome_buttons"],
        theme[1]["colors"]["welcome_buttons"],
        # lambda: abteil_constructor.abteil_1_obj.init_streak(1),
        lambda: abteil_constructor.abteil_3_obj.init_streak(1),
    )


entry_current.bind("<Return>", welcome)
app.mainloop()

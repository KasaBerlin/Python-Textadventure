import random
import abteil_constructor
from main_gui import *


def goodbye():
    app.configure(bg=bg["goodbye"])
    reassign_button(
        button_current_1,
        "Schließen",
        color["goodbye_button"],
        app.destroy,
    )
    button_current_1.config(padx=650, height=2)
    button_current_2.destroy()
    label_current.config(
        text="Schade...\nAuf Wiedersehen!",
        bg=bg["goodbye"],
        fg=color["goodbye"],
    )
    current_image.configure(file="images/goodbye.png")


def streak_b():
    app.configure(bg=bg["exit"])
    text_streak_b = """Die beiden verlassen den Bahnhof.\n\nDu verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(
        text=text_streak_b,
        bg=bg["exit"],
        fg=color["exit"],
        pady=83,
    )
    label_current.configure(font=font_texts)
    current_image.configure(file="images/exit.png")
    abteil_constructor.abteil_1_obj.inventar.clear()
    reassign_button(
        button_current_1,
        "Ja",
        color["exit_button"],
        welcome,
    )
    reassign_button(
        button_current_2,
        "Nein",
        color["exit_button"],
        goodbye,
    )


def welcome(e=None):
    app.configure(bg=bg["welcome"])
    urlaubsgeld = random.randrange(90, 110)
    abteil_constructor.abteil_1_obj.assign_inventar(urlaubsgeld)
    text_welcome = f"""Herzlichen Glueckwunsch!\n{entry_current.get()}, du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\n\nDeine Reise beginnt am Bahnsteig Nummer 12, wo du auf ein seltsames 
      Paar aufmerksam wirst.\nWas tust du?"""
    entry_current.forget()
    label_current.config(
        text=text_welcome,
        bg=bg["welcome"],
        fg=color["welcome"],
        pady=0,
    )
    label_current.configure(font=font_gratulations)
    current_image.configure(file="images/welcome.png")

    reassign_button(
        button_current_1,
        "Beobachten",
        color["welcome_button"],
        streak_b,
    )
    reassign_button(
        button_current_2,
        "Ignorieren",
        color["welcome_button"],
        lambda: abteil_constructor.abteil_1_obj.init_streak(1),
    )


entry_current.bind("<Return>", welcome)
app.mainloop()

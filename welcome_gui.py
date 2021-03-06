import random
import abteil_constructor
from main_gui import *


def goodbye():
    app.configure(bg=bg["goodbye"])
    reassign_button(
        button_current_1,
        "Schließen",
        app.destroy,
        color["goodbye_button"],
        columnGrid=2,
        padxGrid=60
    )

    button_current_2.grid_forget()
    label_current.config(
        text="Schade...\nAuf Wiedersehen!",
        bg=bg["goodbye"],
        fg=color["goodbye"]
    )
    current_image.configure(file="images/goodbye.png")


def paar_beobachten():
    app.configure(bg=bg["exit"])
    text_streak_b = """Die beiden verlassen den Bahnhof.\n\nDu verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(
        text=text_streak_b, bg=bg["exit"], fg=color["exit"], pady=60, font=font_texts
    )

    current_image.configure(file="images/exit.png")
    abteil_constructor.abteil_1_obj.inventar.clear()
    reassign_button(
        button_current_1,
        "Ja",
        welcome,
        color["exit_button"]
    )
    reassign_button(
        button_current_2,
        "Nein",
        goodbye,
        color["exit_button"]
    )


def zu_abteil_1():
    entry_username.destroy()
    abteil_constructor.abteil_1_obj.init_streak(1)


def welcome(e=None):
    # check ob wir schon Urlaubsgeld erhalten haben
    if not len(abteil_constructor.abteil_1_obj.inventar):
        urlaubsgeld = random.randrange(90, 110)
        abteil_constructor.abteil_1_obj.inventar.append(urlaubsgeld)
    app.configure(bg=bg["welcome"])
    text_welcome = f"""Herzlichen Glueckwunsch!\n{entry_username.get()}, du hast eine Zugfahrt im Bergland-Express im Radio-Quiz
      gewonnen! Du hast {abteil_constructor.abteil_1_obj.inventar[0]}DM Urlaubsgeld dabei!\n\nDeine Reise beginnt am Bahnsteig Nummer 12,
      wo du auf ein seltsames Paar aufmerksam wirst.\nWas tust du?"""
    entry_username.grid_forget()
    label_current.config(
        text=text_welcome,
        bg=bg["welcome"],
        fg=color["welcome"],
        pady=0,
        font=font_gratulations
    )
    current_image.configure(file="images/welcome.png")
    reassign_button(
        button_current_1,
        "Beobachten",
        paar_beobachten,
        color["welcome_button"]
    )
    reassign_button(
        button_current_2,
        "Ignorieren",
        zu_abteil_1,
        color["welcome_button"]
    )


entry_username.bind("<Return>", welcome)
app.mainloop()

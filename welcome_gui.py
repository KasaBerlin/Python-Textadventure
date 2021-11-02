import random
from layout import theme
import abteil_constructor
from main_gui import *

def goodbye():
    abteil_constructor.abteil_1_obj.inventar.clear()
    app.configure(background=theme[2]["goodbye"])
    reassign_button(
        button_current_1,
        "Schließen",
        theme[1]["color"]["goodbye_button"], 
        app.destroy,
    )
    button_current_1.config(height=2,padx=400)
    button_current_2.destroy()
    label_current.config(
        text="Schade...\nAuf Wiedersehen!",
        background=theme[2]["goodbye"],
        fg=theme[1]["color"]["goodbye"],
    )
    current_image.configure(file="images/goodbye.png")

def streak_b():
    app.configure(background=theme[2]["exit"])
    text_streak_b = """Die beiden verlassen den Bahnhof.\n\nDu verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(
        text=text_streak_b,
        background=theme[2]["exit"],
        fg=theme[1]["color"]["exit"],
        pady=83,
    )
    label_current.configure(font=font_texts)
    current_image.configure(file="images/exit.png")
    reassign_button(
        button_current_1,
        "Ja",
        theme[1]["color"]["exit_button"],
        welcome,
    )
    reassign_button(
        button_current_2,
        "Nein",
        theme[1]["color"]["exit_button"],
        goodbye,
    )

def welcome(e=None):
    # check ob wir schon Urlaubsgeld erhalten haben
    if not len(abteil_constructor.abteil_1_obj.inventar):
        urlaubsgeld = random.randrange(90, 110)
        abteil_constructor.abteil_1_obj.assign_inventar(urlaubsgeld)
    app.configure(background=theme[2]["welcome"])
    text_welcome = f"""Herzlichen Glückwunsch!\n{text_username.get()}, du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {abteil_constructor.abteil_1_obj.inventar[0]}DM Urlaubsgeld dabei!\n\nDeine Reise beginnt am Bahnsteig Nummer 12, wo dir ein seltsames 
      Paar auffällt.\nWas tust du?"""
    text_username.forget()
    label_current.config(
        text=text_welcome,
        background=theme[2]["welcome"],
        fg=theme[1]["color"]["welcome"],
        pady=0,
    )
    label_current.configure(font=font_gratulations)
    current_image.configure(file="images/welcome.png")

    reassign_button(
        button_current_1,
        "Beobachten",
        theme[1]["color"]["welcome_button"],
        streak_b,
    )
    reassign_button(
        button_current_2,
        "Ignorieren",
        theme[1]["color"]["welcome_button"],
        lambda: abteil_constructor.abteil_1_obj.init_streak(1),
    )


text_username.bind("<Return>", welcome)
app.mainloop()

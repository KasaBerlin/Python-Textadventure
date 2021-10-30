from tkinter import *
import random
from tkinter import font
from layout import theme
import abteil_constructor
from main_gui import *

app.configure(background=theme[2]["name"])

font_texts = font.Font(
    family=theme[1]["texts"]["family"], size=theme[1]["texts"]["size"]
)
font_gratulations = font.Font(
    family=theme[1]["gratulations"]["family"],
    size=theme[1]["gratulations"]["size"],
)
font_buttons = font.Font(
    family=theme[1]["buttons"]["family"],
    size=theme[1]["buttons"]["size"],
    weight=theme[1]["buttons"]["weight"],
)

label_current = Label(
    text="Bitte gib einen Usernamen ein", background=theme[2]["name_label"]
)
label_current.pack(pady=10)
label_current.configure(font=font_texts)

text_username = Entry(background=theme[2]["name_entry"])
text_username.pack()

button_current_1 = Button(background=theme[2]["welcome_buttons"])
button_current_2 = Button(background=theme[2]["welcome_buttons"])
# button_current_1.configure(font=font_buttons)
button_current_2.configure(font=font_buttons)

def goodbye():
    reassign_button(button_current_1, "Schließen", app.destroy)
    button_current_2.destroy()
    label_current.config(text="Schade! Auf Wiedersehen!")


def streak_b():
    text_streak_b = """Die beiden verlassen den Bahnhof. Du verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(text=text_streak_b)
    label_current.configure(font=font_texts)
    abteil_constructor.abteil_1_obj.inventar.clear()
    reassign_button(button_current_1, "Ja", welcome)
    reassign_button(button_current_2, "Nein", goodbye)


def welcome(e=None):
    urlaubsgeld = random.randrange(90, 110)
    abteil_constructor.abteil_1_obj.assign_inventar(urlaubsgeld)
    text_welcome = f"""Herzlichen Glückwunsch!\n{text_username.get()} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames 
      Paar auffällt.\nWas tust du?"""
    text_username.forget()
    label_current.config(text=text_welcome)
    reassign_button(button_current_1, "Beobachten", streak_b)
    reassign_button(
        button_current_2,
        "Ignorieren",
        lambda: abteil_constructor.abteil_1_obj.init_streak(1),
    )


text_username.bind("<Return>", welcome)
app.mainloop()


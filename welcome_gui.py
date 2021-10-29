from tkinter import *
import random
from abteil_1 import abteil_1
from tkinter import font
from layout import theme


# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry(
    "900x600+200+200"
)  # Breite 900, Höhe 600, x und y -Koordinate auf 200 und 200 setzen
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


def reassign_button(button, text, command):
    button["text"] = text
    button["command"] = command
    button.pack(fill="x")


def goodbye():
    reassign_button(button_current_1, "Schließen", app.destroy)
    button_current_2.destroy()
    label_current.config(text="Schade! Auf Wiedersehen!")


def streak_b():
    text_streak_b = """Die beiden verlassen den Bahnhof. Du verpasst deinen Zug und dein
    toller Gewinn verfällt...\nWillst du noch einmal von vorn beginnen?"""
    label_current.config(text=text_streak_b)
    label_current.configure(font=font_texts)
    abteil_1.inventar.clear()
    reassign_button(button_current_1, "Ja", welcome)
    reassign_button(button_current_2, "Nein", goodbye)


def welcome(e=None):
    urlaubsgeld = random.randrange(90, 110)
    abteil_1.assign_inventar(urlaubsgeld)
    text_welcome = f"""Herzlichen Glückwunsch!\n{text_username.get()} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames 
      Paar auffällt.\nWas tust du?"""
    label_current.configure(font=font_gratulations)
    app.configure(background=theme[2]["welcome"])
    text_username.forget()
    label_current.config(text=text_welcome, background=theme[2]["welcome_label"])
    reassign_button(button_current_1, "Beobachten", streak_b)
    reassign_button(button_current_2, "Ignorieren", lambda: abteil_1.init_streak(1))


text_username.bind("<Return>", welcome)

app.mainloop()


"""
buttonX = tk.Button(app, text="Fill X", bg="red", height=5)
buttonX.pack(fill='x')

buttonY = tk.Button(app, text="Fill Y", bg="green", width=10)
buttonY.pack(side='left', fill='y')
<<<<<<< HEAD
"""
# fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")

# textExample.configure(font=fontExample)

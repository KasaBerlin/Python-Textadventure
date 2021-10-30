from tkinter import *
from layout import theme
from tkinter import font
from tkmacosx import Button


# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry(
    "900x600+200+200"
)  # Breite 900, Höhe 600, x und y -Koordinate auf 200 und 200 setzen
app.configure(background=theme[2]["name"])

# FONTS anlegen
font_texts = font.Font(
    family=theme[1]["texts"]["family"], size=theme[1]["texts"]["size"]
)
font_gratulations = font.Font(
    family=theme[1]["gratulations"]["family"], size=theme[1]["gratulations"]["size"]
)
font_buttons = font.Font(
    family=theme[1]["buttons"]["family"],
    size=theme[1]["buttons"]["size"],
    weight=theme[1]["buttons"]["weight"],
)
font_thin = font.Font(family=theme[1]["thin"]["family"], size=theme[1]["thin"]["size"])

# Elemente anlegen
label_current = Label(
    app,
    text="Willkommen zum Abenteuer!\n\nBitte gib einen Usernamen ein:",
    background=theme[2]["name"],
    fg=theme[1]["colors"]["name_alternative"],
)
label_current.pack(pady=30)
label_current.configure(font=font_texts)

text_username = Entry(app, background=theme[2]["name_entry"])
text_username.pack(pady=30)

button_current_1 = Button(
    app, height=5, width=10, font=font_thin, bg=theme[2]["welcome_buttons"]
)
button_current_2 = Button(app, height=5, width=10, background="blue")


def reassign_button(button, text, fg, command):
    button["text"] = text
    button["fg"] = fg
    button["command"] = command
    button_current_1.pack(pady=10, padx=100, side=LEFT)
    button_current_2.pack(pady=10, padx=100, side=RIGHT)


# ! mainloop befindet sich in welcome_gui

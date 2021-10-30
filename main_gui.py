from tkinter import *
from layout import theme
from tkinter import font

# from tkmacosx import Button

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry(
    "1300x900+200+30"
)  # Breite x Höhe, x und y -Koordinate auf 200 und 200 setzen
icon = PhotoImage(file="images/feier_icon.gif")
app.call("wm", "iconphoto", app._w, icon)
app.configure(background=theme[2]["name"])

# FONTS anlegen
font_texts = font.Font(
    family=theme[1]["texts"]["family"], size=theme[1]["texts"]["size"]
)
font_gratulations = font.Font(
    family=theme[1]["gratulations"]["family"], size=theme[1]["gratulations"]["size"]
)
font_entry = font.Font(
    family=theme[1]["buttons"]["family"],
    size=theme[1]["buttons"]["size"],
    weight=theme[1]["buttons"]["weight"],
)
font_thin = font.Font(family=theme[1]["thin"]["family"], size=theme[1]["thin"]["size"])

# Bild einbinden
current_image = PhotoImage(file="images/feier.gif")
label_image = Label(image=current_image, borderwidth=0).pack(pady=30)

# Elemente anlegen
label_current = Label(
    app,
    text="Willkommen in einem Abenteuer!\n\nBitte gib zuerst einen Usernamen ein:",
    background=theme[2]["name"],
    fg=theme[1]["colors"]["name"],
)
label_current.pack(pady=20)
label_current.configure(font=font_texts)

text_username = Entry(
    app,
    bg=theme[2]["name_entry"],
    fg=theme[1]["colors"]["name_entry"],
    font=font_entry,
    borderwidth=0,
)
text_username.pack(padx=5, pady=10)

button_current_1 = Button(
    app,
    height=5,
    width=10,
    font=font_thin,
    # bg=theme[2]["welcome_buttons"],
    borderwidth=0,
)

button_current_2 = Button(
    app,
    height=5,
    width=10,
    font=font_thin,
    # bg=theme[2]["welcome_buttons"],
    borderwidth=0,
)


def reassign_button(button, text, fg, command):
    button["text"] = text
    # ? button["bg"] = bg
    button["fg"] = fg
    button["command"] = command
    button_current_1.pack(padx=250, side=LEFT)
    button_current_2.pack(padx=250, side=RIGHT)


# ! mainloop befindet sich in welcome_gui

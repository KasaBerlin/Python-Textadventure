from tkinter import font,PhotoImage,Label,Entry,Button,LEFT,RIGHT,Tk
from layout import theme
from collections import namedtuple

app,fonts,bg=theme
    
# from tkmacosx import Button

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry(
    "1300x900+200+30"
)  # Breite x Höhe, x und y -Koordinate auf 200 und 200 setzen
# TODO Vollbild?
# TODO grid/place buttons
app.configure(background=theme[2]["name"])
app.resizable(0, 0)

#
# ! ICON ???
#
# icon = PhotoImage(file="feier_icon.gif")
# app.call("wm", "iconphoto", app._w, icon)
# app.iconbitmap("feier_icon.icns")

# ! ICON - wird noch nicht angezeigt

normal=fonts["text"]
bold=fonts["text_bold"]
large=fonts["text_large"]
gratulations=fonts["gratulations"]
entry=fonts["entry"]
button=fonts["button"]
color=fonts["color"]

# FONTS anlegen
font_texts = font.Font(
    family=normal["family"], size=normal["size"]
)
font_texts_bold = font.Font(
    family=bold["family"],
    size=bold["size"],
    weight=bold["weight"],
)
font_texts_large = font.Font(
    family=large["family"], size=large["size"]
)
font_gratulations = font.Font(
    family=gratulations["family"], size=gratulations["size"]
)
font_entry = font.Font(
    family=entry["family"],
    size=entry["size"],
    weight=entry["weight"],
)
font_buttons = font.Font(
    family=button["family"], size=button["size"]
)

# Bild einbinden
current_image = PhotoImage(file="images/name.png")
label_image = Label(image=current_image, borderwidth=0).pack(pady=30)

# Elemente anlegen
label_current = Label(
    app,
    text="Willkommen in einem Abenteuer!\n\nBitte gib zuerst einen Usernamen ein:",
    background=bg["name"],
    fg=color["name"],
)
label_current.pack(pady=20)
label_current.configure(font=font_texts)

text_username = Entry(
    app,
    bg=bg["name_entry"],
    fg=color["name_entry"],
    font=font_entry,
    borderwidth=0,
)
text_username.pack(padx=5, pady=10)
# TODO text_username = entry_current
entry_current=Entry(app)

button_current_1 = Button(
    app,
    height=5,
    width=10,
    font=font_buttons,
    borderwidth=0,
)

button_current_2 = Button(
    app,
    height=5,
    width=10,
    font=font_buttons,
    borderwidth=0,
)

def forget_buttons():
    button_current_1.forget()
    button_current_2.forget()

def reassign_button(button, text, fg, command):
    button["text"] = text
    # ! button["bg"] = bg
    button["fg"] = fg
    button["command"] = command
    button.pack(padx=250, side=LEFT if button == button_current_1 else RIGHT)

# ! mainloop befindet sich in welcome_gui

from tkinter import font, PhotoImage, Label, Entry, Button, LEFT, RIGHT, END, Tk
from layout import theme


app, fonts, bg = theme
# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))
app.configure(background=bg["name"])
app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=200)

# TODO Icon einbinden
# ! ICON ???
#
# icon = PhotoImage(file="feier_icon.gif")
# app.call("wm", "iconphoto", app._w, icon)
# app.iconbitmap("feier_icon.icns")

# ! ICON - wird noch nicht angezeigt


normal = fonts["text"]
large = fonts["text_large"]
gratulations = fonts["gratulations"]
entry = fonts["entry"]
button = fonts["button"]
color = fonts["color"]

# FONTS anlegen
font_texts = font.Font(family=normal["family"], size=normal["size"])
font_texts_large = font.Font(family=large["family"], size=large["size"])
font_gratulations = font.Font(family=gratulations["family"], size=gratulations["size"])
font_entry = font.Font(
    family=entry["family"],
    size=entry["size"],
    weight=entry["weight"],
)
font_buttons = font.Font(family=button["family"], size=button["size"])

# Bild einbinden
current_image = PhotoImage(file="images/name.png")
label_image = Label(image=current_image, borderwidth=0).grid(
    pady=30, row=0, column=1, columnspan=3
)

# Elemente anlegen
label_current = Label(
    app,
    text="Willkommen in einem Abenteuer!\n\nBitte gib zuerst einen Usernamen ein:",
    background=bg["name"],
    fg=color["name"],
)
label_current.grid(pady=20, row=1, column=1, columnspan=3)
label_current.configure(font=font_texts)

entry_username = Entry(
    app,
    bg=bg["name_entry"],
    fg=color["name_entry"],
    font=font_entry,
    borderwidth=0,
)
entry_username.grid(padx=5, pady=10, row=2, column=1, columnspan=3)

entry_current = Entry(app)

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


def reassign_button(button, text, command, fg=None):
    button["text"] = text
    button["fg"] = fg
    button["command"] = command
    button.grid(row=3, column=1 if button == button_current_1 else 3)


def forget_buttons():
    button_current_1.grid_forget()
    button_current_2.grid_forget()


# TODO : responsive Schrift einbauen
""" def resize(e):
    height = label_current.winfo_height()
    width = label_current.winfo_width()
    height = height // 2
    print("height %s" % height)
    print("width %s" % width)
    if height < 10 or width < 200:
        height = 10
    elif width < 400 and height > 20:
        height = 20
    elif width < 600 and height > 30:
        height = 30
    else:
        height = 40
    print("height %s" % height)

    font_texts["size"] = height
    print(font_texts.actual())


app.bind("<Configure>", resize) """
# ! mainloop befindet sich in welcome_gui

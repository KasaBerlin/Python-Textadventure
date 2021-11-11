import json
from tkinter import font, PhotoImage, Label, Entry, Button, LEFT, RIGHT, END, Tk

with open("layout.json") as jsonFile:
    theme = json.load(jsonFile)
    jsonFile.close()

app, fonts, bg = theme.values()
# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))
app.configure(background=bg["name"])
app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=200)
# wm ruft windowmanager,iconPhoto method, windowName, image
app.tk.call("wm", "iconphoto", app._w, PhotoImage(file="images/favicon.gif"))

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
    pady=10, row=0, column=1, columnspan=3
)

# Elemente anlegen
label_current = Label(
    app,
    text="Willkommen in einem Abenteuer!\n\nBitte gib zuerst einen Usernamen ein:",
    bg=bg["name"],
    fg=color["name"],
)
label_current.grid(pady=10, padx=40, row=1, column=0, columnspan=5)
label_current.configure(font=font_texts)

entry_username = Entry(
    app,
    textvariable="",
    bg=bg["name_entry"],
    fg=color["name_entry"],
    font=font_entry,
    borderwidth=0,
)
entry_username.grid(padx=5, pady=10, row=2, column=1, columnspan=3)
entry_username.focus()

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


def reassign_button(
    button,
    text,
    command,
    fg=None,
    columnGrid=None,
    padxGrid=None,
    width=None,
    height=None,
):
    button.config(text=text, fg=fg, command=command, width=width, height=height)
    if button == button_current_1 and not columnGrid:
        column = 1
    elif button == button_current_2:
        column = 3
    else:
        column = columnGrid
    button.grid(row=3, column=column, padx=padxGrid)


def forget_buttons():
    button_current_1.grid_forget()
    button_current_2.grid_forget()


# TODO : responsive Schrift einbauen
def resize(e):
    width = app.winfo_width()
    height_font_labels = 30
    height_font_buttons = 18
    height_font_large = 44
    print("width %s" % width)
    if width <= 500:
        height_font_labels -= 10
        height_font_buttons -= 5
        height_font_large -= 14
        app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=50)
        app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
    elif width <= 900:
        height_font_labels -= 6
        height_font_buttons -= 3
        height_font_large -= 8
        app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
        app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=150)
    elif width <= 1200:
        height_font_labels = 30
        height_font_buttons = 18
        height_font_large = 44
        app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
        app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=200)
    else:
        height_font_labels += 4
        height_font_buttons += 2
        height_font_large += 4
        app.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=100)
        app.columnconfigure([0, 1, 2, 3, 4], weight=1, minsize=240)

    font_texts["size"] = height_font_labels
    font_gratulations["size"] = height_font_labels
    font_buttons["size"] = height_font_buttons
    font_entry["size"] = height_font_buttons
    font_texts_large["size"] = height_font_large
    # print(font_texts.actual())
    # print(font_buttons.actual())


app.bind("<Configure>", resize)
# ! mainloop befindet sich in welcome_gui

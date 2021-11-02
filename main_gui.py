from tkinter import *

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry(
    "800x600+200+200"
)  # Breite 400, Höhe 300, x und y -Koordinate auf 300 und 200 setzen

label_current = Label(app, text="Bitte gib einen Usernamen ein")
label_current.pack(pady=10)

text_username = Entry(app)
text_username.pack()

# TODO text_username = entry_current
entry_current=Entry(app)

button_current_1 = Button(app)
button_current_2 = Button(app)

def forget_buttons():
    button_current_1.forget()
    button_current_2.forget()

def reassign_button(button, text, command):
    button["text"] = text
    button["command"] = command
    button.pack(fill="x")


# ! mainloop befindet sich in welcome_gui

from tkinter import *
import random
from abteil_1 import abteil_1
from tkinter import font
import layout


# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry("900x600+200+200")

font_ex = font.Font(family="Aller", size=26, weight="normal")

label_current = Label(text="Bitte gibt einen Usernamen ein")
label_current.pack(pady=10)

current_entry = Entry()


# def streak_b():
#     final_action = input(
#         """Die beiden verlassen den Bahnhof. Du verpasst deinen Zug und dein
#     toller Gewinn verfällt... Willst du noch einmal von vorn beginnen? (Y)es or (N)o"""
#     )
#     print()
#     abteil_1.inventar.clear()
#     if final_action.upper() == "Y":
#         welcome()
#     else:
#         print()
#         print("Schade! Auf Wiedersehen!")


def welcome(e):
    urlaubsgeld = random.randrange(90, 110)
    abteil_1.assign_inventar(urlaubsgeld)
    text1 = f"""Herzlichen Glückwunsch!\n{text_username.get()} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames 
      Paar auffällt.\n Was tust du?"""
    text_username.pack_forget()

    label_current.configure(font=font_ex)
    label_current.config(text=text1)

    button_beobachten = Button(text="Beobachten")
    button_beobachten.pack()
    button_ignorieren = Button(text="Ignorieren")
    button_ignorieren.pack()
    # if action_1.upper() == "B":
    #     streak_b()
    # elif action_1.upper() == "I":
    #     abteil_1.init_streak(1)


text_username = Entry()
text_username.pack()
text_username.bind("<Return>", welcome)

"""
buttonX = tk.Button(app, text="Fill X", bg="red", height=5)
buttonX.pack(fill='x')

buttonY = tk.Button(app, text="Fill Y", bg="green", width=10)
buttonY.pack(side='left', fill='y')
"""


app.mainloop()

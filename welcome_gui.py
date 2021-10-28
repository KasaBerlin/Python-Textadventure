from tkinter import *
import random
from abteil_1 import abteil_1

# tkinter-window mit Titel und Größe erzeugen
app = Tk()
app.title("Reise im Bergland-Express")
app.geometry("800x600+200+200")
frame = Frame(bd=3, relief="raised")

label_current = Label(frame, text="Bitte gibt einen Usernamen ein")
label_current.pack(pady=10)

text_username = Entry(frame)
text_username.pack()
text_username.bind('<Return>', welcome)

current_entry=Entry(frame)


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
    text1=f"""Herzlichen Glückwunsch!\n{text_username.get()} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames 
      Paar auffällt. Was tust du?"""
    text_username.forget_pack()
    label_current.config(text=text1)
    button_beobachten = Button(frame,text="Beobachten")
    button_beobachten.pack()
    button_ignorieren = Button(frame,text="Ignorieren")
    button_ignorieren.pack()
    # if action_1.upper() == "B":
    #     streak_b()
    # elif action_1.upper() == "I":
    #     abteil_1.init_streak(1)

welcome()

"""
buttonX = tk.Button(app, text="Fill X", bg="red", height=5)
buttonX.pack(fill='x')

buttonY = tk.Button(app, text="Fill Y", bg="green", width=10)
buttonY.pack(side='left', fill='y')
"""


frame.pack(pady=10)
app.mainloop()
from tkinter import *
import random
import abteil_constructor
from main_gui import *

def goodbye():
  reassign_button(button_current_1,"Schließen",app.destroy)
  button_current_2.destroy()
  label_current.config(text="Schade! Auf Wiedersehen!")

def streak_b():
    text_streak_b = """Die beiden verlassen den Bahnhof. Du verpasst deinen Zug und dein
    toller Gewinn verfällt... Willst du noch einmal von vorn beginnen?"""
    label_current.config(text=text_streak_b)
    abteil_constructor.abteil_1_obj.inventar.clear()
    reassign_button(button_current_1,"Ja",welcome)
    reassign_button(button_current_2,"Nein",goodbye)

def welcome(e=None):
    urlaubsgeld = random.randrange(90, 110)
    abteil_constructor.abteil_1_obj.assign_inventar(urlaubsgeld)
    text_welcome=f"""Herzlichen Glückwunsch!\n{text_username.get()} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz 
      gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames 
      Paar auffällt. Was tust du?"""
    text_username.forget()
    label_current.config(text=text_welcome)
    reassign_button(button_current_1,"Beobachten",streak_b)
    reassign_button(button_current_2,"Ignorieren",lambda:abteil_constructor.abteil_1_obj.init_streak(1))

text_username.bind('<Return>', welcome)
app.mainloop()
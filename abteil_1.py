import math
import abteil_constructor
from main_gui import *
from tkinter import IntVar,END

guess_entry = IntVar()
guesses_made = 0

def zu_abteil_4():
    reassign_button(
        button_current_1,
        "Ok",
        lambda: abteil_constructor.abteil_4_obj.init_streak(1),
        button_current_1.config(padx=650, height=2)
    )

def kein_leckerli():
   label_current.config(text="Du MONSTER!!! Du wirst ins Abteil 4 verbannt!",bg=bg["abteil1_monster"])
   zu_abteil_4() 
   
def leckerli():
    abteil_constructor.abteil_1_obj.inventar.remove("Leckerli")
    label_current.config(text=f"""Der Mops freut sich und schlappert 
    dir als Dank die Hand ab! Weiter gehts im Abteil 4!""",  bg=bg["abteil1_leckerli"]) 
    zu_abteil_4() 


def dog_quiz(e):
    # wenn guess_entry value "" ist, assign  0 to guess_entry
    try:guess_entry.get()
    except:guess_entry.set(0)

    key_age_dog = 64
    dog_year_converter = int((math.log(16) * guess_entry.get()) + 31)
    
    global guesses_made
    guesses_made += 1

    if guesses_made < 6:  
        if  key_age_dog < dog_year_converter:
            guess_entry.set(0)
            entry_current.delete(0, END)
            label_current.config(text='Dein Tipp war zu hoch.')
        elif key_age_dog > dog_year_converter:
            guess_entry.set(0)
            entry_current.delete(0, END)
            label_current.config(text='Dein Tipp war zu niedrig.')
        elif dog_year_converter == key_age_dog:
            entry_current.destroy()
            label_current.config(text=f"Richtig! Du hast nach {guesses_made} Tipps das Alter erraten!\nDafür erhälst du ein Leckerli in deinem Inventar! Möchtest du dein Leckerli dem Mops geben?")
            abteil_constructor.abteil_1_obj.inventar.append("Leckerli")
            print(abteil_constructor.abteil_1_obj.inventar)
            reassign_button(button_current_1, "Ja", leckerli)
            reassign_button(button_current_2, "Nein", kein_leckerli)
    if guesses_made == 6 and dog_year_converter != key_age_dog: 
            label_current.config(text=f"""Leider nicht richtig geraten.\nDas Alter des Hundes ist {key_age_dog} Jahre alt in Menschenalter.\nWeiter gehts im Abteil 4!""")  
            zu_abteil_4() 
    
    

def streak_b():
    app.configure(bg=bg["abteil1_speisewagen"])
    forget_buttons()
    label_current.config(text="""Du findest einen Platz im Speisewagen und studierst die Karte - 
    du brauchst erstmal was zur Beruhigung.\nWas möchtest du bestellen?""",bg=bg["abteil1_speisewagen"],fg=color["abteil1_speisewagen"])
    abteil_constructor.abteil_2_obj.init_streak(1)


def streak_h(intro=False):
    if intro:
        label_current.config(
            text="""Sie antwortet freundlich das er noch recht rüstig ist für sein Alter 
        und gibt ihm ein Leckerli.\nSie fragt dich, ob du sein Alter erraten kannst? Gib einen Tipp ab:""",
        )
    forget_buttons()
    entry_current.grid(padx=5, pady=10, row=2, column=1, columnspan=3)
    entry_current.config(textvariable=guess_entry,bg=bg["abteil1_entry_intro"])

def streak_i():
    app.configure(bg=bg["abteil1_intro"])

    label_current.config(
        text="""Im Zug lässt du dich auf deinem Sitzplatz nieder und schaust dich um.\nDie Sitze sind mit dunkelrotem Samt
    bezogen und die Wände mit dunklem Holz verkleidet.\nDer 20er Jahre Stil ist genau nach deinem Geschmack.
    \nEine nette alte Dame setzt sich mit ihrem alten röchelden Mops neben dich und lächelt dich an.\nWas tust du?""",
        font=font_texts,
        bg=bg["abteil1_intro"],
        fg=color["abteil1_intro"],
    )
    reassign_button(
        button_current_1,
        "Du verlässt genervt deinen Platz.\nDas röcheln hälst du nicht aus.\nDu streifst durch den Zug.",
        streak_b,
        color["abteil1_button_intro"],
    )
    reassign_button(
        button_current_2,
        "Du sprichst die Dame auf das Alter ihres Hundes an\nund streichelst ihn über den Kopf.",
        lambda: streak_h(intro=True),
        color["abteil1_button_intro"],
    )
    button_current_1.config(width=50)
    button_current_2.config(width=50)


entry_current.bind("<Return>", dog_quiz)

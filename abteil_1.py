import math
import abteil_constructor
from main_gui import *

guessEntry = IntVar()
guesses_made = 0

def kein_leckerli():
   label_current.config(text="Du MONSTER!!!") 

def leckerli():
    abteil_constructor.abteil_1_obj.inventar.remove("Leckerli")
    label_current.config(text=f"Der Mops freut sich und schlappert dir als Dank die Hand ab!") 
    print(abteil_constructor.abteil_1_obj.inventar)

def dog_quiz(e):
    key_age_dog = 64
    guess = guessEntry.get() 
    dog_year_converter = int((math.log(16) * guess) + 31)
    global guesses_made
    guesses_made += 1
    while guesses_made < 6: 
        print(guesses_made)   
        if  key_age_dog < dog_year_converter:
            entry_current.clear()
            label_current.config(text='Dein Tipp war zu hoch.')

        elif key_age_dog > dog_year_converter:
            entry_current.clear()
            label_current.config(text='Dein Tipp war zu niedrig.')

        elif dog_year_converter == key_age_dog:
            break    
    if dog_year_converter == key_age_dog:
        entry_current.destroy()
        label_current.config(text=f"Richtig! Du hast nach {guesses_made} Tipps das Alter erraten!\nDafür erhälst du ein Leckerli in deinem Inventar! Möchtest du dein Leckerli dem Mops geben?")
        abteil_constructor.abteil_1_obj.inventar.append("Leckerli")
        print(abteil_constructor.abteil_1_obj.inventar)
        reassign_button(button_current_1, "Ja", leckerli)
        reassign_button(button_current_2, "Nein", kein_leckerli)
    else:
        label_current.config(text=f'Leider nicht richtig geraten. Das Alter des Hundes ist {key_age_dog} Jahre alt in Menschenalter.')
    

def streak_b():
    label_current.config(text="""Du findest einen Platz im Speisewagen und studierst die Getränkekarte - 
    du brauchst erstmal was zur Beruhigung. Gib einen Tipp ab:""")
    abteil_constructor.abteil_2_obj.assign_inventar(abteil_constructor.abteil_1_obj.inventar)
    abteil_constructor.abteil_2_obj.init_streak(1)

def streak_h():
    forget_buttons()
    label_current.config(text="""Sie antwortet freundlich das er noch recht rüstig ist für sein Alter 
    und gibt ihm ein Leckerli.\nSie fragt dich, ob du sein Alter erraten kannst? Gib einen Tipp ab:""")
    entry_current.pack()
    entry_current.config(textvariable=guessEntry)

def streak_i():
    label_current.config(text="""Im Zug lässt du dich auf deinem Sitzplatz nieder und schaust dich um.\nDie Sitze sind mit dunkelrotem Samt
    bezogen und die Wände mit dunklem Holz verkleidet.\nDer 20er Jahre Stil ist genau nach deinem Geschmack.
    \nEine nette alte Dame setzt sich mit ihrem alten röchelden Mops neben dich und lächelt dich an. Was tust du?""")
    reassign_button(
    button_current_1, 
    "Du verlässt genervt deinen Platz. Das röcheln hälst du nicht aus. Du streifst durch den Zug.", 
    streak_b)
    reassign_button(
    button_current_2,
    "Du sprichst die Dame auf das Alter ihres Hundes an und streichelst ihn über den Kopf.",
    streak_h,
    )

entry_current.bind("<Return>", dog_quiz)

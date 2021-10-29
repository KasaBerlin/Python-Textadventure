import math
import abteil_constructor
from main_gui import *

def dog_quiz():
    guesses_made = 0
    key_age_dog = 64
    
    while guesses_made < 6:

        guess = int(input("Gib einen Tipp ab: "))
        dog_year_converter = int((math.log(16) * guess) + 31)

        guesses_made += 1
        if  key_age_dog < dog_year_converter:
            print ('Dein Tipp war zu hoch.')

        elif key_age_dog > dog_year_converter:
            print ('Dein Tipp war zu niedrig.')

        elif dog_year_converter == key_age_dog:
            break    
    if dog_year_converter == key_age_dog:
        print (f"Richtig! Du hast nach {guesses_made} Tipps das Alter erraten!\nDafür erhälst du ein Leckerli in deinem Inventar!")
        abteil_constructor.abteil_1_obj.inventar.append("Leckerli")
        print(abteil_constructor.abteil_1_obj.inventar)
        if input("Möchtest du dein Leckerli dem Mops geben? ja(y) oder nein(n)") == "y" :
             abteil_constructor.abteil_1_obj.inventar.remove("Leckerli")
             print("Der Mops freut sich und schlappert dir als Dank die Hand ab!")
             print(abteil_constructor.abteil_1_obj.inventar)             
        else:
             print (f'Leider nicht richtig geraten. Das Alter des Hundes ist {key_age_dog} Jahre alt in Menschenalter.')

def streak_i():
    text_streak_i="""Im Zug lässt du dich auf deinem Sitzplatz nieder und schaust dich um.\nDie Sitze sind mit dunkelrotem Samt
    bezogen und die Wände mit dunklem Holz verkleidet.\nDer 20er Jahre Stil ist genau nach deinem Geschmack.
    \nEine nette alte Dame setzt sich mit ihrem alten röchelden Mops neben dich und lächelt dich an."""
    label_current.config(text=text_streak_i)
    # action_1=input("""Was tust du? Du verlässt genervt deinen Platz. Das röcheln hälst du nicht aus.
    # Du streifst durch den (Z)ug.\nDu sprichst die Dame auf das Alter
    # ihres (H)undes an und streichelst ihn über den Kopf.""")
    # if action_1.upper() == "Z":
    #     print("Du findest einen Platz im Speisewagen und studierst die Getränkekarte - du brauchst erstmal was zur Beruhigung.")
    #     abteil_2.abteil_2.assign_inventar(abteil_constructor.abteil_1_obj.inventar)
    #     abteil_2.abteil_2.init_streak(1)
    # elif action_1.upper() == "H":
    #     print("""Sie antwortet freundlich das er noch recht rüstig ist für sein Alter
    #     und gibt ihm ein Leckerli.\nSie fragt dich, ob du sein Alter erraten kannst?""")
    #     dog_quiz()
        

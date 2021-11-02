import abteil_constructor
from main_gui import *
from tkinter import ttk

def streak_1():
    speisekarte = {
        "Getränke": {
            "Whiskey 4cl": 8,
            "Bier 0.5ml": 4,
            "Milch 300ml": 3,
            "Tasse Kaffee": 5,
            "Tasse Tee-verschiedene Sorten": 4,
        },
        "Speisen": {"Kuchen des Tages": 10, "Eisbein": 15, "Suppe des Tages": 10},
    }
    getraenke= ttk.Combobox(app, values = list(speisekarte["Getränke"].keys()))
    getraenke.set("wähle aus")
    getraenke.pack()
    speisen=ttk.Combobox(app, values = list(speisekarte["Speisen"].keys()))
    speisen.set("wähle aus")
    speisen.pack()
    # for item in speisekarte:
    #     for i in speisekarte[item].keys():
    #         if i.find(f"({auswahl})") != -1:
    #             abteil_constructor.abteil_2_obj.inventar[0] -= speisekarte[item][i]
    #             print(f"Du hast jetzt noch {abteil_constructor.abteil_2_obj.inventar[0]} DM im Inventar.")
    #             if (
    #                 input(
    #                     "Der Kellner fragt dich, ob du noch etwas bestellen möchtest? (J)a oder (N)ein"
    #                 ).upper()
    #                 == "J"
    #             ):
    #                 streak_1()
    #             else:
    #                 print(
    #                     "Du kehst zu deinem Platz zurück. Die Alte Lady mit dem Mops lächelt dich nett an und fragt dich, ob du sein wahres Alter erraten kannst."
    #                 )
    #                 abteil_constructor.abteil_1_obj.dog_quiz()

import abteil_constructor
from main_gui import *
from tkinter import ttk,StringVar

speisekarte = {
        "Getraenke": {
            "Whiskey 4cl": 8,
            "Bier 0.5ml": 4,
            "Milch 300ml": 3,
            "Tasse Kaffee": 5,
            "Tasse Tee-verschiedene Sorten": 4,
        },
        "Speisen": {
            "Kuchen des Tages": 10, 
            "Eisbein": 15, 
            "Suppe des Tages": 10},
    }

getraenke_auswahl=StringVar()
speisen_auswahl=StringVar()

label_getraenke= Label(app, text="Getraenke")
label_speisen= Label(app, text="Speisen")

getraenke= ttk.Combobox(app, values = list(speisekarte["Getraenke"].keys()),textvariable=getraenke_auswahl)
getraenke.set("wähle aus")

speisen=ttk.Combobox(app, values = list(speisekarte["Speisen"].keys()),textvariable=speisen_auswahl)
speisen.set("wähle aus")

def zu_abteil_1():
    label_getraenke.destroy()
    label_speisen.destroy()
    getraenke.destroy()
    speisen.destroy()
    label_current.config(text="""Du kehst zu deinem Platz zurück. Die Alte Lady mit dem Mops lächelt dich 
    nett an und fragt dich, ob du sein wahres Alter erraten kannst.""")
    abteil_constructor.abteil_1_obj.init_streak(2)

def auswahlcheck(speisen_auswahl,getraenke_auswahl):
    check1=speisekarte["Getraenke"][getraenke_auswahl.get()] if getraenke_auswahl.get() in speisekarte["Getraenke"].keys() else 0 
    check2=speisekarte["Speisen"][speisen_auswahl.get()] if speisen_auswahl.get() in speisekarte["Speisen"].keys() else 0 
    return check1+check2

def bestellen(e):
    bezahlung=abteil_constructor.abteil_1_obj.inventar[0] - auswahlcheck(speisen_auswahl,getraenke_auswahl)
    if bezahlung > 0:
        abteil_constructor.abteil_1_obj.inventar[0] = bezahlung
        label_current.config(text=f"""Du hast jetzt noch {abteil_constructor.abteil_1_obj.inventar[0]} DM im Inventar.\n 
        Der Kellner fragt dich, ob du noch etwas bestellen möchtest?""")
        reassign_button(button_current_1, "Ja", streak_1)
        reassign_button(button_current_2, "Nein", zu_abteil_1)
    else:
        label_current.config(text="""Leider hast du nicht mehr genug Geld. Du gehts zurück ins Abteil 1.""")
        forget_buttons()
        reassign_button(
        button_current_1,
        "Ok",
        zu_abteil_1,
        button_current_1.config(padx=650, height=2)
    )
    
def streak_1():
    forget_buttons()
    label_getraenke.pack(pady=10)
    getraenke.pack()
    label_speisen.pack(pady=10)
    speisen.pack()

getraenke.bind('<Return>', bestellen)
speisen.bind('<Return>', bestellen)
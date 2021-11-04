import abteil_constructor
from main_gui import *
from tkinter import ttk, StringVar

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

speisen = ttk.Combobox(
    app, values=list(speisekarte["Speisen"].keys()), textvariable=speisen_auswahl
)
speisen.set("wähle aus")

def zu_abteil_1():
    label_getraenke.destroy()
    label_speisen.destroy()
    getraenke.destroy()
    speisen.destroy()
    abteil_constructor.abteil_1_obj.init_streak(2,2)

def auswahlcheck(speisen_auswahl,getraenke_auswahl):
    check1=speisekarte["Getraenke"][getraenke_auswahl.get()] if getraenke_auswahl.get() in speisekarte["Getraenke"].keys() else 0 
    check2=speisekarte["Speisen"][speisen_auswahl.get()] if speisen_auswahl.get() in speisekarte["Speisen"].keys() else 0 
    return check1+check2
    
def streak_2_1():
    # TODO app.configure key Umbenennung
    app.configure(bg=bg["abteil1_speisewagen"])
    label_current.config(text="""Du findest einen Platz im Speisewagen und studierst die Karte - 
    du brauchst erstmal was zur Beruhigung.\nWas möchtest du bestellen?""",bg=bg["abteil1_speisewagen"],fg=color["abteil1_speisewagen"])
    label_getraenke.grid(pady=10, row=2, column=1, sticky="ne")
    label_getraenke.config(
        font=font_texts, bg=bg["abteil1_speisewagen"], fg=color["abteil1_speisewagen"]
    )
    getraenke.grid(pady=10, row=2, column=1, sticky="e")
    label_speisen.grid(pady=10, row=2, column=3, sticky="nw")
    label_speisen.config(
        font=font_texts, bg=bg["abteil1_speisewagen"], fg=color["abteil1_speisewagen"]
    )
    speisen.grid(pady=10, row=2, column=3, sticky="w")

def bestellen(e):
    bezahlung=abteil_constructor.abteil_1_obj.inventar[0] - auswahlcheck(speisen_auswahl,getraenke_auswahl)
    if bezahlung > 0:
        abteil_constructor.abteil_1_obj.inventar[0] = bezahlung
        label_current.config(text=f"""Du hast jetzt noch {abteil_constructor.abteil_1_obj.inventar[0]} DM im Inventar.\n 
        Der Kellner fragt dich, ob du noch etwas bestellen möchtest?""")
        reassign_button(button_current_1, "Ja", streak_2_1)
        reassign_button(button_current_2, "Nein", zu_abteil_1)
        button_current_1.config(width=10)
        button_current_2.config(width=10)
    else:
        label_current.config(text="""Leider hast du nicht mehr genug Geld. Du gehts zurück ins Abteil 1.""")
        forget_buttons()
        reassign_button(
        button_current_1,
        "Ok",
        zu_abteil_1,
        button_current_1.config(padx=650, height=2)
    )
    

getraenke.bind('<Return>', bestellen)
speisen.bind('<Return>', bestellen)

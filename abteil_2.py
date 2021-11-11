import abteil_constructor
from main_gui import *
from tkinter import StringVar, Listbox

speisekarte = {
    "Getraenke": {
        "Whiskey 4cl:": 8,
        "Bier 0.5ml:": 4,
        "Milch 300ml:": 3,
        "Tasse Kaffee:": 5,
        "Tasse Tee:": 4
    },
    "Speisen": {"Kuchen des Tages:": 10, "Eisbein:": 15, "Suppe des Tages:": 10}
}


list_getraenke = Listbox(
    app,
    exportselection=0,
    height=5,
    font=font_entry,
    fg=color["abteil2_list"],
    bg=bg["abteil2_list"]
)

for getraenk in speisekarte["Getraenke"]:
    list_getraenke.insert(END, getraenk)

list_speisen = Listbox(
    app,
    exportselection=0,
    height=3,
    font=font_entry,
    fg=color["abteil2_list"],
    bg=bg["abteil2_list"]
)
for speise in speisekarte["Speisen"]:
    # TODO: Preise in der Speisekarte ergänzen
    list_speisen.insert(END, "{}".format(speise, speisekarte["Speisen"][speise]))


label_getraenke = Label(app, text="Getränke")
label_speisen = Label(app, text="Speisen")


def zu_abteil_1_oder_abteil_3():
    label_getraenke.destroy()
    label_speisen.destroy()
    list_getraenke.destroy()
    list_speisen.destroy()
    label_current.config(
        text="\nDu kannst zurück ins Abteil 1 oder weiter zu Abteil 3."
    )

    reassign_button(
        button_current_1,
        "Abteil 1",
        lambda: abteil_constructor.abteil_1_obj.init_streak(2, 2),
        width=10,
        height=5
    )
    reassign_button(
        button_current_2,
        "Abteil 3",
        lambda: abteil_constructor.abteil_3_obj.init_streak(1),
        width=10
    )


def auswahlcheck():
    selection_getraenk = list_getraenke.curselection()
    print(selection_getraenk)
    value_getraenk = list_getraenke.get(selection_getraenk[0])
    print(value_getraenk)

    check1 = (
        speisekarte["Getraenke"][value_getraenk]
        if list_getraenke.get(list_getraenke.curselection())
        in speisekarte["Getraenke"].keys()
        else 0
    )
    selection_speise = list_speisen.curselection()
    print(selection_speise)
    value_speise = list_speisen.get(selection_speise[0])
    print(value_speise)
    check2 = (
        speisekarte["Speisen"][value_speise]
        if list_speisen.get(list_speisen.curselection())
        in speisekarte["Speisen"].keys()
        else 0
    )
    return check1 + check2


def streak_2_1():
    app.configure(bg=bg["abteil2_speisewagen"])
    current_image.configure(file="images/speisewagen.png")

    label_current.config(
        text="""Du findest einen Platz im Speisewagen und studierst die Karte -
    du brauchst erstmal was zur Beruhigung.\nWas möchtest du bestellen?""",
        bg=bg["abteil2_speisewagen"],
        fg=color["abteil2_speisewagen"]
    )
    label_getraenke.grid(pady=10, row=2, column=1, sticky="ne")
    label_getraenke.config(
        font=font_texts, bg=bg["abteil2_speisewagen"], fg=color["abteil2_speisewagen"]
    )
    list_getraenke.grid(pady=10, row=2, column=1, sticky="se")
    label_speisen.grid(pady=10, row=2, column=3, sticky="nw")
    label_speisen.config(
        font=font_texts, bg=bg["abteil2_speisewagen"], fg=color["abteil2_speisewagen"]
    )
    list_speisen.grid(pady=10, row=2, column=3, sticky="sw")


def bestellen(e):
    bezahlung = abteil_constructor.abteil_1_obj.inventar[0] - auswahlcheck()
    if bezahlung > 0:
        abteil_constructor.abteil_1_obj.inventar[0] = bezahlung
        label_current.config(
            text=f"""Du hast jetzt noch {abteil_constructor.abteil_1_obj.inventar[0]} DM im Inventar.\n
        Der Kellner fragt dich, ob du noch etwas bestellen möchtest?"""
        )
        reassign_button(button_current_1, "Ja", streak_2_1, width=10)
        reassign_button(button_current_2, "Nein", zu_abteil_1_oder_abteil_3, width=10)

    else:
        label_current.config(text="""Leider hast du nicht mehr genug Geld.""")
        forget_buttons()
        reassign_button(
            button_current_1,
            "Ok",
            zu_abteil_1_oder_abteil_3,
            columnGrid=2,
            padxGrid=60,
            height=2,
            width=20
        )


list_getraenke.bind("<Return>", bestellen)
list_speisen.bind("<Return>", bestellen)

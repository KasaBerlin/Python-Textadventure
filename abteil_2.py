import abteil_constructor

def streak_1():
    speisekarte = {
        "Getränke": {
            "(W)hiskey 4cl": 8,
            "(B)ier 0.5ml": 4,
            "(M)ilch 300ml": 3,
            "Tasse (KA)ffee": 5,
            "Tasse (T)ee-verschiedene Sorten": 4,
        },
        "Speisen": {"(KU)chen des Tages": 10, "(E)isbein": 15, "(S)uppe des Tages": 10},
    }
    print(speisekarte)
    auswahl = input("Wähle aus!").upper()
    for item in speisekarte:
        for i in speisekarte[item].keys():
            if i.find(f"({auswahl})") != -1:
                abteil_constructor.abteil_2_obj.inventar[0] -= speisekarte[item][i]
                print(f"Du hast jetzt noch {abteil_constructor.abteil_2_obj.inventar[0]} DM im Inventar.")
                if (
                    input(
                        "Der Kellner fragt dich, ob du noch etwas bestellen möchtest? (J)a oder (N)ein"
                    ).upper()
                    == "J"
                ):
                    streak_1()
                else:
                    print(
                        "Du kehst zu deinem Platz zurück. Die Alte Lady mit dem Mops lächelt dich nett an und fragt dich, ob du sein wahres Alter erraten kannst."
                    )
                    abteil_constructor.abteil_1_obj.dog_quiz()

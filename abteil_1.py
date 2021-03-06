import math
import abteil_constructor
from main_gui import *
from tkinter import IntVar, END

guess_entry = IntVar()
guesses_made = 0

katze = """Auf einmal mauzt dich irgendetwas von der Seite an.\nEhe du sie steicheln kannst,
sieht du schon, wie ein Katzenschwanz im nächsten Abteil verschwindet.\n\n
Du fragst dich was die Katze von dir will und folgst ihr."""


def zu_abteil_4(streak):
    forget_buttons()
    reassign_button(
        button_current_1,
        "Ok",
        lambda: abteil_constructor.abteil_4_obj.init_streak(streak),
        columnGrid=2,
        padxGrid=60
    )


def zu_abteil_2(streak):
    forget_buttons()
    abteil_constructor.abteil_2_obj.init_streak(streak)


def kein_leckerli():
    app.configure(bg=bg["abteil1_monster"])
    current_image.configure(file="images/monster.png")
    label_current.config(
        text=f"""Er guckt sehr traurig als er sieht, dass das Leckerli
    in der Tasche verschwindet.\nJetzt hast du ein schlechtes Gewissen.\n\n{katze}""",
        bg=bg["abteil1_monster"],
        fg=color["abteil1_monster"]
    )
    zu_abteil_4(1)


def leckerli():
    app.configure(bg=bg["abteil1_leckerli"])
    abteil_constructor.abteil_1_obj.inventar.remove("Leckerli")
    label_current.config(
        text=f"""Der Mops freut sich und schlappert
    dir als Dank die Hand ab!\n\n{katze}""",
        bg=bg["abteil1_leckerli"],
        fg=color["abteil1_leckerli"]
    )
    zu_abteil_4(1)


def dog_quiz(e):
    # wenn guess_entry value "" ist, assign 0 to guess_entry
    try:
        guess_entry.get()
    except:
        guess_entry.set(0)

    key_age_dog = 64
    dog_year_converter = int((math.log(16) * guess_entry.get()) + 31)

    global guesses_made
    guesses_made += 1

    if guesses_made < 6:
        if key_age_dog < dog_year_converter:
            entry_current.delete(0, END)
            label_current.config(text="Dein Tipp war zu hoch.")
        elif key_age_dog > dog_year_converter:
            entry_current.delete(0, END)
            label_current.config(text="Dein Tipp war zu niedrig.")
        elif dog_year_converter == key_age_dog:
            entry_current.destroy()
            label_current.config(
                text=f"""Richtig! Du hast nach {guesses_made} Tipps das Alter erraten!\nDafür
            erhälst du ein Leckerli in deinem Inventar!\nMöchtest du dein Leckerli dem Mops geben?"""
            )
            abteil_constructor.abteil_1_obj.inventar.append("Leckerli")
            print(abteil_constructor.abteil_1_obj.inventar)
            reassign_button(button_current_1, "Ja", leckerli, width=10)
            reassign_button(button_current_2, "Nein", kein_leckerli, width=10)
    if guesses_made == 6 and dog_year_converter != key_age_dog:
        entry_current.destroy()
        label_current.config(
            text=f"""Leider nicht richtig geraten.\nDas Alter des Hundes ist {key_age_dog}
            Jahre alt in Menschenalter.\nDu ärgerst dich ein wenig.\n{katze}"""
        )
        zu_abteil_4(1)


def streak_1_3():
    app.configure(bg=bg["abteil1_intro"])
    current_image.configure(file="images/abteil_1.png")
    forget_buttons()
    label_current.config(
        text="""Endlich wieder in Sicherheit. Du schaust aus dem Fenster,
    unterhälst dich mit der alten Lady und genießt die Reise.""",
        bg=bg["abteil1_intro"]
    )
    reassign_button(
        button_current_1,
        "Spiel beenden",
        app.destroy,
        color["goodbye_button"],
        columnGrid=2,
        padxGrid=60
    )


def streak_1_2(intro):
    current_image.configure(file="images/dog_quiz.png")
    if intro == 1:
        label_current.config(
            text="""Sie antwortet freundlich das er noch recht rüstig ist für sein Alter
        und gibt ihm ein Leckerli.\nSie fragt dich, ob du sein Alter erraten kannst? Gib einen Tipp ab:"""
        )
    elif intro == 2:
        label_current.config(
            text="""Du kehrst zu deinem Platz zurück.\nDie Alte Lady mit dem Mops lächelt dich
        nett an und fragt dich, ob du sein wahres Alter erraten kannst."""
        )
    forget_buttons()
    entry_current.grid(padx=5, pady=10, row=2, column=1, columnspan=3)
    entry_current.config(textvariable=guess_entry, bg=bg["abteil1_entry_intro"])
    entry_current.focus()


def streak_1_1():
    app.configure(bg=bg["abteil1_intro"])
    current_image.configure(file="images/abteil_1.png")

    label_current.config(
        text="""Im Zug lässt du dich auf deinem Sitzplatz nieder und schaust dich um.\nDie Sitze sind mit dunkelrotem Samt
    bezogen und die Wände mit dunklem Holz verkleidet.\nDer 20er Jahre Stil ist genau nach deinem Geschmack.
    \nEine nette alte Dame setzt sich mit ihrem\nalten röchelden Mops neben dich und lächelt dich an.\nWas tust du?""",
        font=font_texts,
        bg=bg["abteil1_intro"],
        fg=color["abteil1_intro"]
    )
    reassign_button(
        button_current_1,
        "Du verlässt genervt deinen Platz.\nDas röcheln hälst du nicht aus.\nDu streifst durch den Zug.",
        lambda: zu_abteil_2(1),
        color["abteil1_button_intro"],
        width=50
    )
    reassign_button(
        button_current_2,
        "Du sprichst die Dame auf das Alter ihres Hundes an\nund streichelst ihn über den Kopf.",
        lambda: streak_1_2(1),
        color["abteil1_button_intro"],
        width=50
    )


entry_current.bind("<Return>", dog_quiz)

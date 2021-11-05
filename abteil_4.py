from tkinter import Frame
import abteil_constructor
from main_gui import *

frame_zahlenschloss = Frame(app)
schloss_öffnen = "64"
guessed_code = {}


def destroy_zahlenschloss():
    frame_zahlenschloss.grid_forget()


def koffer_offen():
    forget_buttons()
    label_current.config(
        text="""Richtig geraten! Als du in den Koffer öffnest fällt dir ein Foto in die Hände.\n
    Darauf ist eine Katzenfamilie zu sehen.\nDie Katze, die dich hergeführt hast ist anscheinend mit auf dem Bild.\n
    Auf der Hinterseite steht 'Pivo' geschrieben. Ob das der Name dieser Katze ist?\n
    Die Katze hat wohl Ihre/n Besitzer*n verloren.
    Was nun?""",
        font=font_texts,
    )
    # reassign_button(button_current_1, "nach Ausweispapieren im Koffer suchen", )
    # reassign_button(button_current_2, "den Koffer wieder schließen und\ndem/der Schaffner*in Bescheid gehen", )


def check_code():
    guess = ""
    for i in guessed_code.values():
        guess += i
    if guess == schloss_öffnen:
        destroy_zahlenschloss()
        koffer_offen()
    else:
        label_current.config(text="Leider falsch, probier es noch einmal!")


def change_code(op, element):
    if op == "+":
        element["text"] += 1 if element["text"] < 9 else 0
    elif op == "-":
        element["text"] -= 1 if element["text"] > 0 else 0
    guessed_code.update({element: str(element["text"])})


def create_counter_index(amount_i):
    label = ["label_code_" + str(var + 1) for var in range(amount_i)]
    counter_plus = ["counter_plus_" + str(var + 1) for var in range(amount_i)]
    counter_minus = ["counter_minus_" + str(var + 1) for var in range(amount_i)]
    frame_zahlenschloss.grid(row=2, column=2)
    frame_zahlenschloss.grid_rowconfigure([0, 1, 2], weight=1)
    frame_zahlenschloss.grid_columnconfigure([0, 1], weight=1)
    for counter_element in range(amount_i):
        label[counter_element] = Label(frame_zahlenschloss, text=0)
        label[counter_element].config(width=10, height=3)
        counter_plus[counter_element] = Button(
            frame_zahlenschloss,
            text="+",
            command=lambda name=label[counter_element]: change_code("+", name),
        )
        counter_plus[counter_element].config(width=10, height=3)
        counter_minus[counter_element] = Button(
            frame_zahlenschloss,
            text="-",
            command=lambda name=label[counter_element]: change_code("-", name),
        )
        counter_minus[counter_element].config(width=10, height=3)

        counter_plus[counter_element].grid(
            row=0,
            column=counter_element + 1,
            sticky="ne" if not counter_element else "nw",
        )
        label[counter_element].grid(
            row=1,
            column=counter_element + 1,
            sticky="e" if not counter_element else "w",
        )
        counter_minus[counter_element].grid(
            row=2,
            column=counter_element + 1,
            sticky="se" if not counter_element else "sw",
        )


def zahlenschloss():
    app.config(bg=bg["abteil4_koffer"])

    label_current.config(
        text="""Errate den Code:\n
    (ein kleiner Tipp: Vielleicht kann dir das Alter des Mopses weiterhelfen.)""",
        bg=bg["abteil4_koffer"],
        font=font_texts_large,
    )
    forget_buttons()
    create_counter_index(2)
    reassign_button(
        button_current_1,
        "Code ausprobieren",
        check_code,
        color["abteil4_button_koffer"],
    )
    button_current_1.grid(padx=60, row=3, column=2)
    button_current_1.config(height=2)


def gepaeckwagen_ade():
    label_current.config(
        text="""Du schaust dich eine Weile um, siehst aber nichts Interessantes.\n
    Die Katze mauzt dich noch mehrmals an.\n
    Du ignorierst es und beschließt wieder ins Abteil 1 zurück zu gehen."""
    )
    forget_buttons()
    reassign_button(
        button_current_1,
        "Zurück zu Abteil 1",
        lambda: abteil_constructor.abteil_1_obj.init_streak(3),
    )
    button_current_1.grid(padx=60, row=3, column=2)
    button_current_1.config(height=2)


def koffer():
    app.config(bg=bg["abteil4_hell"])
    current_image.configure(file="images/katze.png")

    label_current.config(
        text="""Du siehst die Katze neben einem Koffer sitzen.\nDieser ist auffällig beklebt.\n
        Dir fällt auf das der Koffer ein Zahlenschloss hat.\nWas tust du?""",
        bg=bg["abteil4_hell"],
        fg=color["abteil4_hell"],
    )
    reassign_button(
        button_current_1, "Koffer öffnen", zahlenschloss, color["abteil4_button_hell"]
    )
    reassign_button(
        button_current_2,
        "Koffer in Ruhe lassen",
        gepaeckwagen_ade,
        color["abteil4_button_hell"],
    )


def im_dunkeln():
    current_image.configure(file="images/katze_schreit.png")

    label_current.config(
        text="""Du vernimmst Katzengeschrei. Du bist der Katze im Dunkeln auf den Schwanz getreten.\n
    Nach deiner Entschuldigung deutet sie auf die Lampe in der Ecke.\nUnd nun?"""
    )
    reassign_button(button_current_1, "Du machst Licht und siehst dich um", koffer)
    reassign_button(
        button_current_2,
        "Es ist dir zu gruselig und kehrst in Abteil 1 zurück",
        lambda: abteil_constructor.abteil_1_obj.init_streak(3),
    )
    button_current_1.config(width=30)
    button_current_2.config(width=40)


def streak_4_1():
    app.config(bg=bg["abteil4_dunkel"])
    current_image.configure(file="images/katze.png")

    label_current.config(
        text="Du folgst der Katze bis in den Gepäckwagen. Hier ist es dunkel. Was tust du?",
        bg=bg["abteil4_dunkel"],
        fg=color["abteil4_dunkel"],
    )
    reassign_button(
        button_current_1, "Lampe suchen", koffer, color["abteil4_button_dunkel"]
    )
    reassign_button(
        button_current_2,
        "Im Dunkeln vorantasten",
        im_dunkeln,
        color["abteil4_button_dunkel"],
    )
    button_current_1.config(width=20, height=5)
    button_current_2.config(width=20, height=5)

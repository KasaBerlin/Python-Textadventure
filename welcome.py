import random
from abteil_1 import abteil_1


def streak_b():
    final_action = input(
        """Die beiden verlassen den Bahnhof. Du verpasst deinen Zug und dein
    toller Gewinn verfällt... Willst du noch einmal von vorn beginnen? (Y)es or (N)o"""
    )
    print()
    abteil_1.inventar.clear()
    if final_action.upper() == "Y":
        welcome()
    else:
        print()
        print("Schade! Auf Wiedersehen!")


def welcome():
    urlaubsgeld = random.randrange(90, 110)
    abteil_1.assign_inventar(urlaubsgeld)
    username = input("Gib deinen Spieler*innennamen an?")
    print()
    print(
        f"""Herzlichen Glückwunsch!\n{username} du hast eine Zugfahrt im Bergland-Express im Radio-Quiz gewonnen! Du hast {urlaubsgeld}DM Urlaubsgeld dabei!\nDu beginnst deine Reise am Bahnsteig, wo dir ein seltsames Paar auffällt."""
    )
    action_1 = input("""Was tust du? (B)eobachten oder (I)gnorieren""")
    print()
    if action_1.upper() == "B":
        streak_b()
    elif action_1.upper() == "I":
        abteil_1.init_streak(1)


welcome()

import abteil_1
import abteil_2
import abteil_3


class Abteil:
    def __init__(
        self,
        nummer=0,
        farbe="",
        passagiere={},
        geschwindigkeit=0.0,
        faehrt_schnell=False,
        streaks={},
        inventar=[],
    ):
        self.nummer = nummer
        self.farbe = farbe
        self.passagiere = passagiere
        self.geschwindigkeit = geschwindigkeit
        self.faehrt_schnell = faehrt_schnell
        self.streaks = streaks
        self.inventar = inventar

    def init_streak(self, i):
        self.streaks[i]()

    def assign_inventar(self, inv):
        self.inventar.append(inv)


abteil_1_obj = Abteil(
    1,
    "rot",
    {1: "alte Lady", 2: "rüstiger Mops"},
    0.0,
    False,
    {1: abteil_1.streak_i},
)
abteil_2_obj = Abteil(
    2,
    "gruen",
    {1: "alte Lady", 2: "rüstiger Mops", 3: "Kellner"},
    0.0,
    False,
    {1: abteil_2.streak_1},
)
abteil_3_obj = Abteil(
    3,
    "blau",
    {1: "Lokführer"},
    200.0,
    True,
    {1: abteil_3.streak_emergency},
)

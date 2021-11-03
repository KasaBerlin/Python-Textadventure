from abteil_1 import streak_i, streak_h
from abteil_2 import streak_1
from abteil_3 import streak_emergency


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
    {1: streak_i, 2: streak_h},
)
abteil_2_obj = Abteil(
    1, "rot", {1: "alte Lady", 2: "rüstiger Mops"}, 0.0, False, {1: streak_1}
)

abteil_3_obj = Abteil(
    3,
    "blau",
    {1: "Lokführer"},
    200.0,
    True,
    {1: streak_emergency},
)

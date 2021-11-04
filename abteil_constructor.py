import inspect
from abteil_1 import streak_1_1, streak_1_2
from abteil_2 import streak_2_1
from abteil_3 import streak_3_1
from abteil_4 import streak_4_1

# Parameter sind auskommentiert für spätere Nutzung im Spiel
class Abteil:
    def __init__(
        self,
        # nummer=0,
        # farbe="",
        # passagiere={},
        geschwindigkeit=0.0,
        # faehrt_schnell=False,
        streaks={},
        inventar=[],
    ):
        # self.nummer = nummer
        # self.farbe = farbe
        # self.passagiere = passagiere
        self.geschwindigkeit = geschwindigkeit
        # self.faehrt_schnell = faehrt_schnell
        self.streaks = streaks
        self.inventar = inventar

    def init_streak(self, i, par=None):
        if not inspect.signature(self.streaks[i]).parameters.values():
            self.streaks[i]()
        else:
            self.streaks[i](par)


abteil_1_obj = Abteil(streaks={1: streak_1_1, 2: streak_1_2})
abteil_2_obj = Abteil(streaks={1: streak_2_1})
abteil_3_obj = Abteil(geschwindigkeit=200, streaks={1: streak_3_1})
abteil_4_obj = Abteil(streaks={1: streak_4_1})

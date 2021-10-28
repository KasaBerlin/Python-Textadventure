class Abteil:
    def __init__(self, nummer=0, farbe = '', passagiere = {}, geschwindigkeit = 0.0, faehrt_schnell = False,streaks={}, inventar=[]):
        self.nummer = nummer
        self.farbe = farbe
        self.passagiere = passagiere
        self.geschwindigkeit = geschwindigkeit
        self.faehrt_schnell = faehrt_schnell
        self.streaks=streaks
        self.inventar=inventar
        
    def init_streak(self,i):
        self.streaks[i]()
        
    def assign_inventar(self, inv):
        self.inventar.append(inv)


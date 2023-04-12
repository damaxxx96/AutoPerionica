from Zaposleni import Zaposleni

from Klijent import Klijent

from Automobil import Automobil


class PerionicaAutomobila:
    def __init__(self, ime: str):
        self.ime = ime
        self.zaposleni: list[Zaposleni] = []
        self.klijenti: list[Klijent] = []
        self.automobili: list[Automobil] = []

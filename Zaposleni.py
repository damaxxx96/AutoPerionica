from enum import Enum


class TipZaposlenog(Enum):
    RADNIK = (1,)
    MENADZER = (2,)


class Zaposleni:
    def __init__(
        self,
        ime: str,
        broj_telefona: str,
        email: str,
        ID_zaposlenog: int,
        tip_zaposlenog: TipZaposlenog,
    ):
        self.ime = ime
        self.broj_telefona = broj_telefona
        self.email = email
        self.ID_zaposlenog = ID_zaposlenog
        self.tip_zaposlenog = tip_zaposlenog

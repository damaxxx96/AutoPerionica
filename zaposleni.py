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
        id: int,
        tip_zaposlenog: TipZaposlenog,
    ):
        self.ime = ime
        self.broj_telefona = broj_telefona
        self.email = email
        self.id = id
        self.tip_zaposlenog = tip_zaposlenog

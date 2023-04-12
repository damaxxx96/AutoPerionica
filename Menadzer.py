from Zaposleni import Zaposleni
from Zaposleni import TipZaposlenog


class Menadzer(Zaposleni):
    def __init__(
        self,
        ime: str,
        broj_telefona: str,
        email: str,
        ID_zaposlenog: int,
        tip_zaposlenog: TipZaposlenog,
    ):
        super().__init__(ime, broj_telefona, email, ID_zaposlenog, tip_zaposlenog)

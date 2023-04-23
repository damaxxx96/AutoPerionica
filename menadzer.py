from zaposleni import Zaposleni
from zaposleni import TipZaposlenog


class Menadzer(Zaposleni):
    def __init__(
        self,
        ime: str,
        broj_telefona: str,
        email: str,
        id: int,
        tip_zaposlenog: TipZaposlenog,
    ):
        super().__init__(ime, broj_telefona, email, id, tip_zaposlenog)

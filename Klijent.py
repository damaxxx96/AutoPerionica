from Automobil import Automobil


class Klijent:
    def __init__(
        self,
        ime: str,
        broj_telefona: int,
        email: str,
        posedovani_automobil: Automobil,
        id: int,
    ):
        self.ime = ime
        self.broj_telefona = broj_telefona
        self.email = email
        self.posedovani_automobil = posedovani_automobil
        self.id = id

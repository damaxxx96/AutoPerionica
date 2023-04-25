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

    def zaposli_radnika(self, svi_radnici: list[Zaposleni]) -> Zaposleni:
        unos_imena = input("Unesite ime novog radnika: ")
        unos_broja_telefona = input ("Unesite broj telefona novog radnika: ")
        unos_email = input ("Unesite email novog radnika: ")
        tip_zaposlenog = TipZaposlenog.RADNIK
        id = max(list(map(lambda zaposleni: zaposleni.id, svi_radnici))) + 1
        
        novi_radnik = Zaposleni(unos_imena, unos_broja_telefona, unos_email, id, tip_zaposlenog)
        
        return novi_radnik
        
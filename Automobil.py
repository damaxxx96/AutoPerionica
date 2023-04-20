from enum import Enum


class ModelAutomobila(Enum):
    FIAT = (1,)
    MERCEDES = (2,)
    OPEL = (3,)
    AUDI = (4,)
    NISSAN = (5,)
    ALFA_ROMEO = (6,)
    BMW = (7,)
    VW = (8,)
    VOLVO = (9,)
    TOYOTA = (10,)


class BojaAutomobila(Enum):
    CRVENA = (1,)
    PLAVA = (2,)
    ZELENA = (3,)
    ZUTA = (4,)
    CRNA = (5,)


class Automobil:
    def __init__(
        self,
        model: ModelAutomobila,
        boja: BojaAutomobila,
        registracioni_broj: str,
        da_li_je_cist: bool,
        klijent: int,
        id: int,
    ):
        self.model = model
        self.boja = boja
        self.registracioni_broj = registracioni_broj
        self.da_li_je_cist = da_li_je_cist
        self.klijent = klijent
        self.id = id

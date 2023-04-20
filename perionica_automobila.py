import json
from menadzer import Menadzer
from zaposleni import TipZaposlenog, Zaposleni
from klijent import Klijent
from automobil import Automobil, BojaAutomobila, ModelAutomobila


class PerionicaAutomobila:
    def __init__(self, ime: str):
        self.ime = ime
        self.zaposleni: list[Zaposleni] = []
        self.klijenti: list[Klijent] = []
        self.automobili: list[Automobil] = []

    def ucitaj_klijente(self) -> bool:
        try:
            f = open("database/klijenti.json", "r")
            ucitani_klijenti: list[dict] = json.load(f)
            f.close()

            for ucitan_klijent in ucitani_klijenti:
                klijent = Klijent(
                    ucitan_klijent["ime"],
                    ucitan_klijent["broj_telefona"],
                    ucitan_klijent["email"],
                    ucitan_klijent["posedovani_automobil"],
                    ucitan_klijent["id"],
                )

                self.klijenti.append(klijent)

            return True

        except:
            return False

    def ucitaj_automobile(self) -> bool:
        try:
            f = open("database/automobili.json", "r")
            ucitani_automobili: list[dict] = json.load(f)
            f.close()

            for ucitan_automobil in ucitani_automobili:
                model_automobila = ModelAutomobila[ucitan_automobil["model"]]
                boja_automobila = BojaAutomobila[ucitan_automobil["boja"]]
                automobil = Automobil(
                    model_automobila,
                    boja_automobila,
                    ucitan_automobil["registracioni_broj"],
                    ucitan_automobil["da_li_je_cist"],
                    ucitan_automobil["klijent"],
                    ucitan_automobil["id"],
                )

                self.automobili.append(automobil)

            return True

        except:
            return False

    def ucitaj_zaposlene(self) -> bool:
        try:
            f = open("database/zaposleni.json", "r")
            ucitani_zaposleni: list[dict] = json.load(f)
            f.close()

            for ucitani_zaposlen in ucitani_zaposleni:
                tip_zaposlenog = TipZaposlenog[ucitani_zaposlen["tip_zaposlenog"]]

                if tip_zaposlenog == TipZaposlenog.RADNIK:
                    zaposleni = Zaposleni(
                        ucitani_zaposlen["ime"],
                        ucitani_zaposlen["broj_telefona"],
                        ucitani_zaposlen["email"],
                        ucitani_zaposlen["id"],
                        tip_zaposlenog,
                    )

                    self.zaposleni.append(zaposleni)

                else:
                    menadzer = Menadzer(
                        ucitani_zaposlen["ime"],
                        ucitani_zaposlen["broj_telefona"],
                        ucitani_zaposlen["email"],
                        ucitani_zaposlen["id"],
                        tip_zaposlenog,
                    )

                    self.zaposleni.append(menadzer)

            return True

        except:
            return False

    def info_klijent(self, klijent_id: int) -> None:
        klijent = next(filter(lambda klijent: klijent.id == klijent_id, self.klijenti))

        print("Ime Klijenta: " + klijent.ime)
        print("Broj telefona klijenta: " + klijent.broj_telefona)
        print("Email klijenta: " + klijent.email)

        automobil = next(
            filter(
                lambda automobil: automobil.id == klijent.posedovani_automobil,
                self.automobili,
            )
        )

        print(
            "Posedovani automobil "
            + automobil.model.name
            + " "
            + automobil.boja.name
            + " "
            + automobil.registracioni_broj
        )

    def info_automobil(self, automobil_id: int) -> None:
        automobil = next(
            filter(lambda automobil: automobil.id == automobil_id, self.automobili)
        )

        print("Model automobila " + automobil.model.name)
        print("Boja automobila " + automobil.boja.name)
        print("Registacioni broj automobila " + automobil.registracioni_broj)
        print(
            "Automobil je cist"
            if automobil.da_li_je_cist == True
            else "Automobil je prljav"
        )

        klijent = next(
            filter(lambda klijent: klijent.id == automobil.klijent, self.klijenti)
        )

        print("Klijent " + klijent.ime)

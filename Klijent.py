class Klijent:
    def __init__(
        self,
        ime: str,
        broj_telefona: str,
        email: str,
        posedovani_automobil: int,
        id: int,
    ):
        self.ime = ime
        self.broj_telefona = broj_telefona
        self.email = email
        self.posedovani_automobil = posedovani_automobil
        self.id = id

    def info(self, automobili) -> None:
        print("Ime Klijenta: " + self.ime)
        print("Broj telefona klijenta: " + self.broj_telefona)
        print("Email klijenta: " + self.email)

        automobil = next(
            filter(
                lambda automobil: automobil.id == self.posedovani_automobil, automobili
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

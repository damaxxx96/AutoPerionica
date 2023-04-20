import os
import sys
from perionica_automobila import PerionicaAutomobila


def info_klijenti(perionica: PerionicaAutomobila):
    while True:
        svi_klijent_id = list(map(lambda klijent: klijent.id, perionica.klijenti))
        print("-------------")
        print("Klijenti")
        print("-------------")
        for klijent in perionica.klijenti:
            print(str(klijent.id) + " - " + klijent.ime)
        print("-------------")

        unos_id_klijenta = input("Unesite ID klijenta: ")
        os.system("cls")

        if unos_id_klijenta.isdigit():
            id_klijenta = int(unos_id_klijenta)
            if id_klijenta in svi_klijent_id:
                perionica.info_klijent(id_klijenta)
                break
            else:
                print("Klijent sa ovim ID-em ne postoji!")
        else:
            print("Pogresan unos!")


def info_automobili(perionica: PerionicaAutomobila):
    while True:
        svi_automobili_id = list(
            map(lambda automobil: automobil.id, perionica.automobili)
        )
        print("-------------")
        print("Automobili")
        print("-------------")
        for automobil in perionica.automobili:
            print(
                str(automobil.id)
                + " - "
                + automobil.model.name
                + " | "
                + automobil.boja.name
                + " | "
                + automobil.registracioni_broj
            )
        print("-------------")

        unos_id_automobila = input("Unesite ID automobila: ")
        os.system("cls")

        if unos_id_automobila.isdigit():
            id_automobila = int(unos_id_automobila)
            if id_automobila in svi_automobili_id:
                perionica.info_automobil(id_automobila)
                break
            else:
                print("Automobil sa ovim ID-em ne postoji!")
        else:
            print("Pogresan unos!")


perionica = PerionicaAutomobila("Rade i majstori")

print("Ucitavanje ...")

status_zaposleni = perionica.ucitaj_zaposlene()

print("Ucitani svi zaposleni") if status_zaposleni == True else print(
    "Neuspesno ucitani zaposleni"
)

status_klijenti = perionica.ucitaj_klijente()

print("Uspesno ucitani klijenti") if status_klijenti == True else print(
    "Neuspesno ucitani klijenti"
)

status_automobili = perionica.ucitaj_automobile()

print("Uspesno ucitani automobili") if status_automobili == True else print(
    "Neuspesno ucitani automobili"
)

while True:
    print("------------------------------------------")
    print("Dobrodosli u perionicu: " + perionica.ime)
    print("------------------------------------------")

    print("1. Informacije o klijentima")
    print("2. Informacije o automobilima")
    print("0. Kraj")
    print("-------------")

    unos = input("Unesite broj: ")
    os.system("cls")

    if unos == "1":
        info_klijenti(perionica)
    elif unos == "2":
        info_automobili(perionica)
    elif unos == "0":
        sys.exit()
    else:
        print("Pogresan unos!")

import os
import sys
from klijent import Klijent
from menadzer import Menadzer
from perionica_automobila import PerionicaAutomobila
from zaposleni import TipZaposlenog, Zaposleni





def logovanje() -> Klijent | Zaposleni | Menadzer:
    while True:
        uneti_email = input ("Unesite Vas email: ")
        os.system("cls")
        
        lista_klijenata = list(filter(lambda klijent: uneti_email == klijent.email, perionica.klijenti))
        
        if len(lista_klijenata) != 0:
            return lista_klijenata[0]
        
        lista_zaposlenih = list(filter(lambda zaposleni: uneti_email == zaposleni.email, perionica.zaposleni))
        
        if len(lista_zaposlenih) != 0:
            return lista_zaposlenih[0]

        print("Korisnik ne postoji!")
    

def info_klijenti(perionica: PerionicaAutomobila) -> None:
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


def info_automobili(perionica: PerionicaAutomobila) -> None:
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

def info_ulogovani_korisnik(ulogovani_korisnik) -> None:
    if isinstance (ulogovani_korisnik,Klijent ):
        print("|| KLIJENT ||")
        print("-------------")
    elif isinstance (ulogovani_korisnik,Zaposleni):
        if ulogovani_korisnik.tip_zaposlenog == TipZaposlenog.RADNIK:
            print("|| ZAPOSLENI ||")
            print("---------------")
        elif ulogovani_korisnik.tip_zaposlenog == TipZaposlenog.MENADZER:
            print("|| MENADZER ||")
            print("--------------")
        else:
            print ("GRESKA, NEPOSTOJECI TIP KORISNIKA!!!")
    else:
        print ("GRESKA, NEPOSTOJECI KORISNIK!!!")
        return
        
    print ("Ime: " + ulogovani_korisnik.ime)
    print ("Email: " + ulogovani_korisnik.email)
    print ("Broj: " + ulogovani_korisnik.broj_telefona)
       

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

ulogovani_korisnik = logovanje()    
    
while True:
    print("------------------------------------------")
    print("Dobrodosli u perionicu: " + perionica.ime)
    print("------------------------------------------")

    print("1. Informacije o klijentima")
    print("2. Informacije o automobilima")
    print("3. Informacije o ulogovanom korisniku")
    print("0. Kraj")
    print("-------------")

    unos = input("Unesite broj: ")
    os.system("cls")

    if unos == "1":
        info_klijenti(perionica)
    elif unos == "2":
        info_automobili(perionica)
    elif unos == "3":
        info_ulogovani_korisnik(ulogovani_korisnik)
    elif unos == "0":
        sys.exit()
    else:
        print("Pogresan unos!")

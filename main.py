from perionicaAutomobila import PerionicaAutomobila

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

print("Dobrodosli u perionicu: " + perionica.ime)

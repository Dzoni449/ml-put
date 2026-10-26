
import random

print("=== Pogodi broj ===")
seme = input("Seme (Enter = nasumično): ").strip()

if seme.isdigit():
    random.seed(int(seme))

MAX_POKUSAJA = 3
broj_pokusaja = 0

print("Zamislio sam broj od 1 do 20. Imaš 3 pokušaja.")

pogodjen_broj = False
poeni = 0
tajni_broj = random.randint(1, 20)

while broj_pokusaja < MAX_POKUSAJA and not pogodjen_broj:
    unos = input(f"Pokušaj {broj_pokusaja + 1}: ").strip()

    if unos.isdigit():
        unos = int(unos)

        if unos == tajni_broj:
            pogodjen_broj = True

            if broj_pokusaja == 0:
                poeni = 100
            elif broj_pokusaja == 1:
                poeni = 60
            else:
                poeni = 30

        else:
            if unos < tajni_broj:
                smer = "Tajni broj je veći."
            else:
                smer = "Tajni broj je manji."

            if abs(unos - tajni_broj) <= 2:
                dodatak = " Vruće!"
            else:
                dodatak = ""

            print(f"{smer}{dodatak}")

    else:
        print("To nije broj! Pokušaj je izgubljen.")

    broj_pokusaja += 1

if pogodjen_broj:
    print(f"Pogodio si iz {broj_pokusaja}. pokušaja!")
    print(f"Poeni: {poeni}")
else:
    print(f"Kraj igre! Tajni broj je bio {tajni_broj}.")

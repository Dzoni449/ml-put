# 1. uvoz modula
# 2. naslov igre
# 3. pitaj za seme; ako su cifre, postavi seme
# 4. izaberi tajni broj, ispiši pravila
# 5. pripremi zastavicu i poene
# 6. pokušaj 1: unos -> da li je broj? -> pogodak ili hint
# 7. pokušaj 2 (samo ako nije pogođen)
# 8. pokušaj 3 (samo ako nije pogođen)
# 9. kraj: poeni ili otkrij tajni broj

import random

print("=== Pogodi broj ===")

seme = input("Seme (Enter = nasumično): ").strip()

if seme.isdigit():
    random.seed(int(seme))

tajni_broj = random.randint(1, 20)

print("Zamislio sam broj od 1 do 20. Imaš 3 pokušaja.")

pogodjen = False
poeni = 0

# --- pokušaj 1 ---
unos = input("Pokušaj 1: ").strip()

if not unos.isdigit():
    print("To nije broj! Pokušaj je izgubljen.")
else:
    broj = int(unos)

    if broj == tajni_broj:
        pogodjen = True
        poeni = 100
        print("Pogodio si iz 1. pokušaja!")
    else:
        if broj < tajni_broj:
            smer = "Tajni broj je veći"
        else:
            smer = "Tajni broj je manji"

        if abs(broj - tajni_broj) <= 2:
            dodatak = " Vruće!"
        else:
            dodatak = ""

        print(f"{smer}.{dodatak}")

# --- pokušaj 2 ---
if not pogodjen:
    unos = input("Pokušaj 2: ").strip()

    if not unos.isdigit():
        print("To nije broj! Pokušaj je izgubljen.")
    else:
        broj = int(unos)

        if broj == tajni_broj:
            pogodjen = True
            poeni = 60
            print("Pogodio si iz 2. pokušaja!")
        else:
            if broj < tajni_broj:
                smer = "Tajni broj je veći"
            else:
                smer = "Tajni broj je manji"

            if abs(broj - tajni_broj) <= 2:
                dodatak = " Vruće!"
            else:
                dodatak = ""

            print(f"{smer}.{dodatak}")


if not pogodjen:
    unos = input("Pokušaj 3: ").strip()

    if not unos.isdigit():
        print("To nije broj! Pokušaj je izgubljen.")
    else:
        broj = int(unos)

        if broj == tajni_broj:
            pogodjen = True
            poeni = 30
            print("Pogodio si iz 3. pokušaja!")
        else:
            if broj < tajni_broj:
                smer = "Tajni broj je veći"
            else:
                smer = "Tajni broj je manji"

            if abs(broj - tajni_broj) <= 2:
                dodatak = " Vruće!"
            else:
                dodatak = ""

            print(f"{smer}.{dodatak}")


if pogodjen:
    print(f"Poeni: {poeni}")
else:
    print(f"Kraj igre! Tajni broj je bio {tajni_broj}.")

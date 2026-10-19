pregledi = int(input("Pregledi: "))
lajkovi = int(input("Lajkovi: "))
prosecno_gledanje = float(input("Prosečno odgledano (%): "))

if pregledi >= 100000:
    nivo = "Viralan"
    zvezdice = 5
elif pregledi >= 10000:
    nivo = "Odličan"
    zvezdice = 4
elif pregledi >= 1000:
    nivo = "Dobar"
    zvezdice = 3
elif pregledi >= 100:
    nivo = "Prosečan"
    zvezdice = 2
else:
    nivo = "Početak"
    zvezdice = 1 

stopa_lajkova = 0

if pregledi != 0:
    stopa_lajkova = lajkovi / pregledi

if pregledi == 0:
    ocena = "nema podataka"
elif stopa_lajkova >= 0.08:
    ocena = "izuzetna"
elif stopa_lajkova >= 0.04:
    ocena = "dobra"
elif stopa_lajkova >= 0.02:
    ocena = "prosečna"
else:
    ocena = "slaba"

if pregledi == 0:
    savet = "Objavi klip i podeli ga sa prijateljima!"
elif prosecno_gledanje < 50:
    savet = "Skrati uvod, gledaoci odlaze rano."
elif stopa_lajkova < 0.04:
    savet = "Na kraju klipa zamoli gledaoce za lajk."
else:
    savet = "Odlično, nastavi ovako!"

print("=== Ocena klipa ===")
print(f"Nivo: {nivo}")
print(f"Zvezdice: {'*' * zvezdice}")
if pregledi == 0:
    print(f"Stopa lajkova: {ocena}")
else:
    print(f"Stopa lajkova: {stopa_lajkova:.2%} ({ocena})")
print(f"Savet: {savet}")
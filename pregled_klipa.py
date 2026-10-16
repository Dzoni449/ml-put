naslov = input("Naslov: ")
broj_pregleda = int(input("Pregledi: "))
broj_novih_pratilaca = int(input("Novi pratioci: "))

naslov = naslov.strip()

print("=== Pregled klipa ===")
print("Naslov:", naslov)

duzina_naslova = len(naslov)

if duzina_naslova <= 20:
    print("Preview:", naslov)
else:
    print("Preview:", naslov[:20] + "...")

print(f"Pregledi: {broj_pregleda:,}")

if broj_novih_pratilaca != 0:
    pregleda_po_novom_pratiocu = broj_pregleda / broj_novih_pratilaca
    print(f"Pregleda po novom pratiocu: {round(pregleda_po_novom_pratiocu)}")
else:
    print("Pregleda po novom pratiocu: nema novih pratilaca")

if broj_pregleda >= 10000:
    print("Status: Cilj od 10,000 pregleda je dostignut!")
else:
    print(f"Status: Do 10,000 pregleda fali još {10000 - broj_pregleda:,}.")    


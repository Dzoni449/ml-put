#A
# 1. 3, 1 ,1 3.5
# 2. hon
# 3. pogresan tip
# 4. true
# 5. 1%
# 6. abab c
# 7. 3
# 8. 3
# 9. ab
# 10.[   ok]

#B
#cena = int(input("Cena: "))
#kolicina = int(input("Količina: "))
#ukupno = cena * kolicina
#pdv = ukupno * int((20/100))
#naziv = "  laptop  "
#velika_kupovina = 100000 <= ukupno <= 500000
#print("Naziv:", naziv.strip(), "Ukupno sa PDV:", ukupno + pdv)

#prvi baj je vio u 4 redu gde se racunao procenat
# drugi bag koji sam nasao u velikoj kupovini lose je bilo ograniceno plus kombinacija 
# treci bag je takodje u okviru pdv morace float da se castuje u int
# cena je uzimala str zbog inputa a treba da bude int
# takodje naziv.strip() nista nije radilo pa sam prebacio u printu

#----------------------------------------------------------------------

restoran = input("Restoran: ")
racun = float(input("Iznos računa (din): "))
procenat_napojnice = int(input("Napojnica (%): "))
broj_osoba = int(input("Broj osoba: "))
kod_za_popust = input("Kod za popust: ")

naziv_restorana_bez_razmaka = restoran.strip().title()
vazeci_kod = kod_za_popust.strip().lower() == "python10"

popust = (vazeci_kod * racun) * 0.10

udeo_napojnice = procenat_napojnice/100

iznos_posle_popusta = racun - popust

diniznos_napojnice = (iznos_posle_popusta) * udeo_napojnice



ukupno = (iznos_posle_popusta) + diniznos_napojnice

po_osobi = ukupno / broj_osoba

vise_po_osobi = po_osobi > 1000

procenat_napojnice_ispis = f"Napojnica ({procenat_napojnice}%)"
po_osobi_ispis = f"Po osobi ({broj_osoba})"


print("=" * 40)
print(f"{naziv_restorana_bez_razmaka:^40}")
print("=" * 40)
print(f"{"Iznos računa":<24}{racun:>12,.2f} din")
print(f"{"Popust":<24}{popust:>12,.2f} din")
print(f"{procenat_napojnice_ispis:<24}{diniznos_napojnice:>12,.2f} din")
print("-" * 40)
print(f"{"UKUPNO":<24}{ukupno:>12,.2f} din")
print(f"{po_osobi_ispis:<24}{po_osobi:>12,.2f} din")
print("=" * 40)
print(f"{"Kod za popust važi:"} {vazeci_kod}")
print(f"{"Po osobi više od 1,000 din:"} {vise_po_osobi}")




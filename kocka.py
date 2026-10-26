# srediti ulog_unos i ulog
#srediti strip().lower jednom
# opseg
# predvidjanje kao lestvica
# bez exit
# dobitak sa ,
# test



import random

print("=== Kocka ===")
seme = input("Seme (Enter = nasumično): ").strip()
ulog_unos = input("Ulog (10-1000 din): ").strip()
predvidjanje = input("Predviđanje (visoko / nisko / broj 1-6): ").strip().lower()


broj_gresaka = 0
if seme.isdigit():
    random.seed(int(seme))

if ulog_unos.isdigit():
    ulog = int(ulog_unos)


if not ulog_unos.isdigit():
    print("Greška: Ulog mora biti ceo broj.")
    broj_gresaka +=1
elif not 10 <= ulog <= 1000:
    print("Greška: Ulog mora biti između 10 i 1000 din.")
    broj_gresaka +=1

tip = ""

if predvidjanje == "visoko" or predvidjanje == "v":
    tip = "visoko"
elif predvidjanje == "nisko" or predvidjanje == "n":
    tip = "nisko"
elif predvidjanje.isdigit() and 1 <= int(predvidjanje) <= 6:
    tip = "broj"
else:
    print("Greška: Predviđanje mora biti visoko, nisko ili broj od 1 do 6.")
    broj_gresaka+=1

if broj_gresaka > 0:
    print(f"Pronađeno grešaka: {broj_gresaka}. Bacanja nema.")
else:


    print("--- Bacanje ---")

    kocka = random.randint(1,6)

    print(f"Pala je: {kocka}")





    if not predvidjanje.isdigit():
        predvidjanje = predvidjanje.lower()

    if predvidjanje.isdigit():
        predvidjanje = int(predvidjanje)

    if predvidjanje == kocka:
        print(f"Pogodio si! Dobitak: {ulog * 5:,} din")

    elif predvidjanje == "visoko" or predvidjanje == "v":
        if kocka == 4 or kocka == 5 or kocka == 6:
            print(f"Pogodio si! Dobitak: {ulog * 2:,} din")
        else:
            print(f"Nisi pogodio. Izgubio si: {ulog:,} din.")

    elif predvidjanje == "nisko" or predvidjanje == "n":
        if kocka == 1 or kocka == 2 or kocka == 3:
            print(f"Pogodio si! Dobitak: {ulog * 2:,} din")
        else:
            print(f"Nisi pogodio. Izgubio si: {ulog:,} din.")



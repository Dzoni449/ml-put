
print("=== Novi klip ===")

naslov = input("Naslov: ").strip()
trajanje = input("Trajanje (s): ").strip()
budzet = input("Budžet za promociju (din): ").strip()
javan = input("Javan klip? (da/ne): ").strip().lower()

duzina_naslova = len(naslov)

broj_gresaka = 0
greska_naslov = ""
greska_budzet = ""
greska_trajanje = ""
greska_vidljivost = ""

if not naslov:
    greska_naslov = "Greška: Naslov je obavezan."
    broj_gresaka +=1
elif not 1 <= duzina_naslova <= 60:
    greska_naslov = f"Greška: Naslov je predugačak ({duzina_naslova}/60 znakova)."
    broj_gresaka +=1

if not trajanje.isdigit():
    greska_trajanje = "Greška: Trajanje mora biti ceo broj."
    broj_gresaka +=1
elif not 1 <= int(trajanje) <= 180:
    greska_trajanje = "Greška: Trajanje mora biti između 1 i 180 s."
    broj_gresaka +=1

budzet = budzet.replace(",",".")

if not budzet:
    budzet = 0
elif not budzet.replace(".","", 1).isdigit():
    greska_budzet = "Greška: Budžet mora biti broj (npr. 1500 ili 1500,50)."
    broj_gresaka +=1

vidljivost = ""
if javan == "da" or javan == "d":
    vidljivost = "javan"
elif javan == "ne" or javan == "n":
    vidljivost = "privatan"
else:
    greska_vidljivost = "Greška: Odgovori sa da ili ne."
    broj_gresaka +=1

print("--- Provera ---")
if greska_naslov != "":
    print(greska_naslov)
if greska_trajanje != "":
    print(greska_trajanje)
if greska_budzet != "":
    print(greska_budzet)
if greska_vidljivost != "":
    print(greska_vidljivost)



if broj_gresaka != 0:
    print(f"Pronađeno grešaka: {broj_gresaka}. Klip nije sačuvan.")
else:
    print("Sve je ispravno!")
    print(f"Naslov: {naslov}")
    print(f"Trajanje: {int(trajanje) // 60}:{int(trajanje) % 60:02d}")
    print(f"Budžet: {float(budzet):,.2f}"  + " din")
    print(f"Vidljivost: {vidljivost}")
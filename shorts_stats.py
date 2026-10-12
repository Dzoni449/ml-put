
pregledi = int(input("Pregledi: "))
lajkovi = int(input("Lajkovi: "))
komentari = int(input("Komentari: "))
deljenje = int(input("Deljenja: "))
trajanje_klipa = int(input("Trajanje klipa (s): "))
prosecno_vreme_gledanja = float(input("Prosečno vreme gledanja (s): "))
pratioci = int(input("Novi pratioci: "))

eng_rate = (lajkovi + komentari + deljenje) / pregledi
prosecno_odgledano = prosecno_vreme_gledanja / trajanje_klipa

ukupno_vreme_gledanja = pregledi * prosecno_vreme_gledanja
ukupno_minuta = int(ukupno_vreme_gledanja // 60)

sati = ukupno_minuta // 60
minuti = ukupno_minuta % 60
lajkovi_na_hiljadu = lajkovi / pregledi * 1000;
pregled_po_pratiocu = pregledi/pratioci;


print("=== Statistika Shorts klipa ===")

print(f"Pregledi: {pregledi:,}")
print(f"Trajanje klipa: {trajanje_klipa // 60}:{trajanje_klipa % 60:02d}")
print(f"Engagement rate: {eng_rate:.2%}")
print(f"Prosečno odgledano: {prosecno_odgledano:.1%}")
print(f"Ukupno vreme gledanja: {sati} h {minuti} min")
print(f"Lajkova na 1000 pregleda: {lajkovi_na_hiljadu:.1f}")
print(f"Pregleda po novom pratiocu:  {pregled_po_pratiocu:.0f}")

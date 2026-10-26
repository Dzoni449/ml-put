naslovi = ["Najbolji Python trik", "Savet za VS Code", "Kako da naučiš Python za 30 dana",
           "Moj radni sto", "Python liste za 60 sekundi", "Dan u mom životu"]
pregledi = [48250, 1200, 15000, 3400, 22100, 9800]
lajkovi = [2130, 30, 450, 210, 1650, 300]

print("=== Moji klipovi ===")
print(f"{'#':>2}  {'Naslov':<22}{'Pregledi':>10}{'Stopa':>9}")
print("-" * 45)

najbolja_lista = []
najbolji = 0
for broj,p in enumerate(pregledi,start=1):
    stopa = lajkovi[broj-1] / pregledi[broj-1]
    najbolja_lista.append(stopa) 
    print(f"{broj:>2}  {naslovi[broj-1][:20]:<22}{pregledi[broj-1]:>10,}{stopa:>9.2%}")
    
print("-" * 45)

ukupno = 0

for p in pregledi:
    ukupno+=p


for s in najbolja_lista:
    if s > najbolji:
        najbolji = s

indeks_naslova = najbolja_lista.index(najbolji) 

naslov = naslovi[indeks_naslova]
print(f"Ukupno pregleda: {ukupno:,}")
print()
print(f"Najbolja stopa lajkova: {naslov} ({najbolji:.2%})")

brojac = 0

prazna_lista = []
for p,n in zip(pregledi,naslovi):
    if p > 10000:
        brojac+=1
        vrednost = n
        prazna_lista.append(vrednost)


print(f"Klipovi preko 10,000 pregleda: {brojac}")

for p in prazna_lista:
    print(f"- {p}")


ukupno_naslova = 0
sta_trazim = "Python"
for n in naslovi:
    if sta_trazim.lower() in n.lower():
        ukupno_naslova += 1

print(f"Klipova o Pythonu: {ukupno_naslova} od {len(naslovi)}")
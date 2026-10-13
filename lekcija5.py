naslov1 = "Najbolji Python trik"
pregledi1 = 48250
lajkovi1 = 2130
trajanje1 = 42
stopa1 = lajkovi1 / pregledi1


naslov2 = "Savet za VS Code"
pregledi2 = 1200
lajkovi2 = 30
trajanje2 = 75
stopa2 = lajkovi2 / pregledi2


naslov3 = "Kako da naučiš Python za 30 dana"
pregledi3 = 15000
lajkovi3 = 450
trajanje3 = 58
stopa3 = lajkovi3 / pregledi3

ukupno_pregledi = pregledi1 + pregledi2 + pregledi3
ukupno_lajkovi = lajkovi1 + lajkovi2 + lajkovi3
ukupno_stopa = ukupno_lajkovi / ukupno_pregledi
ukupno_trajanje = trajanje1 + trajanje2 + trajanje3
najvise_pregleda = max(pregledi1,pregledi2,pregledi3)
najkraci_klip = min(trajanje1,trajanje2,trajanje3)



print("=" * 60)
print(f"{'IZVEŠTAJ: MOJI SHORTS KLIPOVI':^60}")
print("=" * 60)
print(f"{'Naslov':<22}{'Pregledi':>10}{'Lajkovi':>9}{'Stopa':>9}{'Trajanje':>10}")
print("-" * 60)

print(f"{naslov1[:22]:<22}{pregledi1:>10,}{lajkovi1:>9,}{stopa1:>9.2%}{f'{trajanje1 // 60}:{trajanje1 % 60:02d}':>10}")
print(f"{naslov2[:22]:<22}{pregledi2:>10,}{lajkovi2:>9,}{stopa2:>9.2%}{f'{trajanje2 // 60}:{trajanje2 % 60:02d}':>10}")
print(f"{naslov3[:22]:<22}{pregledi3:>10,}{lajkovi3:>9,}{stopa3:>9.2%}{f'{trajanje3 // 60}:{trajanje3 % 60:02d}':>10}")

print("-" * 60)
print(f"{'UKUPNO':<22}{ukupno_pregledi:>10,}{ukupno_lajkovi:>9,}{ukupno_stopa:>9.2%}{f'{ukupno_trajanje // 60}:{ukupno_trajanje % 60:02d}':>10}")
print("=" * 60)

print(f"{'Najviše pregleda'}: {najvise_pregleda:,}")
print(f"Najkraći klip: {najkraci_klip} s")

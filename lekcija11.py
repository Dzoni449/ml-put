troskovi = []

while True:
    unos = input("Trošak (Enter = kraj): ").strip()
    if not unos:
        break
    troskovi.append(float(unos))

print(troskovi)

print(sum(troskovi))

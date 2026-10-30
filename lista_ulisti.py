ocene = [8, 10, 6, 9, 5, 10, 7]

zbir = 0
for i in ocene:
    zbir += i

najveci = 0
brojac = 0
prolazne = 0
for i in ocene:
    if najveci < i:
        najveci = i
    if i == 10:
        brojac+=1
    if i >= 6:
        prolazne += 1



print(f"Prosek: {zbir/len(ocene):.2f}")
print(f"Najveća ocena: {najveci}")
print(f"Broj desetki: {brojac}")
print(f"Prolaznih: {prolazne} od {len(ocene)}")

nova = []
for j in ocene:
    if j >= 6:
        nova.append(str(j))

ispis = ", ".join(nova)
print(f"Prolazne ocene: {ispis}")

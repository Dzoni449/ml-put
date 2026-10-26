pregledi = [48250, 1200, 15000, 3400]

ukupno = 0
for p in pregledi:
    ukupno += p


hitova = 0
for p in pregledi:
    if p > 10000:
        hitova+=1

mali = []

for p in pregledi:
    if p < 5000:
        mali.append(p)

najbolji = pregledi[0]

for p in pregledi:
    if p > najbolji:
        najbolji = p

print(ukupno,hitova,mali,najbolji)
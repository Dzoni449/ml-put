print("=== Unos pregleda ===")

lista = []
broj_klipa = 1



i = 0

while i <= len(lista):
    unos = input(f"Pregledi klipa {broj_klipa} (Enter = kraj): ").strip()
    
    if not unos:
        break

    if unos.isdigit():
        lista.append(int(unos))
        broj_klipa +=1 
        i += 1
    else:
        print(f"Preskačem: '{unos}' nije broj.")    
        
print()

if len(lista) == 0:
    print("=== Analiza klipova ===")
    print("Nema unetih klipova.")
else:
    suma = sum(lista)
    maximum = max(lista)
    minimum = min(lista)
    prosek = suma // len(lista)
    print("=== Analiza klipova ===")
    print(f"Broj klipova: {len(lista)}")
    print(f"Ukupno pregleda: {suma:,}")
    print(f"Prosek: {prosek:,}")
    print(f"Najviše: {maximum:,} (klip {lista.index(maximum) + 1})")
    print(f"Najmanje: {minimum:,} (klip {lista.index(minimum) + 1})")
    print("--- Svi klipovi ---")

    j = 0
    iznad_proseka = 0
    while j < len(lista):
        vrednost = lista[j]
        if vrednost > prosek:
            print(f"Klip {j+1}:{vrednost:>8,} (iznad proseka)")
            iznad_proseka+=1
        else:
            print(f"Klip {j+1}:{vrednost:>8,}")

        j += 1

    print(f"Iznad proseka: {iznad_proseka} od {len(lista)}")

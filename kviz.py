print("=== Python kviz ===")

pitanja = ["Šta vraća input()?", "Koliko je 7 // 2?", "Šta ispisuje print(len('Python'))?",
           "Kojom metodom se dodaje element na kraj liste?", "Koliko puta se izvrši: for i in range(1, 5)?"]
opcije = [["int", "str", "float", "bool"], ["3.5", "4", "3", "1"], ["5", "6", "7", "Greška"],
          ["add()", "insert()", "push()", "append()"], ["3", "4", "5", "6"]]
tacni = ["b", "c", "b", "d", "b"]
SLOVA = "abcd"
lista = []
brojac = 0
poeni = 0
for i in range(len(pitanja)):
    print()
    print(f"Pitanje {i+1}/{len(tacni)}: {pitanja[i]}")
    for j in range(len(opcije[i])):
        print(f"{SLOVA[j]}) {opcije[i][j]}")              
    unos = input("Tvoj odgovor: ").strip().lower() 
    while not (len(unos) == 1 and unos in "abcd"):
         print("Unesi a, b, c ili d.")
         unos = input("Tvoj odgovor: ").strip().lower()
    if unos == tacni[i]:
        print("Tačno! +10")
        brojac+=1
        poeni+=10

    elif unos != tacni[i]:
        indexiran = SLOVA.index(tacni[i])
        tekst = opcije[i][indexiran]
        lista.append(i+1)
        print(f"Netačno. Tačan odgovor: {SLOVA[indexiran]}) {tekst}")   



print()
print("=== Rezultat ===")

procenat = (brojac / len(tacni)) * 100

print(f"Tačnih: {brojac} od {len(tacni)} ({procenat:.0f}%)")
print(f"Poeni: {poeni}")

if procenat >= 80:
    print("Ocena: Odlično!")
elif procenat >= 60:
    print("Ocena: Dobro.")
elif procenat >= 40:
    print("Ocena: Može bolje.")
else:
    print("Ocena: Vreme je za ponavljanje.")

if len(lista) != 0:
    print(f"Ponovi pitanja: {', '.join(str(i) for i in lista)}")
else:
    print("Sve tačno, bravo!")

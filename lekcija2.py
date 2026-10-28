pitanja = ["Šta vraća input()?", "Koliko je 7 // 2?"]
opcije = [["int", "str", "float", "bool"], ["3.5", "4", "3", "1"]]

for i in range(len(pitanja)):            # spoljašnja: pitanje po pitanje
    print(pitanja[i])
    for opcija in opcije[i]:             # unutrašnja: opcije TOG pitanja
        print(f"  - {opcija}")
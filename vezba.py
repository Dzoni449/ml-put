p = input("Broj 1-6: ").strip()

ispravan = p.isdigit() and 1 <= int(p) <= 6


# T
# False
# false
# greska string u int
# false
#z1
klip = {"naslov": "Najbolji Python trik",
        "pregledi": 48250,
        "lajkovi": 2130}

#stopa = klip["lajkovi"] / klip["pregledi"]
#print(f"Naslov: {klip['naslov']}")
#print(f"Pregledi: {klip['pregledi']:,}")
#print(f"Stopa lajkova: {stopa:.2%}")
#z2

#klip["pregledi"] += 500
#klip["komentari"] = 87

#z3
#polje = input("Koje polje želiš da vidiš? ").strip().lower()

#if polje in klip:
    #print(f"{polje}: {klip[polje]}")
#else:
    #print(f"Nema polja {polje}.")

#z4
opisi = {5: "nedovoljan", 6: "dovoljan", 7: "dobar", 8: "vrlo dobar", 9: "odličan", 10: "odličan"}

ocena = input("Ocena: ")

if ocena.isdigit() and int(ocena) in opisi:
    print(f"Ocena {ocena} je: {opisi[int(ocena)]}")
else:
    print("Nepoznata ocena.")
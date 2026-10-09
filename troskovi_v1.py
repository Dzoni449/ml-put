ime = input("unesi ime: ")
prvi_trosak = float(input("Unesi prvi trosak: "))
drugi_trosak = int(input("Unesi drugi trosak: "))
treci_trosak = int(input("Unesi treci trosak: "))

ukupno = prvi_trosak + drugi_trosak + treci_trosak
prosecan = ukupno//3;

print(f"{ime}, ukupno si potrosio {ukupno} din. Prosecan trosak: '{prosecan}'")

print("Tvoje ime ima" + str(len(ime)))
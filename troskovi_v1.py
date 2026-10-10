ime = input("unesi ime: ")
prvi_trosak = float(input("Unesi prvi trosak: "))
drugi_trosak = float(input("Unesi drugi trosak: "))
treci_trosak = float(input("Unesi treci trosak: "))

ukupno = prvi_trosak + drugi_trosak + treci_trosak
prosecan = ukupno/3

print(f"{ime}, ukupno si potrosio {ukupno:.2f} din. Prosecan trosak: {prosecan:.2f} din")

print("Tvoje ime ima " + str(len(ime)) + " slova")
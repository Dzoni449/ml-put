naslov = input("Unesi naslov: ")
ociscen_naslov = naslov.replace("!!!","!").replace("#shorts","").strip().capitalize()
print("Ociscen naslov: " + ociscen_naslov)
print("Duzina: " + str(len(ociscen_naslov)) + " karaktera")
print("Broj reci: " + str(len(ociscen_naslov.split())))

print("Sadrži'python':", "python" in ociscen_naslov.lower())

print("Preview: " + ociscen_naslov[:20] + "...")

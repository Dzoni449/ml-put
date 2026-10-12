pregledi = int(input("Pregledi: "))
lajkovi = int(input("Lajkovi: "))
trajanje_klipa = int(input("Trajanje klipa (s): "))
prosecno_vreme_gledanja = float(input("Prosečno vreme gledanja (s): "))
naslov = input("Naslov: ")

stopa_lajkova = lajkovi / pregledi
dobro_zadrzavanje = prosecno_vreme_gledanja / trajanje_klipa;
naslov_dobre_duzine = naslov.strip()
ima_hashtag = "#" in naslov_dobre_duzine


dovoljno_pregleda = pregledi >= 10000
dobra_stopa_lajkova = stopa_lajkova >= 0.04
dobar_procenat_zadrzavanja = dobro_zadrzavanje >= 0.7
dobro_trajanje_klipa = trajanje_klipa <= 60
ukupan = dovoljno_pregleda + dobra_stopa_lajkova + dobar_procenat_zadrzavanja + dobro_trajanje_klipa

viralan = dovoljno_pregleda and (dobra_stopa_lajkova or dobar_procenat_zadrzavanja)
dobar_naslov = 10 <= len(naslov_dobre_duzine) <= 60

zlatniklip1 = ukupan == 4
zlatniklip2 = dovoljno_pregleda and dobra_stopa_lajkova and dobar_procenat_zadrzavanja and dobro_trajanje_klipa

print("=== Provera klipa ===")

print("Dovoljno pregleda (10,000+): ", dovoljno_pregleda)
print("Dobra stopa lajkova (4%+): ", dobra_stopa_lajkova)
print("Dobro zadržavanje (70%+): ", dobar_procenat_zadrzavanja)
print("Kratak klip (do 60 s): ", dobro_trajanje_klipa)
print("Naslov dobre dužine (10-60): ", dobar_naslov)
print("Ima hashtag: ", ima_hashtag)
print("Ispunjeno kriterijuma: " +  str(ukupan) + "/4")
print("Viralni kandidat: ", viralan)
print("Treba popraviti naslov: ", not dobar_naslov)
print("Zlatni klip1: ", zlatniklip1)
print("Zlatni klip2: ", zlatniklip2)
print("Oba se slazu: ", zlatniklip1 == zlatniklip2)


###########AAAAAAAAAAAAAAAAA###############
#1. 6,2,4
#2. 2,5
#3. 10
#4. [1,3,5]
#5.greska prazna brojevi treba samo brojevi.append(3)
#6. len =2 i 5
#7. *** dva reda po 3*
#   *** 
#8.a,b,c ce da ispise bez zagrada
#9. 6
#10.greska
########################BBBBBBBBBBBBBB#############
#brojevi = [4, 7, 2, 9]
#najveci = brojevi[0]
#for b in brojevi:
    #if b > najveci:
        #najveci = b
#print(najveci)
# na pocetku imamo niz brojevi i najveci koji je 4 jer uzima vrednost iz niza
# for b in brojevi: uzima index po index tj b ce biti njegova vrednost na pocetku je 4
# if b > najveci je uslov i ukoliko je tacan dodeljujemo najvecem njegovu vrednost
# print se izvrsava na kraju kada se ceo niz brojevi prodje 
# dakle na pocetku imam 4 > 4 jednak je pa najveci ostaje 4
# pa idemo na sleci u nizu dakle 7 > 4 sto je true najveci postaje 7
# pa idemo na sledeci u nizu dakle 2 > 7 sto je false znaci nista se ne desava
# pa idemo na sledeci u nizu dakle 9 >7 sto je true najveci je 9
# i tek onda se ispisuje
###################ccccccccccccccccccc#########
#igraci = ["Ana", "Ivan"]
#poeni = [[3, 5], [10, 2, 1]]


#for i in range(len(igraci)):
    #ukupno = 0
    #for p in range(len(poeni[i])):
        #ukupno += poeni[i][p]
    #print(f"{igraci[i]}: {ukupno}")

#najbolji = []
#najbolji.append("Ivan")
#print(najbolji)

# prvi bug je prvi for ne treba + 1 len vraca 2 
# drugi bag je da u drugom for-u nedostaje len i range i takodje ukupno mora da se ubaci u for inace se za ivana racuna sve bice 21
# najbolji = najbolji.append("ivan") postaje prazno treba samo najbolji.append("ivan")
########################ddddddddddd##################
#ocene = [8, 10, 6, 9, 5, 10, 7]

#zbir = 0
#for i in ocene:
    #zbir += i

#najveci = 0
#brojac = 0
#prolazne = 0
#for i in ocene:
    #if najveci < i:
        #najveci = i
    #if i == 10:
        #brojac+=1
    #if i >= 6:
        #prolazne += 1



#print(f"Prosek: {zbir/len(ocene):.2f}")
#print(f"Najveća ocena: {najveci}")
#print(f"Broj desetki: {brojac}")
#print(f"Prolaznih: {prolazne} od {len(ocene)}")

#nova = []

#for j in ocene:
    #nova.append(str(j))

#ispis = ", ".join(nova)
#print(ispis)

#################d2d2d2d2###################

print("=== Korpa ===")
namirnice = []
lista_cena = []

while True:
    unos = input("Artikal (Enter = kraj): ").strip()

    if not unos:
        break
    else:
        namirnice.append(unos)

    unos_cene = input("Cena (din): ")

    while not unos_cene.isdigit():
        print("Cena mora biti ceo broj.")
        unos_cene = input("Cena (din): ")
    lista_cena.append(unos_cene)


print()


if len(namirnice) == 0:
    print("Korpa je prazna.")
else:

    suma = 0
    print("=== Račun ===")
    for i in range(len(namirnice)):
        suma += int(lista_cena[i])
        print(f"{i+1}. {(namirnice[i]):<14} {int(lista_cena[i]):>6,} din")
    print(f"Ukupno: {suma:>16,} din")


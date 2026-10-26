# 1. ispisace A pa B
# 2. SAmo A
# 3. "10+100+"
# 4. da ce da ispise
# 5. nece imati lep ispis ima da se prekine na prihvaceno, mora da bude
# if o == "da" or o == "d"
#6 ima
#7 " 12" nije digit dok "12" jeste false
#8  True
#9 true
#10 C samo ispise
#--------------------------------------------------------------------
    #2 zad

poeni = input("Poeni (0-100): ")




if poeni.isdigit():
    poeni = int(poeni)
    ocena = 0;

    if poeni >= 50 and poeni <= 60:
        ocena = 6
    elif  poeni >= 60 and poeni <= 70:
        ocena = 7
    elif poeni >= 70 and poeni <= 80:
        ocena = 8
    elif poeni >= 80 and poeni <= 90:
        ocena = 9
    elif poeni >= 90 and poeni <= 100:
        ocena = 10
    elif poeni >= 0 and poeni < 50:
        ocena = 5
    else:
        print("Pogresan unos!")



    polozio = ocena > 5
    if polozio == True:
        print(f"Ocena: {ocena}, položio!")

else:
    print("mora da se unese broj ne moze string")




# prvi bag je da fali : kod else
# drugi bag je da print nije uvuceno kod poslednjeg ifa
# treci bug koji sam nasao je da su lose granice za ocene
# cetvrti bug je da nemamo ocenu 7 pa moze recimo kada imamo 65poena da napise ocena 5 samo dodamo granice za 7
# ubacio sam proveri za string da kada se unesi string bude tekst greska

#--------------------------------------------------------------------
#snooker.txt
#Helyezes;Nev;Orszag;Nyeremeny
#   0       1   2       3
#52;Akani Sunny;Thaiföld;118500

# file beolvas, fejlec egysor mátrixba többit belepakolni, feladatok!!!
# sor for sor in
with open('snooker.txt','r', encoding 'latin2') as f:
    fejlec = f.readline
    matrix = [ sor.strip().split(';') sor for sor in f ]
    # soronként végigmegyünk a file on, megstrippeljük a '\n' től, és a ';' mentén szét splitteljük igy mátrix lesz


# hány versenző van a kistán (len(matrix))
print(f'3.feladat: A világranglistán {len(matrix)} versenyző szerepel')

# versenyzők átlagos bevétele
bevetelek = [int(sor[3]) for sor in matrix]
print(f'4. feladat : a versenyzők átlagosan {sum(bevetelek)/len(matrix)} kerestek')

# kinaiak

kinaiak = [(int(nyeremeny),helyezes, nev, orszag) for helyezes, nev, orszag, nyeremeny in matrix if sor[2]== 'Kína']
nyeremeny, helyezes, nev, orszag = max(kinaiak)#megkeresi a maxot)

print(f'5. feladat: a legjobban kereső kinai: ')
print(f'    Helyezés: {helyezes}')
print(f'    Név: {nev}')
print(f'    Ország: {orszag}')
print(f'    Nyeremény összege: {nyeremeny*380} Ft')

#norvegok
norvegok = [ nev for helyezes, nev, orszag, nyeremeny in matrix if orszag == 'Norvégia']
# eleg a neve mert a darab kell a tobbi nem számít
print(f'6. feladat')
if len(norvegok)>0:
    print("van norvég")
else:
    print("nincs norvég")


# orszagok ahol tobb mint 4 versenyzo van : orszag neve és indulok száma
# SZÓTÁR

orszagok = {orszag : 0 for helyezes, nev, orszag, nyeremeny in matrix}

for helyezes, nev, orszag, nyeremeny in matrix :
    orszagok[orszag] +=1
    # ha van valamiből 1 akkor egyel megnöveljük a számát
    # megkapjuk az országok listáját az inditottak számával

print(f' 7. feladat statisztika:')
for orszag, vsz in orszagok.items():
    if vsz>4:
        print(f'    {orszag} - {vsz} fő')


#           HARMADIK FELADATTÓL 17 PERC

"""
#Generátor uživatelského jména
#Zadání:
#Uživatel zadá jméno a příjmení.
#Vytvoř username takto:
#první 3 písmena jména
#první 3 písmena příjmení
#vše malými písmeny
#Pokud je jméno kratší než 3 znaky, vezmi celé.

jmeno = input("Zadej své jméno.")
prijmeni = input("Zadej své příjmení.")
#print(jmeno[:3])
#print(prijmeni[:3])
uzivatelske_jmeno = jmeno[:3] + prijmeni[:3]
print(uzivatelske_jmeno.lower())
"""

#Kontrola hesla 🔐
#Pravidla:
#Heslo musí:
#mít alespoň 8 znaků
#obsahovat číslo
#obsahovat velké písmeno
#Použij:
#len()
#"0" in heslo atd.
#upper() nebo porovnání znaků

#heslo = input("Heslo musí mít alespoň 8 znaků. Zadej delší heslo. ")
#heslo = input("Heslo musí obsahovat číslo. Zadej jiné heslo. ")



ma_aspon_8_znaku = False
obsahuje_cislo = False
obsahuje_velke_pismeno = False
heslo_je_platne = False
while heslo_je_platne == False:
    heslo = input("Zadej heslo. ")
    if len(heslo) >= 8:
        ma_aspon_8_znaku = True
    else:
        print("Heslo musí mít alespoň 8 znaků.")
    for znak in heslo:
        if znak.isdigit() == True:
            obsahuje_cislo = True
            break
        else:
            print("Heslo musí obsahovat číslo.")
            break
    for znak in heslo:
        if znak.isupper() == True:
            obsahuje_velke_pismeno = True
            break
        else:
            print("Heslo musí obsahovat velké písmeno.")
            break
    if ma_aspon_8_znaku == True and obsahuje_cislo == True and obsahuje_velke_pismeno == True:
        heslo_je_platne = True
    #else:
        #heslo = input("Zadej jiné heslo. ")
else:
    print("Heslo je platné.")


"""
#POČÍTÁNÍ SUROVIN PRO VĚTŠÍ DORTOVOU FORMU
#Chci, aby se vypsalo několik řádků a na každém řádku aby se vypsala surovina a zároveň se propočítalo její množství
do receptu s větší dortovou formou.
sablona = {surovina}, {původní množství} * 1.5625
print(sablona.format(původní množství=140, surovina='dětské sušenky'))
print(sablona.format(původní množství=40, surovina='ovesné vločky'))
print(sablona.format(původní množství=90, surovina='kvalitní máslo'))
print(sablona.format(původní množství=3, surovina='menší banány'))
print(sablona.format(původní množství=2, surovina='vajíčka'))
print(sablona.format(původní množství=250, surovina='ricotta'))
print(sablona.format(původní množství=100, surovina='jogurt'))
print(sablona.format(původní množství=10, surovina='vanilkový puding'))

#počítání surovin po jednom
puvodni_mnozstvi = 10
print(1.5625 * puvodni_mnozstvi)
"""

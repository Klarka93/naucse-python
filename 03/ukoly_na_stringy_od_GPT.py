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

def at_least_8(heslo):
    if len(heslo) >= 8:
        return True

    print("Heslo musí mít alespoň 8 znaků.")
    return False


def has_number(heslo):
    for znak in heslo:
        if znak.isdigit():
            return True

    print("Heslo musí obsahovat číslo.")
    return False


def has_capital(heslo):
    for znak in heslo:
        if znak.isupper():
            return True

    print("Heslo musí obsahovat velké písmeno.")
    return False


def valid_password(heslo):
    return at_least_8(heslo) and has_number(heslo) and has_capital(heslo)

"""
heslo_je_platne = False
while not heslo_je_platne:
    heslo = input("Zadej heslo. ")
    heslo_je_platne = valid_password(heslo)
else:
    print("Heslo je platné.")
"""

assert not valid_password("Abcdefgh")
assert not valid_password("1bcdefgh")
assert not valid_password("1bcd")
assert valid_password("1bcdAbcd")
assert not valid_password("")
assert not valid_password("@bcdAbcd")

"""
#POČÍTÁNÍ SUROVIN PRO VĚTŠÍ DORTOVOU FORMU
#Chci, aby se vypsalo několik řádků a na každém řádku aby se vypsala surovina a zároveň se propočítalo její množství
#do receptu s větší dortovou formou.
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
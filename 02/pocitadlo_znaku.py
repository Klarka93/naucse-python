
"""
odpoved = input('Jak se jmenuješ?')
len(odpoved)
print("Tvoje jméno má", len(odpoved), "znaků.")
if len(odpoved) > 7:
    input("Tvoje jméno je dost dlouhé. Nemáš kratší přezdívku?")
print("Těší me!")
"""
"""
cislo = int(input("Jaké číslo chceš vynásobit?"))
for i in range(11):
    print(i, "x", cislo, "=", i * cislo)
"""
"""
from random import randrange
cislo = randrange(1,1000)
odpoved = int(input("Myslím si číslo od jedné do tisíce. Hádej, jaké to je?"))
while odpoved != cislo:
    if odpoved > cislo:
        odpoved = int(input("Moc velké. Hádej dál!"))
    elif odpoved < cislo:
        odpoved = int(input("Moc malé. Hádej dál!"))
else:
    print("Uhádl jsi!")
"""
"""
heslo = "jednorozec"
pokusy = 0
while pokusy < 3:
    odpoved = input("Zadej heslo.")
    if heslo == odpoved:
        print("Přihlášeno.")
        break
    else:
        pokusy = pokusy + 1
        print("Nesprávné heslo.")
if pokusy == 3:
    print("Přístup zablokován.")
"""
from random import randrange
cislo1 = randrange(0, 10)
#cislo2 = randrange(0, 10)
cislo2 = 6
operace = "/"
"""
operace = ["+", "-", "*", "/"]
index = randrange(0,4)
operace = operace[index]
"""
"""
if operace == "+":
    print(f"{cislo1} + {cislo2} = {cislo1 + cislo2}")
elif operace == "-":
    print(f"{cislo1} - {cislo2} = {cislo1 - cislo2}")
elif operace == "*":
    print(f"{cislo1} * {cislo2} = {cislo1 * cislo2}")
elif operace == "/" and cislo2 == 0:
    cislo2 = randrange(0, 10)
    print(f"{cislo1} / {cislo2} = {cislo1 / cislo2}")
elif operace == "/":
    while cislo1 % cislo2 != 0:
        cislo1 = randrange(0, 10)
    else:
        print(f"{cislo1} / {cislo2} = {cislo1 / cislo2}")
"""
#GENERÁTOR PŘÍKLADŮ
#Vylosuj dvě čísla
#Zeptej se na výsledek (např. sčítání)
#Vyhodnoť správnost
#Opakuj třeba 5×
#Na konci vypiš skóre

"""
from random import randrange
spravne = 0
spravne_vysledky = []
for i in range(5):
    cislo1 = randrange(0, 10)
    cislo2 = randrange(0, 10)
    odpoved = int(input(f"{cislo1} + {cislo2} = "))
    if odpoved == cislo1 + cislo2:
        spravne = spravne + 1
    spravne_vysledky.append(f"{cislo1 + cislo2}")
print(f"Spravne = {spravne}. Spravne vysledky = {spravne_vysledky}")
"""
#STATISTIKA ČÍSEL
#Uživatel zadává čísla jedno po druhém
#Zadávání skončí, když napíše „konec“
#Program vypíše:
#kolik čísel zadal
#součet
#průměr
seznam_cisel = []
soucet = 0
odpoved = input("Zadej číslo. Až budeš chtít skončit, napiš 'konec'.")
while odpoved != "konec":
    seznam_cisel.append(odpoved)
    soucet = soucet + int(odpoved)
    odpoved = input("Zadej číslo. Až budeš chtít skončit, napiš 'konec'.")
print("Zadal jsi", len(seznam_cisel), "čísel.")
print("Součet čísel je", soucet)
print("Průměr je", soucet / len(seznam_cisel))
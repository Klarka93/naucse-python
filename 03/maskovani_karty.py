#Maskování karty 💳
#Uživatel zadá číslo karty (např. 1234567812345678)
#Program má vypsat:
#************5678

"""
#Kód z Wishe :-P
#Předpokládá 16místné číslo karty, takže vrátí vždy 12 hvězdiček a poslední 4 číslice.
cislo_karty = input("Zadej číslo svojí platební karty. ")
print("**** **** ****", cislo_karty[-4:])

"""

"""
#O chlup lepší kód
#Vypíše poslední 4 číslice z libovolně dlouhého čísla a zbytek vyhvězdičkuje.
cislo_karty = input("Zadej číslo svojí platební karty. ")
pocet_hvezdicek = len(cislo_karty) - 4
print(pocet_hvezdicek * "*", end="")
print(cislo_karty[-4:])

"""

"""
#Řešení pomocí definice vlastní funkce
#Funkce si uloží do listu počet hvezdiček a poslední 4 čísla. Kód pak vypíše hodnotu funkce.
def maskovana_karta(cislo_karty):
    maskovane_cislo = []
    maskovane_cislo.append((len(cislo_karty) - 4) * "*")
    maskovane_cislo.append(cislo_karty[-4:])
    return ''.join(maskovane_cislo)

cislo_karty = input("Zadej číslo svojí platební karty. ")
print(maskovana_karta(cislo_karty))
"""
"""
def maskovana_karta(cislo_karty):
    maskovane_cislo = "*" * (len(cislo_karty) - 4)
    maskovane_cislo += cislo_karty[-4:]
    return maskovane_cislo

print(maskovana_karta("4890123456781234"))
print(maskovana_karta("489012345678"))

print("489012345678"[::2])

text = "489012345678"
skupiny = []
for i in range(0, len(text), 4):
    skupiny.append(text[i:i + 4])
print(":".join(skupiny))
"""
#Nejrafinovanější řešení
#PC si vezme číslo karty, 75% zahvězdičkuje a posledních 25% číslic zobrazí
"""
def maskovana_karta(cislo_karty):
    pocet_hvezdicek = round(len(cislo_karty) * 0.75)
    pocet_cislic = len(cislo_karty) - pocet_hvezdicek
    maskovane_cislo = []
    maskovane_cislo.append(pocet_hvezdicek * "*")
    maskovane_cislo.append(cislo_karty[-pocet_cislic:])
    return ''.join(maskovane_cislo)

cislo_karty = input("Zadej číslo svojí platební karty. ")
print(maskovana_karta(cislo_karty))

"""

#Můžu dát počítači podmínku, aby akceptival jen řetězce dělitelné 4.
#Můžu zkusit nastavit, aby počítač po každé sérii číslic vkládal v printu mezeru.




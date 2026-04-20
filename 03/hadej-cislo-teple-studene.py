#Hádej číslo – teplé / studené
#Počítač si vylosuje číslo (1–100)
#Uživatel hádá
#Program říká:
#🔥 „Hodně blízko“ (rozdíl ≤ 3)
#🙂 „Blízko“ (≤ 10)
#❄️ „Daleko“ (> 10)
#Po uhodnutí:
#vypiš počet pokusů
#nabídni novou hru

from random import randrange
pocet_pokusu = 0
chce_pokracovat = "ano"

while chce_pokracovat == "ano":
    cislo = randrange(1, 100)
    odpoved = int(input("Hádej, jaké číslo od 1 do 100 si myslím? "))
    while odpoved != cislo:
        if abs(odpoved - cislo) <= 3:
            print("Hodně blízko!")
        elif abs(odpoved - cislo) <= 10:
            print("Blízko.")
        elif abs(odpoved - cislo) > 10:
            print("Daleko.")
        pocet_pokusu = pocet_pokusu + 1
        odpoved = int(input("Hádej dál. "))
    else:
        print(f"Uhádl jsi! Tvůj počet pokusů je {pocet_pokusu}.")
        pocet_pokusu = 0
        chce_pokracovat = input("Chceš hrát znovu? ")
else:
    print("Děkuji za hru.")

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
cislo = randrange(1,100)
chce_pokracovat = "ano"
while chce_pokracovat == "ano":
    odpoved = int(input("Hádej, jaké si myslím číslo?"))
    if odpoved - cislo == ≤ 3:
        print("Hodně blízko!")
    elif odpoved - cislo == ≤ 10:
        print("Blízko.")
    elif odpoved - cislo == > 10:
        print("Daleko.")
    pocet_pokusu = pocet_pokusu + 1
    odpoved = int(input("Hádej dál."))
    elif odpoved == cislo:
        print("Uhádl jsi!")

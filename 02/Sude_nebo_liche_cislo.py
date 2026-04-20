from random import randrange
cislo = randrange(10)
print(cislo)
if cislo % 2 == 0 and cislo != 0:
    print("Číslo je sudé.")
elif cislo % 2 == 1:
    print("Číslo je liché.")
elif cislo == 0:
    print("Číslo je 0.")
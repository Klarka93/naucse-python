#Kostková hra (hráč vs. počítač)
#Pravidla:
#Hráč i počítač hodí kostkou (1–6)
#Vyšší číslo vyhrává
#Při shodě → remíza
#Po každém kole:
#zeptej se, jestli chce pokračovat
#Po skončení:
#vypiš celkové skóre

from random import randrange
skore_hrac = 0
skore_PC = 0
chce_pokracovat = 'ano'
print('Zahrajeme si kostky. Vyšší číslo vyhrává.')
while chce_pokracovat == "ano":
    hrac = randrange(1, 7)
    PC = randrange(1, 7)
    print(f'Hráč: {hrac}, PC: {PC}')
    if hrac > PC:
        skore_hrac += 1
        chce_pokracovat = input('Hráč vyhrává. Chceš pokračovat? ')
    elif hrac < PC:
        skore_PC += 1
        chce_pokracovat = input('PC vyhrává. Chceš pokračovat? ')
    elif hrac == PC:
        chce_pokracovat = input('Remíza.Chceš pokračovat? ')
else:
    print(f'Děkuji za hru. Tvoje celkové skóre je {skore_hrac}. Celkové skóre PC je {skore_PC}.')


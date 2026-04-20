# Hra Oko bere: Po každém kole se hráči přičte náhodný počet bodů a on se musí rozhodnout, jestli chce pokračovat.
# Cílem je získat co nejvíc bodů, ale nepřesáhnout 21.
celkem_bodu = 0
print('Zahraj si se mnou Oko bere!')
odpoved = input('Chceš pokračovat?')
#while odpoved == 'ano':
#while odpoved == 'ano' or odpoved == 'Ano':

while odpoved.lower() == 'ano':
    from random import randrange
    cislo = randrange(2, 11)
    print('Získáváš', cislo, 'bodů')
    celkem_bodu = celkem_bodu + cislo
    print('Celkem máš',celkem_bodu, 'bodů.')
    if celkem_bodu > 21:
        print('Přesáhl jsi 21 bodů. Prohrál jsi!')
        break
    elif celkem_bodu == 21:
        print('Gratuluji! Vyhrál jsi!')
        break
    odpoved = input('Chceš pokračovat?')
else:
    print('Konec hry. Získal jsi' , celkem_bodu, 'bodů.')


# strana = float(input('Zadej stranu čtverce v centimetrech: '))
# cislo_je_spravne = strana > 0
# if cislo_je_spravne:
    # print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    # print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
# else:
    # print('Strana musí být kladná, jinak z toho nebude čtverec!')

# print('Děkujeme za použití geometrické kalkulačky.')
#####
# cislo = int(input('Zadej číslo, přičtu k němu 3: '))
# if cislo == 0:
    # print('Jé, to je jednoduché!')
# print(f'{cislo} + 3 = {cislo + 3}')
#####
"""
vek = int(input('Kolik ti je let? '))
if vek >= 150:
    print('A ze kterépak jsi planety?')
elif vek >= 18:
    # Tahle větev se např. pro "200" už neprovede.
    print('Můžeme nabídnout: víno, cider, nebo vodku.')
elif vek >= 1:
    print('Můžeme nabídnout: mléko, čaj, nebo vodu')
elif vek >= 0:
    print('Sunar už bohužel došel.')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Pro návštěvy z budoucnosti bohužel nemáme nic v nabídce.')
#####
"""
from requests.utils import select_proxy

"""
stastna = input('Jsi šťastná?')
if stastna == 'ano':
    # Tenhle kus kódu se provede, když je "šťastná"
    bohata = input('Jsi bohatá?')
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus míň utrácet.')
elif stastna == 'ne':
    bohata = input('Jsi bohatá?')
    # Tenhle kus kódu se provede, když není "šťastná"
    if bohata == 'ano':
        print('Zkus se víc usmívat!')
    else:
        print('To je mi líto.')
else:
    print('Co to meleš? Řekni ano nebo ne!')
"""
"""
# Tento program rozdává nejapné rady do života.

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano' or stastna_retezec == 'Ano':
    stastna = True
elif stastna_retezec == 'ne' or stastna_retezec == 'Ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano' or bohata_retezec == 'Ano':
    bohata = True
elif bohata_retezec == 'ne' or bohata_retezec == 'Ne':
    bohata = False
else:
    print('Nerozumím!')

if bohata and stastna:
    # Je bohatá a zároveň štǎstná, ta se má.
    print('Gratuluji!')
elif bohata:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')
"""
"""
barva = input('Jaká je tvoje oblíbená barva?')
if barva == 'červená':
    print('Jako jahody!')
elif barva == 'modrá':
    print('Jako obloha!')
elif barva == 'žlutá':
    print('Jako sluníčko!')
elif barva == 'zelená':
    print('Jako tráva.')
else:
    print('Takovou barvu neznám.')
"""
"""
zvíře = input('Jaké je tvoje oblíbené zvíře?')
if zvíře == 'pes':
    print('Haf! Haf!')
elif zvíře == 'kočka':
    print('Mňau! Mňau!')
elif zvíře == 'kůň':
    print('íhaha!')
elif zvíře == 'krokodýl':
    print('Chramst!')
else:
    print('Takové zvíře neznám.')
"""

"""
mas_kocku_retezec = input('Máš kočku?')
if mas_kocku_retezec == 'ano' or mas_kocku_retezec == 'Ano':
    kocka = True
elif mas_kocku_retezec == 'ne' or mas_kocku_retezec == 'Ne':
    kocka = False
else:
    print('Nerozumím!')
mas_psa_retezec = input('Máš psa?')
if mas_psa_retezec == 'ano' or mas_psa_retezec == 'Ano':
    pes = True
elif mas_psa_retezec == 'ne'or mas_psa_retezec == 'Ne':
    pes = False
else:
    print('Nerozumím!')
if kocka and pes:
    print('Gratuluji, máš kočku i psa!')
elif kocka or pes:
    print('Máš buď kočku nebo psa.')
else:
    print('Nemáš ani kočku ani psa.')
"""
from random import randrange

cislo = randrange(0, 3)  # číslo je 0, 1, nebo 2
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:  # tady musí být číslo 2
    print('Trojúhelníček')

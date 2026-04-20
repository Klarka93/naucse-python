#Lhář nebo pravda (ano/ne)
#Zadání:
#Program si náhodně vybere:
#pravda
#lež
#Položí otázku (např. „Python je had. Ano/Ne?“)
#Pokud:
#odpověď odpovídá realitě → bod
#Po 5 otázkách vypiš skóre
#Trénuje podmínky a práci s textem

otazky_ano = [
    'Mozek spotřebuje asi 20 % energie těla.',
    'Chobotnice mají tři srdce.',
    'Na planetě Venuše je den delší než rok.',
    'Med je při správném skladování jedlý i po 1000 letech.',
    'Žirafy mají stejný počet krčních obratlů jako lidé.']

otazky_ne = [
    'Tučňáci žijí na severním pólu.',
    'Slunce je největší hvězda ve vesmíru.',
    'Sloni neumí plavat.',
    'Eiffel Tower stojí v Londýně.',
    'Mořská voda není slaná.',
    'Netopýři jsou slepí.',
    'Rajče je zelenina.']

from random import randrange
from random import choice
skore = 0
print('Dám ti 5 otázek ano/ne. Za každou správnou odpověď získáš 1 bod a za každou chybnou jeden ztratíš.')
for i in range(5):
    otazky = randrange(0,2)
    if otazky == 0:
        index = randrange(0, len(otazky_ano))
        print(otazky_ano[index], end="")
        otazky_ano.pop(index)
        #print(choice(otazky_ano), end="")

    elif otazky == 1:
        index = randrange(0, len(otazky_ne))
        print(otazky_ne[index], end="")
        otazky_ne.pop(index)
        #print(choice(otazky_ne), end="")
    odpoved = input(' Ano nebo ne? ')
    if otazky == 0 and odpoved == 'ano'or otazky == 1 and odpoved == 'ne':
        skore += 1
        print(f'Správně!Tvoje skóre je {skore}/5')
    elif otazky == 0 and odpoved == 'ne' or otazky == 1 and odpoved == 'ano':
        skore -= 1
        print(f'Špatně.Tvoje skóre je {skore}/5')

print(f'Tvoje celkové skóre je {skore}/5')






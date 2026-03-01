#POČÍTÁNÍ SUROVIN PRO VĚTŠÍ DORTOVOU FORMU
#Chci, aby se vypsalo několik řádků a na každém řádku aby se vypsala surovina a zároveň se propočítalo její množství
#do receptu s větší dortovou formou.

puvodni_mnozstvi = {
    'dětské sušenky': 140,
    'ovesné vločky' : 40,
    'kvalitní máslo' : 90,
    'menší banány' : 3,
    'vajíčka' : 2,
    'ricotta' : 250,
    'jogurt' : 100,
    'vanilkový puding' : 10}

sablona = '{surovina} {gramaz}'
for surovina, gramaz in puvodni_mnozstvi.items():
    print(sablona.format(surovina=surovina, gramaz=round(gramaz * 1.5625)))

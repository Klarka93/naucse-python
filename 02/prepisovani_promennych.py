"""
celkem = 0

for delka_trasy in 8, 45, 9, 21:
    print('Jdu', delka_trasy, 'km do další vesnice.')
    celkem = celkem + delka_trasy

print('Celkem jsem ušla', celkem,'km')
"""
"""
odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')
"""
"""
while True:
    odpoved = input('Řekni Ááá! ')
    if odpoved == 'Ááá':
        print('Bééé')
        break
    print('Špatně, zkus to znovu')

print('Hotovo, ani to nebolelo.')
"""
"""
for i in range(10):  # Vnější cyklus
    for j in range(10):  # Vnitřní cyklus
        print(j * i, end=' ')
        if i <= j:
            break
    print()
"""
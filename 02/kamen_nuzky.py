from random import randrange

prvky = ['kámen', 'nůžky', 'papír']

def spocitej_vyhru(cislo, odpoved):
    if prvky[cislo] == "kámen" and odpoved == "nůžky":
        print("Kámen tupí nůžky. Vyhrál jsem!")
    elif prvky[cislo] == "kámen" and odpoved == "papír":
        print("Papír balí kámen. Vyhráváš!")
    if prvky[cislo] == "nůžky" and odpoved == "kámen":
        print("Kámen tupí nůžky. Vyhráváš!")
    elif prvky[cislo] == "nůžky" and odpoved == "papír":
        print("Nůžky stříhají papír. Vyhrál jsem!")
    if prvky[cislo] == "papír" and odpoved == "kámen":
        print("Papír balí kámen. Vyhrál jsem!")
    elif prvky[cislo] == "papír" and odpoved == "nůžky":
        print("Nůžky stříhají papír. Vyhráváš!")

print('Zahrajeme si Kámen, nůžky, papír.')
chce_hrat = "ano"
while chce_hrat == 'Ano' or chce_hrat == 'ano':
    for i in range(3):
        cislo = randrange(0, 3)
        odpoved = input('Co dáváš? Kámen, nůžky nebo papír?')
        print(f"PC: {prvky[cislo]}")

        if prvky[cislo] == odpoved:
            print("Remíza.")
        spocitej_vyhru(cislo, odpoved)

        if odpoved != 'kámen' and odpoved != 'nůžky' and odpoved != 'papír':
            print('Nerozumím.')
            continue

    chce_hrat = input("Chceš pokračovat?")
else:
    print('Děkuji za hru.')


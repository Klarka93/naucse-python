def precti_zaznamy():
    vysky = []
    with open("zaznamy.txt", "r") as f:
        zaznamy = f.read()

    for student in zaznamy:
        vysky.append(student['vyska'])

    return vysky

try:
    precti_zaznamy()
except FileNotFoundError:
    print("Soubor zaznamy.txt neexistuje")


vstup = "3"
print(int(vstup))
vstup = "abc"
print(int(vstup))

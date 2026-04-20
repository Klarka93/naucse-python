#Palindrom 🔁
#Zjisti, zda je slovo palindrom (čte se stejně zepředu i zezadu).
#Např:
#radar → ano
#python → ne


slovo = input('Napiš slovo. ')
slovo_pozpatku = slovo[::-1]
if slovo == slovo_pozpatku:
    print('Slovo je palindrom.')
else:
    print('Slovo není palindrom.')

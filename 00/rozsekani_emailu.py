#Rozsekání e-mailu 📧
#Uživatel zadá email.
#Program:
#zjistí, zda obsahuje "@"
#pokud ano:
#vypíše část před @
#vypíše doménu za @
#pokud ne:
#vypíše „Neplatný email“


"""
#Můj výsledný kód.
email = input('Zadej email. ')
pozice = email.find("@")
if '@' in email:
    print('uživatel:', email[:pozice])
    print('doména:', email[pozice+1:])
else:
    print('Neplatný email.')

"""
#Vylepšení od GPT
email = input("Zadej email: ")
pozice = email.find("@")

if pozice == -1:
    print("Neplatný email.")
else:
    print("uživatel:", email[:pozice])
    print("doména:", email[pozice+1:])
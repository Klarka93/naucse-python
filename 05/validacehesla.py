heslo = input("Napiš heslo. ")
if len(heslo) <= 6:
    print("Heslo je příliš krátké.")
elif " " in heslo:
    print("Heslo nesmí obsahovat mezeru.")
else:
    print("Heslo je v pořádku.")
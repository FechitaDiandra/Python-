def este_palindrom(numar):
    # din nr in sir carac
    numar_str = str(numar)
    # daca nr = inv
    return numar_str == numar_str[::-1]


numar_utilizator = input("Introdu un număr: ")

if este_palindrom(numar_utilizator):
    print(f"Numărul {numar_utilizator} este un palindrom.")
else:
    print(f"Numărul {numar_utilizator} nu este un palindrom.")

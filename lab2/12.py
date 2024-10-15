def este_palindrom(numar):
    if numar < 0:
        return False
    
    numar_inversat = 0
    original = numar

    while numar > 0:
        ultima_cifra = numar % 10
        numar_inversat = numar_inversat * 10 + ultima_cifra
        numar //= 10

    return numar_inversat == original

numar = 12321
if este_palindrom(numar):
    print(f"{numar} este palindrom.")
else:
    print(f"{numar} nu este palindrom.")

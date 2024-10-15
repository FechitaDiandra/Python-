def numara_biti_1(numar):
    # conversia nr in format binar si nr bitilor de 1
    return bin(numar).count('1')


numar_utilizator = int(input("Introdu un număr: "))

biti_1 = numara_biti_1(numar_utilizator)

print(f"Numărul {numar_utilizator} are {biti_1} biți cu valoarea 1.")

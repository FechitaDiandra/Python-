
def gcd_doua_numere(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def gaseste_gcd(numere):
    gcd = numere[0]
    
    for i in range(1, len(numere)):
        gcd = gcd_doua_numere(gcd, numere[i]) 
    return gcd

input_numere = input("Introdu numerele separate prin spații: ")

numere = list(map(int, input_numere.split()))


gcd_rezultat = gaseste_gcd(numere)

print("Cel mai mare divizor comun al numerelor este:", gcd_rezultat)

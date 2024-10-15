from math import factorial

def permutare_alfabet(alfabet, index, lungime):
    cuvant = []
    n = len(alfabet)
    
    for i in range(lungime):
        fact = factorial(n - 1 - i)
        
        pozitie = index // fact
        cuvant.append(alfabet[pozitie])
        
       
        index %= fact
       
        alfabet = alfabet[:pozitie] + alfabet[pozitie + 1:]
    
    return ''.join(cuvant)


alfabet = "AEGIJLNOPSUVbdefhimnoprstuvwxy"
index = 218553019
lungime = 6


cuvant = permutare_alfabet(alfabet, index, lungime)
print(f"Cuvantul corespunzător indexului {index} este: {cuvant}")

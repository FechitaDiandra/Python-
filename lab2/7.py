def numara_majuscule(propozitie):
    numar_majuscule = 0
    for char in propozitie:
        
        if char.isupper():
            numar_majuscule += 1
    
    return numar_majuscule


rezultat = numara_majuscule("A fost, de asemenea, Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele-state Grecesti.")
print(f"Numarul de caractere scrise cu majuscula este: {rezultat}")

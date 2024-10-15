def inverseaza_cuvinte(propozitie):
    cuvinte = propozitie.split()
    
    cuvinte_inversate = cuvinte[::-1]
    
    propozitie_inversata = ' '.join(cuvinte_inversate)
    
    return propozitie_inversata

propozitie_inversata = inverseaza_cuvinte("Maricica merge la nunta fiicei sale")
print(propozitie_inversata)

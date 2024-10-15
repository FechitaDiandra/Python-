def afiseaza_hex_cuvinte(propozitie):
    cuvinte = propozitie.split()
    for cuvant in cuvinte:
        hex_repr = ''.join(format(ord(char), '02x') for char in cuvant)
        print(hex_repr)


afiseaza_hex_cuvinte("bda 102")

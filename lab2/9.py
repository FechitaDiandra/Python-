def extrage_prima_ultimul_caracter(propozitie):
    cuvinte = propozitie.split()
    
    rezultat = []
    
    for cuvant in cuvinte:
        if cuvant:  
            primul_caracter = cuvant[0]  
            ultimul_caracter = cuvant[-1] 
            rezultat.append(primul_caracter + ' ' + ultimul_caracter) 
    

    for item in rezultat:
        print(item)


extrage_prima_ultimul_caracter("Ana are 10 mere, foarte bune")

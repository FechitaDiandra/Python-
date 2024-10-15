def numara_vocale_consoane(text):
    
    vocale = "aeiouAEIOU"
    consoane = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    numar_vocale = 0
    numar_consoane = 0

    for char in text:
        if char in vocale:
            numar_vocale += 1
        elif char in consoane:
            numar_consoane += 1
    
    return numar_vocale, numar_consoane

text = "vata de zahar"
numar_vocale, numar_consoane = numara_vocale_consoane(text)

print(f"Numărul de vocale: {numar_vocale}")
print(f"Numărul de consoane: {numar_consoane}")

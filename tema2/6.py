import re 

def extrage_numar(din_text):
    numar = re.search(r'\d+', din_text) # \d+ = una sau mai multe cifre
    
    if numar:  
        return int(numar.group()) 
    else:
        return None 

text_utilizator = input("Introdu un text: ")


numar_extras = extrage_numar(text_utilizator)


if numar_extras is not None:
    print(f"Numărul extras este: {numar_extras}")
else:
    print("Nu am găsit niciun număr în text.")

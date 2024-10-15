def numara_cuvinte(text):
    # impart textul folosind spatiul ca separator si returnez lungimea listei rezultate
    return len(text.split())


text_utilizator = input("Introdu un text: ")

numar_cuvinte = numara_cuvinte(text_utilizator)

print(f"Numărul de cuvinte în text este: {numar_cuvinte}")

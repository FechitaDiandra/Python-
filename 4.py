def converteste_upper_camel_case_in_snake_case(upper_camel_case):
    rezultat = "" #sir gol init

    for char in upper_camel_case:
        if char.isupper() and rezultat:  # caract maj si nu gol
            rezultat += "_"  # _ bef lit mare
        rezultat += char.lower()  

    return rezultat  

input_utilizator = input("Introdu un șir în format UpperCamelCase: ")
sir_convertit = converteste_upper_camel_case_in_snake_case(input_utilizator)

print("Șirul convertit:", sir_convertit)

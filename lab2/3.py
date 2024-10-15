def convert_to_base(string, number):
    base = len(string)
    result = []
  
    while number > 0:
        remainder = number % base
        result.append(string[remainder])
        number //= base

    result.reverse()
    
    return ''.join(result)


print(convert_to_base("edsc", 432)) 

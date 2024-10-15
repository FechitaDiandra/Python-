def convert_to_hexadecimal(number):
    hex_chars = "0123456789ABCDEF"
    result = []

    
    if number == 0:
        return "0x0"
    
    while number > 0:
        remainder = number % 16
        result.append(hex_chars[remainder])
        number //= 16
    result.reverse()
    return "0x" + ''.join(result)

print(convert_to_hexadecimal(405))

def verifica_paranteze(expresie):
    stack = []

    for char in expresie:
        if char == '(':
            stack.append(char)  
        elif char == ')':
            if not stack:
                return False 
            stack.pop() 
    
    return len(stack) == 0


print(verifica_paranteze("((2+3)*(5-2)/(7+1))")) 
print(verifica_paranteze("((2+3)*(5-2)/(7+1)")) 

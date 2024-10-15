def ex8(x=1, listOfWords=None, flag=True):
    if listOfWords is None:
        listOfWords = [] 

    result = []
    
    for word in listOfWords:
        listOfCharacters = []
        for character in word:
            if flag:
                if ord(character) % x == 0:
                    listOfCharacters.append(character)
            else:
                if ord(character) % x != 0:
                    listOfCharacters.append(character)
        result.append(listOfCharacters)
    
    return result

print("ex8:\n", ex8(2, ["test", "hello", "lab002"], False), "\n")

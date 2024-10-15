def ex7(listOfNumbers):
    listOfPalindroms = []
    biggestPalindrom = 0
    
    for number in listOfNumbers:
        if str(number) == str(number)[::-1]:
            listOfPalindroms.append(number)
            if biggestPalindrom < number:
                biggestPalindrom = number

    return len(listOfPalindroms), biggestPalindrom 


print("ex7:\n", ex7([12321, 1234321, 57875, 146]), "\n")

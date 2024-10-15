import math
def ex2(listOfNumbers):
    listOfPrimeNumbers = []
 
    for number in listOfNumbers:
        isPrime = True
        if number < 2 or (number % 2 == 0 and number != 2):
            isPrime = False
        for divider in range(3, int(math.sqrt(number) + 1), 2):
            if number % divider == 0:
                isPrime = False
                break
        if isPrime:
            listOfPrimeNumbers.append(number)
 
    return listOfPrimeNumbers


if __name__ == '__main__':
    print("ex2:\n", ex2([1, 2, 3, 4, 5, 7, 9, 11, 12, 25]), "\n")  # Only 2,3,5,7,11
def ex1(n):
    a = 1
    b = 1
    fibonacciList = [a, b]
    for i in range(0, n - 2):
        c = a + b
        fibonacciList.append(c)
        a = b
        b = c
    return fibonacciList
def ex1_Recursiv(n):
    fibonacciList = [1, 1]
    for i in range(n, 2, -1):
        fibonacciList.append(fibonacciList[n - i] + fibonacciList[n - i + 1])
    return fibonacciList
 
if __name__ == '__main__':
    print("ex1:\n", ex1(8), "\n")
    print("ex1_recursiv:\n", ex1_Recursiv(8), "\n")
def ex5(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if i > j:
                matrix[i][j] = 0

    return matrix
result = ex5([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
print("ex5:\n", result, "\n")

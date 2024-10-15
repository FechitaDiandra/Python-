def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def ex9(initialMatrix):
    listOfPositions = []
    transposeOfMatrix = transpose(initialMatrix)
    print("The transposed matrix is:")
    for row in transposeOfMatrix:
        print(row)

    for col in range(len(transposeOfMatrix)):
        for row in range(1, len(transposeOfMatrix[col])):
            current_value = transposeOfMatrix[col][row]
            max_values = transposeOfMatrix[col][:row]
            print(f"Current value: {current_value}")
            print(f"Max values before current: {max_values}")
            
            if current_value <= max(max_values, default=float('-inf')): 
                listOfPositions.append((row, col)) 

    return listOfPositions


print("ex9:\n", ex9([[1, 2, 3, 2, 1, 1],
                       [2, 4, 4, 3, 7, 2],
                       [5, 5, 2, 5, 6, 4],
                       [6, 6, 7, 6, 7, 5]]), "\n")

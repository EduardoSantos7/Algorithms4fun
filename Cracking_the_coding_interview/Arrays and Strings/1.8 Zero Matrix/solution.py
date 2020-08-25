def zero_matrix(matrix):
    zeros = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for coor in zeros:
        row, col = coor

        for i in range(0, len(matrix)):
            matrix[row][i] = 0

        for i in range(0, len(matrix[0])):
            matrix[i][col] = 0


# Test
matrix = [
    [0, 1, 2],
    [7, 0, 3],
    [6, 5, 4]
]

zero_matrix(matrix)

print(matrix)

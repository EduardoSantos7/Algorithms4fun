def nullify_row(matrix, i):
    for j in range(len(matrix)):
        matrix[i][j] = 0


def nullify_col(matrix, i):
    for j in range(len(matrix[0])):
        matrix[j][i] = 0


def zero_matrix(matrix):
    first_row_has_zeros = False
    first_col_has_zeros = False

    for i in range(0, len(matrix)):
        if matrix[i][0]:
            first_row_has_zeros = True
            break

    for i in range(0, len(matrix)):
        if matrix[0][i]:
            first_col_has_zeros = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            # Nullify
            nullify_row(matrix, row)

    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            # Nullify
            nullify_col(matrix, col)

    if first_row_has_zeros:
        nullify_row(matrix, 0)

    if first_col_has_zeros:
        nullify_col(matrix, 0)


# Test
matrix = [
    [0, 1, 2],
    [7, 0, 3],
    [6, 5, 4]
]

zero_matrix(matrix)

print(matrix)

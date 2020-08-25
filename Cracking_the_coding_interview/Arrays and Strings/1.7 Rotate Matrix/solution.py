# Rotate in place
def rotate(matrix):
    if not matrix or not matrix[0]:
        return False

    for layer in range(0, len(matrix) // 2):
        first = layer
        last = len(matrix) - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # Save the top

            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

    return True


# Test
matrix = [
    [0, 1, 2],
    [7, 8, 3],
    [6, 5, 4]
]

rotate(matrix)

print(matrix)

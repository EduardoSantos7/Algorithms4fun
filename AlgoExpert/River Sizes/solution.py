def riverSizes(matrix):
    sizes = []

    visited = [[False for _ in range(len(matrix[0]))] for _ in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverse(i, j, matrix, visited, sizes)
    return sizes


def traverse(i, j, matrix, visited, sizes):
    stack = [[i, j]]
    size = 0

    while len(stack):
        node = stack.pop()
        i = node[0]
        j = node[1]

        if visited[i][j]:
            continue
        visited[i][j] = True
        if not matrix[i][j]:
            continue

        size += 1

        stack.extend(getUnvisitedNeighbors(i, j, matrix, visited))

    if size:
        sizes.append(size)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors

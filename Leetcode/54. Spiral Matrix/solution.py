class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        result = []
        ops = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        i, j, current_op = 0, 0, 0

        def is_valid_move(i, j):
            return i >= 0 and i < rows and j >= 0 and j < cols

        for _ in range(rows*cols):
            if is_valid_move(i, j) and (i, j) not in visited:
                result.append(matrix[i][j])
                visited.add((i, j))
            
            action = ops[current_op%4]
            next_i, next_j = i + action[0], j + action[1]
            
            if not is_valid_move(next_i, next_j) or (is_valid_move(next_i, next_j) and (next_i, next_j) in visited):
                current_op += 1
                action = ops[current_op%4]
                next_i, next_j = i + action[0], j + action[1]

            i, j = next_i, next_j
        
        return result

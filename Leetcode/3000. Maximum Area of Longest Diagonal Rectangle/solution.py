class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        biggest_diagonal = 0
        current_area_biggest_diagonal = 0

        for dimension in dimensions:
            x, y = dimension
            current_diagonal = math.sqrt(x*x + y*y)
            if current_diagonal > biggest_diagonal:
                biggest_diagonal = current_diagonal
                current_area_biggest_diagonal = x * y
            elif current_diagonal == biggest_diagonal:
                current_area = x*y
                if current_area > current_area_biggest_diagonal:
                    current_area_biggest_diagonal = current_area
                    biggest_diagonal = current_diagonal
        
        return current_area_biggest_diagonal
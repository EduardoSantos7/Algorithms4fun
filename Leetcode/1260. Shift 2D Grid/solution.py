class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols
        k = k % total  # Only shift necessary positions
        
        start = 0
        count_visited = 0
        
        while count_visited < total:
            current_index = start
            current_value = grid[current_index // cols][current_index % cols]
            
            while True:
                # Calculate new position
                next_index = (current_index + k) % total
                next_value = grid[next_index // cols][next_index % cols]
                
                # Place the current value into its new position
                grid[next_index // cols][next_index % cols] = current_value
                current_index = next_index
                current_value = next_value
                count_visited += 1
                
                # If we are back to the start, break the loop
                if current_index == start:
                    break
            
            start += 1  # Move to the next starting position to check other cycles
        
        return grid

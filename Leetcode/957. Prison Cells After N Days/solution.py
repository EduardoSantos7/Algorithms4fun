class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        mem = {}
        while(N > 0):
            cells_tup = tuple(cells)
            if cells_tup in mem:
                # Adjust N using frequency
                N %= mem[cells_tup] - N

            mem[cells_tup] = N

            if N >= 1:
                N -= 1
                # Get the new day
                cells = [1 if i > 0 and i < 7 and cells[i - 1]
                         == cells[i + 1] else 0 for i in range(8)]

        return cells

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_count = []

        for i, row in enumerate(mat):
            row_count.append((i, row.count(1)))

        # Sort by ones count
        row_count.sort(key=lambda x: x[1])

        return [elem[0] for elem in row_count[:k]]

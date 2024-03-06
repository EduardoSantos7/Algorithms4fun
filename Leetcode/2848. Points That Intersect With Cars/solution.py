class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        coordinates_covered = set()
        for coordinates in nums:
            coordinates_covered.update([i for i in range(coordinates[0],coordinates[1] + 1)])
        return len(coordinates_covered)
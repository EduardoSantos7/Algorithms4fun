class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Initialize the seen array with an extra space to avoid boundary issues
        seen = [0] * 52

        # Apply the difference array technique
        for start, end in ranges:
            seen[start] += 1
            seen[end + 1] -= 1

        # Compute the prefix sums to get the actual coverage
        for i in range(1, 52):
            seen[i] += seen[i - 1]
        
        # Check if all elements from left to right are covered
        for i in range(left, right + 1):
            if seen[i] == 0:
                return False

        return True
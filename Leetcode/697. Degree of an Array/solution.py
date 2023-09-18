class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Store count, first occurrence, and last occurrence for each number
        count, first, last = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1
        
        # Init a variable to keep the min length of a subarray
        min_length = float('inf')  # Set to infinity as a start

        # Find the maximum frequency
        degree = max(count.values())

        # For every number with the max freq, find its first and last occurrence in the data
        for x in count:
            if count[x] == degree:
                min_length = min(last[x] - first[x] + 1, min_length)

        # Return the minimum
        return min_length

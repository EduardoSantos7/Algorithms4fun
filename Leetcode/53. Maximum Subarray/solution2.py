class Solution:
    def maxSubArray(self, array: List[int]) -> int:
        maxEnding = array[0]
        maxSoFar = array[0]

        for i in range(1, len(array)):
            maxEnding = max(maxEnding + array[i], array[i])
            maxSoFar = max(maxSoFar, maxEnding)

        return maxSoFar

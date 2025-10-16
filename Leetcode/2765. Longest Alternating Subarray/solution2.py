class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        i = 0
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            # Start of alternating subarray
            j = i + 2
            expected = -1  # next diff should be -1
            while j < n and nums[j] - nums[j - 1] == expected:
                expected *= -1
                j += 1
            ans = max(ans, j - i)
            i = j - 1
        return ans
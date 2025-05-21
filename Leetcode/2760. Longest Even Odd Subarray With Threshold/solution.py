class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n, longest_len = len(nums), 0

        for i, left in enumerate(nums):
            if left % 2 != 0 or left > threshold:
                continue
            
            right = i

            while right < n and nums[right] <= threshold and (right == i or nums[right] % 2 != nums[right - 1] % 2):
                right += 1

            longest_len = max(longest_len, right - i)
        
        return longest_len

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        if(n == 0):
            return 0

        prefix_idx, suffix_idx = 0, n - 1

        while(prefix_idx + 1 < n and nums[prefix_idx + 1] > nums[prefix_idx]):
            prefix_idx += 1

        if(prefix_idx == n - 1):
            return (n*(n + 1)) // 2
        
        while(suffix_idx > 0 and nums[suffix_idx] > nums[suffix_idx - 1]):
            suffix_idx -= 1
        
        result += prefix_idx + 1
        result += n - suffix_idx + 1

        i = 0
        j = suffix_idx 
        while(i <= prefix_idx):
            while(j < n and nums[i] >= nums[j]):
                j += 1
            result += n - j
            i += 1
        return result

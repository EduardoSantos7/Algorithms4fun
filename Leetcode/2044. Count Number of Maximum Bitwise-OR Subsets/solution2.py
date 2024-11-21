class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        
        n = len(nums)
        total_subsets = 1 << n
        subsets_with_max_or = 0

        for subset in range(total_subsets):
            current_or = 0
            for i in range(n):
                if (subset >> i) & 1:
                    current_or |= nums[i]

            if current_or == max_or_value:
                subsets_with_max_or += 1
        
        return subsets_with_max_or
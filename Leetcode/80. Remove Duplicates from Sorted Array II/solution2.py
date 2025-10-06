class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i - 1] == nums[i - 2] == nums[i]:
                del nums[i]
                continue
            i += 1

        return len(nums)

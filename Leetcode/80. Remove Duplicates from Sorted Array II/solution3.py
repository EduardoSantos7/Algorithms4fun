class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        writter = 2
        for reader in range(2, len(nums)):
            if nums[reader] != nums[writter - 2]:
                nums[writter] = nums[reader]
                writter += 1

        return writter

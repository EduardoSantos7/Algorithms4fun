class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        return self.count_subsets(nums, 0, 0, max_or_value)

    def count_subsets(self, nums, index, current_or, max_or) -> int:
        if index == len(nums):
            return 1 if current_or == max_or else 0

        count_withouth = self.count_subsets(nums, index + 1, current_or, max_or)
        count_with = self.count_subsets(nums, index + 1, current_or | nums[index], max_or)

        return count_with + count_withouth

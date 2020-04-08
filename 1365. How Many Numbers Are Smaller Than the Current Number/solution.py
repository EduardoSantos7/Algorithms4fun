class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        counter = {}

        for i, num in enumerate(sorted_nums):
            if num not in counter:
                counter[num] = i

        return [counter[num] for num in nums]

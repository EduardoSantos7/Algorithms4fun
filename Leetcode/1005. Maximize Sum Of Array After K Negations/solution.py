class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0

        while(nums[i] < 0 and i < k and i < len(nums) - 1):
            nums[i] = -nums[i]
            i += 1

        k -= i

        if k % 2 is not 0:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
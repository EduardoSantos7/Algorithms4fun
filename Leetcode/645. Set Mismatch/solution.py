class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = None
        missing = 1

        for num in nums:
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1

        for i in range(1, len(nums)):
            if(nums[i] > 0):
                missing = i + 1

        return [dup, missing]

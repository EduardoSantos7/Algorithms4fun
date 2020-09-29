class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            maxi = nums[0]
            cur = nums[0]

            if len(nums) == 1:
                return nums[0]

            for num in nums[1:]:
                if cur < 0:
                    cur = num
                else:
                    cur += num
                maxi = max(cur, maxi)

            return maxi

        return 0

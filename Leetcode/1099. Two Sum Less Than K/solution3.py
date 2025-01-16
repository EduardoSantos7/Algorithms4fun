class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            temp_sum = nums[p1] + nums[p2]
            if temp_sum < k:
                max_sum = max(max_sum, temp_sum)
                p1 += 1
            else:
                p2 -= 1
        return max_sum
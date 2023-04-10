class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total_count = sum(nums)
        count_left = 0
        ans = [0] * len(nums)

        for i, num in enumerate(nums):
            count_right = total_count - count_left - num
            ans[i] = abs(count_left - count_right)
            count_left += num

        return ans

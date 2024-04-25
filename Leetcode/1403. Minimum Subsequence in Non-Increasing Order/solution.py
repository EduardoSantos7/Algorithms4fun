class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = sum(nums)
        subsequence = []
        temp = 0
        i = len(nums) - 1
        while temp <= count:
            biggest = nums[i]
            i -= 1
            temp += biggest
            count -= biggest
            subsequence.append(biggest)

        return subsequence
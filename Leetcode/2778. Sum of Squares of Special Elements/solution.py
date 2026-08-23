class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                j = n // i
                total += nums[i - 1] * nums[i - 1]
                if j != i:
                    total += nums[j - 1] * nums[j - 1]
            i += 1
        return total

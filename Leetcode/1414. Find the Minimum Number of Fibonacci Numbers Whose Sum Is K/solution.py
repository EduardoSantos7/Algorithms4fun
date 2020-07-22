class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f1 = 1
        f2 = 1
        nums = [f1, f2]
        while f2 < k:
            temp = f2 + f1
            f1 = f2
            f2 = temp
            nums.append(f2)

        count = 0
        res = 0

        for num in reversed(nums):
            if count + num <= k:
                count += num
                res += 1

        return res

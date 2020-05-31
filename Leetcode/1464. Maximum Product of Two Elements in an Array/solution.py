class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Find the 2 biggest values
        val_1, val_2 = 0, 0

        for num in nums:
            if num > val_1:
                val_2 = val_1
                val_1 = num
            elif num > val_2:
                val_2 = num

        return (val_1 - 1) * (val_2 - 1)

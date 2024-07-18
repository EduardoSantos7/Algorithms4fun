class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_sorted = sorted([nums[n] for n in range(0, len(nums), 2)])
        odd_sorted = reversed(sorted([nums[n] for n in range(1, len(nums), 2)]))
        res = [0] * len(nums)
        i = 0
        for n in even_sorted:
            res[i] = n
            i += 2
        i = 1
        for n in odd_sorted:
            res[i] = n
            i += 2
        return res
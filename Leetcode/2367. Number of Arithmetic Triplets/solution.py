class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if (num - diff) in nums_set and (num - (2*diff)) in nums_set:
                ans += 1
        
        return ans
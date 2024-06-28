class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        
        left = 0
        right = len(nums)
        
        for freq in c.values():
            right -= freq
            res += left * freq * right
            left += freq
        
        return res
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        base = len(nums) - 1
        
        if nums[-1] != base:
            return False
        
        for i in range(base):
            if i+1 != nums[i]:
                return False
        
        return True
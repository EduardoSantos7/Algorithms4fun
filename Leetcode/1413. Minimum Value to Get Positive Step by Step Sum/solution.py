class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr=0
        min_val=0
        for i in range(len(nums)):
            curr=curr+nums[i]
            min_val=min(curr, min_val)
        
        return -min_val+1
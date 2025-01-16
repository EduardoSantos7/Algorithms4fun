class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        mem = set()

        for i in range(1, len(nums)):
            _sum = nums[i] + nums[i-1]

            if _sum in mem:
                return True
            
            mem.add(_sum)
        
        return False
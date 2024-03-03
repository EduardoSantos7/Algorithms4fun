class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mem = set(nums)

        while original in mem:
            original *= 2
        
        return original
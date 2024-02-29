class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        
        return len(s) == 0
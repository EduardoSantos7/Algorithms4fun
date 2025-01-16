class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        mem = set()

        for n in nums:
            if n in mem:
                res.append(n)
                if len(res) == 2:
                    return res
            
            mem.add(n)
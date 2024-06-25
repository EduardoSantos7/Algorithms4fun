class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mem = set()
        ans = 0
        for num in nums:
            if num not in mem:
                mem.add(num)
            else:
                mem.remove(num)
                ans += 1
        return [ans, len(mem)]
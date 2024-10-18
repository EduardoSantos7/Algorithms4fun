class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mem = {}
        ans = 0
        for i in range(0, len(nums)):
            if mem.get(nums[i]):
                ans += len([n for n in mem.get(nums[i]) if n * i % k == 0] or [])
                mem[nums[i]].append(i)
            else:
                mem[nums[i]] = [i]
        
        return ans

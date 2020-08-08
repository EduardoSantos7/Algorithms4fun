class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mem = {}
        pairs = 0
        for num in nums:
            count = mem.get(num, 0)

            if count:
                pairs += count

            mem[num] = count + 1

        return pairs

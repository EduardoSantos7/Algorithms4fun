class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mem = {}
        pairs = 0
        for cur_num in nums:
            pairs += mem.get(k + cur_num, 0)
            pairs += mem.get(-k + cur_num, 0)
            mem[cur_num] = mem.get(cur_num, 0) + 1
        return pairs
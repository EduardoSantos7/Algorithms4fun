class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([target_num for i, target_num in enumerate(nums) if bin(i).count("1") == k])
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, elem in enumerate(nums):
            other_num = target - elem
            if other_num in mem:
                return [mem[other_num], i]
            else:
                mem[elem] = i

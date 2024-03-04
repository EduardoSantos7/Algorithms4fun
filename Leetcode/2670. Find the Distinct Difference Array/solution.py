class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # Get Frequencies
        mem = {}
        for num in nums:
            mem[num] = mem.get(num) + 1 if mem.get(num) else 1
        
        left_set = set()
        diff = [0] * len(nums)

        for i, num in enumerate(nums):
            left_set.add(num)
            mem[num] -= 1

            if mem[num] == 0:
                del mem[num]
            
            diff[i] = len(left_set) - len(mem)
        
        return diff
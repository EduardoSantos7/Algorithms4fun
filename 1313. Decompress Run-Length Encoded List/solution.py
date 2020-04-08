class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums), 2):
            freq = nums[index]
            value = nums[index + 1]
            for episodes in range(freq):
                result.append(value)
        return result

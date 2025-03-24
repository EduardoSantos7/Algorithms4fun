class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use hastables to map the number in the arrays and its position
        mem = {}
        for i, num in enumerate(nums2):
            mem[num] = i

        # create an array where the value in index i is the position of arr[i] in nums2
        mapping = [0] * len(nums1)
        for i, num in enumerate(nums1):
            mapping[i] = mem[num]

        return mapping
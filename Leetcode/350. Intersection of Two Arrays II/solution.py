class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = dict()
        for num in nums1:
            mem[num] = mem.get(num, 0) + 1

        res = list()
        for num in nums2:
            if num in mem and mem[num] > 0:
                res.append(num)
                mem[num] -= 1

        return res

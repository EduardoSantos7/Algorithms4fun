class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = 0, 0
        set_nums1, set_nums2 = set(nums1), set(nums2)

        for num in nums1:
            if num in set_nums2:
                a += 1
        
        for num in nums2:
            if num in set_nums1:
                b += 1

        return [a, b]

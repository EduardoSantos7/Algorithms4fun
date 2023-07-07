class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        return set(list(set.intersection(set1, set2)) + list(set.intersection(set1, set3)) + list(set.intersection(set3, set2)))
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Create counter arrays for num1 and num2
        counts_1, counts_2 = [0] * 101, [0] * 101
        for num1, num2 in zip(nums1, nums2):
            counts_1[num1] += 1
            counts_2[num2] += 1
        # Use two pointer to go through the counter arrays, one from the beggining and the other from the end
        p1, p2, result = 1, 100, 0

        while p1 <= 100 or p2 > 0:
            while p1 <= 100 and counts_1[p1] == 0:
                p1 += 1
            while p2 > 0 and counts_2[p2] == 0:
                p2 -= 1
            if p1 == 101 or p2 == 0:
                break
            
            used = min(counts_1[p1], counts_2[p2])
            result += used*p1*p2
            counts_1[p1] -= used
            counts_2[p2] -= used

        return result

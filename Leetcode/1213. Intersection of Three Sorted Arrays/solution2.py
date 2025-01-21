class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        range_nums = [0] * 2001
        for num in arr1 + arr2 + arr3:
            range_nums[num] += 1
        ans = []
        for i, num in enumerate(range_nums):
            if num == 3:
                ans.append(i)
        return ans

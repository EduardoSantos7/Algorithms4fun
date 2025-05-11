class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        ans = [0] * N
        smaller = 0
        greater = N - 1

        for i, j in zip(range(N), range(N-1, -1, -1)):
            if nums[i] < pivot:
                ans[smaller] = nums[i]
                smaller += 1

            if nums[j] > pivot:
                ans[greater] = nums[j]
                greater -= 1

        while smaller <= greater:
            ans[smaller] = pivot
            smaller += 1

        return ans

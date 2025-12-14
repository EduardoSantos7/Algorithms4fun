class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [0]
        l = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                x = stack.pop(-1)
                l[i] = max(l[x], l[i])
            if len(stack) > 0:
                l[i] = l[i] + 1
            stack.append(i)
        return max(l)

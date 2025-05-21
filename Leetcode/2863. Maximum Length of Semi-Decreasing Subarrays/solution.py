class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []                # índices de picos
        for i, v in enumerate(nums):
            if not stack or v > nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for r in range(n - 1, -1, -1):
            while stack and stack[-1] >= r:        # inicio no válido
                stack.pop()
            while stack and nums[stack[-1]] > nums[r]:
                ans = max(ans, r - stack[-1] + 1)  # longitud del sub‑array
                stack.pop()                        # probar pico más a la izq.
        return ans

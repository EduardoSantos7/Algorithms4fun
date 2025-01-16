class Solution:
    def minElement(self, nums: List[int]) -> int:
        _min = 100 # max

        for num in nums:
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
                # If it's already bigger than min don't continue
                if temp >= _min:
                    break

            _min = min(_min, temp)

        return _min

# One liner
# class Solution:
#     def minElement(self, nums: List[int]) -> int:
#         return min(map(lambda x: sum([int(n) for n in str(x)]), nums))
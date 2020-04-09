class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        seen = {}
        for num in nums:
            if num in seen:
                if not seen[num] % 2:
                    result += 1
                continue
            count = 0
            while num > 0:
                num //= 10
                count += 1
            seen[num] = count
            if not count % 2:
                result += 1
        return result

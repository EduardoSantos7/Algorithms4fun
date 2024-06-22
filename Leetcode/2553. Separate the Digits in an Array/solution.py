class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            temp = []
            while num > 0:
                x = num % 10
                num //= 10
                temp.append(int(x))
            ans.extend(temp[::-1])
        return ans
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0

        for digit in str(num):
            if num % int(digit) == 0:
                ans += 1
        
        return ans
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        _max = -1
        for a in range(len(num) - 2):
            if num[a] == num[a+1] == num[a+2]:
                sub = num[a:a + 3]
                _max = max(_max, int(sub))
            a += 1
        
        return str(_max) if _max > 0 else "000" if _max == 0 else ""
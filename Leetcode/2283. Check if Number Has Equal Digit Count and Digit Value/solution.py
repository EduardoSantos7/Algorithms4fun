class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i in range(len(num)):
            if num[i] != str(count[str(i)]):
                return False
        
        return True
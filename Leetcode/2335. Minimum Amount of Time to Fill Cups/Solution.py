class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0
        while(any(amount)):
            amount.sort()
            if amount[-1] > 0:
                amount[-1] -= 1
            if amount[-2] > 0:
                amount[-2] -= 1
            seconds += 1
        
        return seconds
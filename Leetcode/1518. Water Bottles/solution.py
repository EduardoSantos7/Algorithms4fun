class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            numBottles = emptyBottles // numExchange
            ans += numBottles
            emptyBottles = emptyBottles % numExchange + numBottles
        
        return ans
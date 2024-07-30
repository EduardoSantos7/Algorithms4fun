class Solution:
    def fillCups(self, amount):
        amount.sort()
        
        # The total number of cups
        total_cups = sum(amount)
        
        # If the largest amount is greater than or equal to the sum of the other two
        # Otherwise, the answer is the ceiling of total_cups / 2
        return amount[2] if amount[2] >= amount[0] + amount[1] else (total_cups + 1) // 2
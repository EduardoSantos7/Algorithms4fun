class Solution:
    def largestInteger(self, num: int) -> int:
        # Keep a mem of even or odds:
        nums_str = str(num)
        parities = [(1 if int(digit) % 2 else 0) for digit in nums_str]
        # Sort digits
        digits_sorted = reversed(sorted([int(d) for d in nums_str]))
        # Separate digits by parity
        evens, odds = [], []
        for digit in digits_sorted:
            if digit % 2:
                odds.append(digit)
                continue
            evens.append(digit)
        # Assign the digits to its new position
        odd, even = 0, 0
        for i in range(len(parities)):
            if parities[i]:
                parities[i] = str(odds[odd])
                odd += 1
                continue
            parities[i] = str(evens[even])
            even += 1
        
        return int("".join(parities))
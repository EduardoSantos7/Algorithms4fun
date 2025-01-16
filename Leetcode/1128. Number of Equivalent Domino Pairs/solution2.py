from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Array to store frequency of domino pairs
        count = [0] * 100
        pairs = 0
        
        for domino in dominoes:
            # Sort the domino to handle rotation equivalence
            key = min(domino) * 10 + max(domino)  # Encodes (a, b) uniquely where a <= b
            # Increment the count of equivalent pairs
            pairs += count[key]
            # Update the frequency for this key
            count[key] += 1
        
        return pairs

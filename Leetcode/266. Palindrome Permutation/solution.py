class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq  = Counter(s)

        if len(s) % 2 == 0:
            return all([x % 2 == 0 for x in freq.values()])
        else:
            odd_freq_seen = False

            for val in freq.values():
                if val % 2 != 0 and not odd_freq_seen:
                    odd_freq_seen = True
                elif val % 2 != 0 and odd_freq_seen:
                    return False
            
            return True

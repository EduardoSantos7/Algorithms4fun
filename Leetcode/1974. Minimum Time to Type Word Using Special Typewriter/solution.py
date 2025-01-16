class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds, prev = len(word), 'a'

        for current in word:
            diff = abs(ord(current) - ord(prev))
            seconds += min(diff, 26 - diff)
            prev = current
        
        return seconds

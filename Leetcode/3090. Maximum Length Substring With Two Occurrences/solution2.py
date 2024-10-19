class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = j = 0
        mem = Counter()

        for i, start_c in enumerate(s):
            mem[start_c] += 1

            while mem[start_c] == 3:
                mem[s[j]] -= 1
                j += 1
            
            max_len = max(max_len, i - j + 1)

        return max_len
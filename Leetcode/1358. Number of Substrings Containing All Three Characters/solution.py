class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mem = {'a': 0, 'b': 0, 'c': 0}
        start_window = 0
        count = 0

        for end_window in range(len(s)):
            mem[s[end_window]] += 1

            while(all(mem.values())):
                count += len(s) - end_window
                mem[s[start_window]] -= 1
                start_window += 1

        return count

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        last = len(s) - 1
        for i, c in enumerate(s):
            if c == 'I':
                count += 1 if i == last or s[i + 1] not in ['V', 'X'] else - 1
            elif c == 'V':
                count += 5
            elif c == 'X':
                count += 10 if i == last or s[i +
                                              1] not in ['L', 'C'] else - 10
            elif c == 'L':
                count += 50
            elif c == 'C':
                count += 100 if i == last or s[i +
                                               1] not in ['D', 'M'] else - 100
            elif c == 'D':
                count += 500
            elif c == 'M':
                count += 1000

        return count

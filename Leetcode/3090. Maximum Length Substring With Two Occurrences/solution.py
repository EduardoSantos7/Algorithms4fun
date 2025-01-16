class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 1

        for i, start_c in enumerate(s):
            mem = {start_c: 1}
            flag = True
            for j in range(i + 1, len(s)):
                temp_c = s[j]
                if temp_c not in mem:
                    mem[temp_c] = 1
                else:
                    mem[temp_c] += 1

                if mem[temp_c] > 2:
                    max_len = max(max_len, j - i)
                    flag = False
                    break

            if flag:
                max_len = max(max_len, len(s) - i)

        return max_len
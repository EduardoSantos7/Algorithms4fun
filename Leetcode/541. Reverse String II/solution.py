class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        i = 0
        step = 2*k

        def reverse(word):
            return ''.join([word[:k][::-1], word[k:]])
        while i >= 0 and i <= len(s):
            temp.append(reverse(s[i:i + step]))
            i += step

        return ''.join(temp)

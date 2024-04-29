class Solution:
    def replaceDigits(self, s: str) -> str:
        s_arr = list(s)

        for i in range(1, len(s), 2):
            s_arr[i] = chr(ord(s_arr[i-1]) + int(s_arr[i]))
    
        return ''.join(s_arr)
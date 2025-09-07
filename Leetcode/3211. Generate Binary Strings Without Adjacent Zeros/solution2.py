class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        temp = ""
        self.find_valid_strings(temp, ans, 0, n, 0, 0)
        return ans
    
    def find_valid_strings(self, temp, ans, i, n, prev, curr):
        if prev == '0' and curr == '0':
            return
        
        if i == n:
            ans.append(temp)
            return
        
        temp += '0'
        self.find_valid_strings(temp, ans, i + 1, n, curr, '0')
        temp = temp[:-1]
        temp += '1'
        self.find_valid_strings(temp, ans, i + 1, n, curr, '1')
        temp = temp[:-1]
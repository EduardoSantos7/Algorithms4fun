class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        for num in range(0, 2 ** n):
            binary_string = bin(num)[2:].zfill(n) # remove "0b"
            if "00" not in binary_string:
                ans.append(binary_string)
        return ans
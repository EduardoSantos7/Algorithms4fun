class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        new_number = ""

        for digit in str(num):
            if digit not in strobogrammatic:
                return False
            new_number += strobogrammatic[digit]

        return new_number[::-1] == num
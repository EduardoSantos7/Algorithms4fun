class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        left = 0
        right = len(num) - 1

        while left <= right:
            if num[left] not in strobogrammatic or strobogrammatic[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0

        for start in range(len(num_str)):
            substring = num_str[start:start + k]
            sub_num = int(substring)

            if len(substring) != k or sub_num == 0:
                continue

            if num % int(substring) == 0:
                count += 1
        
        return count
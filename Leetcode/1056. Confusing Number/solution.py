class Solution:
    def confusingNumber(self, n: int) -> bool:
        stack = []
        str_n = str(n)
        num_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        for num in str_n[::-1]:
            if num not in num_map:
                return False
            else:
                stack.append(num_map[num])

        return "".join(stack) != str_n

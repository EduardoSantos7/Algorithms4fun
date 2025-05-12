class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindrome(number):
            number_str = str(number)
            for i, j in zip(range(len(number_str)), range(len(number_str) - 1, -1, -1)):
                if j < i:
                    return True

                if number_str[i] != number_str[j]:
                    return False

        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return "".join(str(i) for i in digits[::-1])

        for base in range(2, n - 1):
            new_number = numberToBase(n, base)
            if not is_palindrome(new_number):
                return False

        return True

class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        numbers.sort()

        for num1, num2 in pairwise(numbers):
            if num2.startswith(num1):
                return False

        return True

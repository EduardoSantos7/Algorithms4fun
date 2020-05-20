class Solution:
    def maxScore(self, s: str) -> int:
        left_pointer = len(s) - 2
        right_pointer = len(s) - 1

        # Init score values
        right = 1 if s[right_pointer] == '1' else 0
        left = s[:-1].count('0')
        max_score = left + right

        while left_pointer > 0:
            # substract the current value in left and add it in right
            if s[left_pointer] == '0':
                left -= 1
            elif s[left_pointer] == '1':
                right += 1

            # Update score
            max_score = max(max_score, left + right)
            # Move pointer
            left_pointer -= 1
            right_pointer -= 1

        return max_score

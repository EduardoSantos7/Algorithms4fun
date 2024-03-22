class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word: str):
            left, right = 0, len(word) - 1
            while(left <= right):
                print(right)
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""
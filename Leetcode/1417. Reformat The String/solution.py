class Solution:
    def reformat(self, s: str) -> str:
        nums, letters = [], []
        for c in s:
            if c.isnumeric():
                nums.append(c)
                continue
            letters.append(c)
        
        if abs(len(nums) - len(letters)) > 1:
            return ""
        
        bigger, smaller = (nums, letters) if len(nums) > len(letters) else (letters, nums)
        combined = "".join([char1 + char2 for char1, char2 in zip_longest(bigger, smaller, fillvalue='')])
        return combined
        
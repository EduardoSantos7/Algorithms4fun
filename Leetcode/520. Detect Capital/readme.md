# Algorithm Idea

Initialize all_lower and all_upper as True. Then, we iterate through each character in the word starting from the second character. Check the ASCII value of each character and update the all_lower and all_upper variables accordingly. If at any point both all_lower and all_upper become False, we can immediately return False because the capitalization rule is violated. Finally, we return all_lower or all_upper if the ASCII value of the first character is within the range of uppercase letters (65-90). Otherwise, we return all_lower since the first character is expected to be lowercase.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
48 ms
Beats
40.66%
Memory
16.3 MB
Beats
16.45%
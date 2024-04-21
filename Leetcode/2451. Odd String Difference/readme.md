# Algorithm Idea

A dictionary called mem_vals is created to store the alphabet position of each character (e.g., 'a' = 0, 'b' = 1, etc.) for quick access. This is used to avoid recalculating these positions multiple times for the same letter.

The method get_difference is defined to calculate the differences between the alphabet positions of adjacent letters within a word. For example, for the word "abc", the differences would be [1, 1] because b-a=1 and c-b=1.

The get_difference function iterates through each pair of adjacent letters in a word.
It checks if the alphabet position of each letter is already stored in mem_vals; if not, it calculates this position and stores it.
Then, it calculates the difference between the positions of the current and next letters and appends this difference to a list.
This list of differences for the entire word is returned.

calculates the pattern of differences for the first three words in the list and checks if all these patterns are the same using the all_same function. The all_same function returns True if all elements in a list are identical.

If all three initial words have the same pattern of differences, the algorithm assumes there is a common pattern and iterates through the rest of the words to find the one that doesn't match this pattern.
If the first three words do not all share the same pattern, the algorithm immediately identifies the odd one out based on which ones do match. It compares the first three patterns to each other to determine this:
If the first and second word have the same pattern, the third word is the odd one.
If the second and third word have the same pattern, the first word is the odd one.
Otherwise, the second word is considered the odd one.

# Complexity

- Time: O(w*(n-1)) w = the length of of words and n = the length of characters

- Space:O(1)

# Results

Runtime
37
ms
Beats
60.56%
of users with Python3
Memory
16.59
MB
Beats
75.43%
of users with Python3
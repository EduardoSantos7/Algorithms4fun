# Algorithm Idea

Get the frequencies of the chars in the string.
Repeat while any frequency values are greater than 0:
Iterate from a to z looking for this letter in the freq map. If found then append it to the result array/string and decrease its frequency by 1.
Iterate from z to a looking for this letter in the freq map. If found then append it to the result array/string and decrease its frequency by 1.
Return concatenated array/string.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
52
ms
Beats
79.49%
of users with Python3

Memory
16.66
MB
Beats
45.42%
of users with Python3
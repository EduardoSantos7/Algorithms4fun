# Algorithm Idea

Sort the array, use two pointers, one at 0 and the other at n -1, where n is the length of the array. If the sum of the numbers pointed is less or equal to the target increment a variable answer by 2^(right - left) which represent the combnation in that range.

# Complexity

- Time: O(n*logn)

- Space:O(1)

# Results

Runtime
813 ms
Beats
80.82%
Memory
28.5 MB
Beats
15.98%
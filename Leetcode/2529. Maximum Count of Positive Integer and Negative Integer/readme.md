# Algorithm Idea

Init two pointers, one in the start and the other one and the end of the array, if these pointers have the same sign then return the length of the array.

if not, while the start pointer is in the boundaries of the array and the number it's pointing at is equals or less than 0, increment the pointer and if it's 0 then increment the zeros found.

Return the max between the positive numbers (length of the array minus the position of the start pointer), and the negative numbers (start pointer - zero count)

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
98
ms
Beats
91.07%
of users with Python3

Memory
16.86
MB
Beats
75.65%
of users with Python3